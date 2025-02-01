from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json
import requests

def index(request):
    return render(request, 'editor/index.html')

@csrf_protect
def run_code(request):
    if request.method == 'POST':
        try:
            # Parse incoming data
            data = json.loads(request.body)
            code = data.get('code', '')

            # Compiler API configuration
            url = "https://code-compiler.p.rapidapi.com/v2"
            
            payload = {
                "LanguageChoice": "5",  # Python
                "Program": code  # Use the actual code from the editor
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
