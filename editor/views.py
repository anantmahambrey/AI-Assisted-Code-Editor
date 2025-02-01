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
        data = json.loads(request.body)
        code = data.get('code', '')
        # Compiler API


        # You can add code execution logic here later
        return JsonResponse({'output': code})
