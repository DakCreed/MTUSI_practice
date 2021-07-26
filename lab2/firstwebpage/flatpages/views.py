from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django import template



# Create your views here.
def home(request):
    return render(request, 'templates/index.html')

def hello(request):
    return HttpResponse(u'Hellow World! from hello', content_type="text/plain")
    
def static_handler(request):
    return render(request, 'templates/static_handler.html')