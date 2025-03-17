from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import google.generativeai as genai
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import CodeSnippet

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def index(request):
    return render(request, 'editor/index.html',{'username': request.user.username})

@login_required
def user(request):
    theme = request.GET.get('theme', 'light')
    print(theme)
    return render(request, 'editor/user.html',{'username': request.user.username, 'theme': theme})

#On run code button
@csrf_protect
@login_required
def run_code(request):
    if request.method == 'POST':
        try:
            # Parse incoming data
            data = json.loads(request.body)
            code = data.get('code', '')
            language = data.get('language', '')
            inputs = data.get('inputs', '')

            mapping = {'text/x-java':'4','python':'5','text/x-csrc':'6','text/x-c++src':'7','javascript':'17'}
            lang=mapping[language]   #language for compiler

            # Compiler API configuration
            url = "https://code-compiler.p.rapidapi.com/v2"
            
            payload = {
                "LanguageChoice": lang,  # language
                "Program": code,  # The actual code from the editor
                "Input": inputs  # inputs from editor if any
            }
            
            headers = {
                "x-rapidapi-key": "3a123a404cmshf5483e521d7da6fp14ce7bjsnb90b0f6ca183",
                "x-rapidapi-host": "code-compiler.p.rapidapi.com",
                "Content-Type": "application/x-www-form-urlencoded"
            }

            # Make API request
            response = requests.post(url, data=payload, headers=headers)
            
            # Convert response to JSON
            result = response.json()
            
            # Return the result
            return JsonResponse({
                'output': result.get('Result', 'No output'),
                'errors': result.get('Errors', '')
            })
            
        except requests.RequestException as e:
            return JsonResponse({
                'error': f'API Error: {str(e)}'
            }, status=500)
            
        except json.JSONDecodeError as e:
            return JsonResponse({
                'error': f'Invalid JSON: {str(e)}'
            }, status=400)
            
        except Exception as e:
            return JsonResponse({
                'error': f'Server Error: {str(e)}'
            }, status=500)
    
    return JsonResponse({
        'error': 'Method not allowed'
    }, status=405)


#On ask AI (submit) button
@csrf_protect
@login_required
def process_sidebar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            purpose = data.get('purpose', '')
            
            #sending to Gemini
            genai.configure(api_key="AIzaSyDxiigaZNe4TTzdDojZOoQfOC-PjnTLiw4")
            generation_config = {
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            }
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config=generation_config,
            )

            chat = model.start_chat()
            if purpose=='a':
                prompt='Generate a code snippet for the following. Do not include any other text, or letters or punctuations. Just give one code. Thats it.'
            elif purpose=='b':
                prompt='Debug the following code. Briefly explain what is wrong and what can be corrected.'
            elif purpose=='d':
                prompt='Please briefly tell me what the following error means.'
            else:
                prompt='Please answer the following query briefly.'
            
            warning ='Do Not include any Bold Words.'
            prompt+= text
            prompt+=warning
            ai_response = chat.send_message(prompt)

            return JsonResponse({'output': ai_response.text})  # Sending result back.
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@login_required
def get_saved_codes(request):
    codes = CodeSnippet.objects.filter(user=request.user)
    return JsonResponse({
        'codes': list(codes.values('id', 'title', 'code', 'language','created_at','desc'))
    })

@login_required
def search_view(request):
    query = request.GET.get('query', '')  # Get the search query
    if not query:
        results = CodeSnippet.objects.filter(user=request.user).values(
            'id', 'title', 'code', 'language', 'created_at', 'desc'
        )
    else:
        # Fetch matching results
        results = CodeSnippet.objects.filter(user=request.user, title__icontains=query).values(
            'id', 'title', 'code', 'language','created_at','desc'  # Add more fields if needed
        )
    return JsonResponse({'codes': list(results)})

@login_required
def save_code(request):
    if request.method == 'POST':
        try:
            # Parse incoming data
            data = json.loads(request.body)
            code = data.get('code', '')
            language = data.get('language', '')
            title = data.get('title', '')
            created_at = data.get('created_at','')
            desc = data.get('desc','')

            # Ensure data is not empty
            if not code.strip():
                return JsonResponse({'error': 'Code cannot be empty'}, status=400)

            # Save to database
            CodeSnippet.objects.create(
                user=request.user,
                code=code,
                language=language,
                desc=desc,
                title=title,
                created_at=created_at
            )

            return JsonResponse({'message': 'Code saved successfully'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
def delete_code(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code_id = data.get('id')
            
            # Get and delete the code snippet
            code_snippet = CodeSnippet.objects.get(id=code_id)
            code_snippet.delete()
            
            return JsonResponse({'status': 'success', 'message': 'Code deleted successfully'})
        except CodeSnippet.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Code not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)