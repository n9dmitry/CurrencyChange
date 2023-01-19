from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

def store_view(request):
    return render(request, 'products/index.html')

def index(request):
    return render(request, 'base.html')


