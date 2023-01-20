from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import requests
from .models import Product

def store_view(request):
    return render(request, 'products/base.html')

def index(request):
    return render(request, 'products/index.html')


api_key = '0b3a0600039b4a438508b98feb11b8a7'
def get_currency_rate(api_key, currency_code):
    url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(currency_code)


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})