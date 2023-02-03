from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
import requests
from .models import Product
from .models import Currency
from django.contrib import messages
import sqlite3

def store_view(request):
    return render(request, 'products/base.html')

def index(request):
    return render(request, 'products/index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})


# def update_currency(request):
#     if request.method == 'POST':
#         api_key = '0b3a0600039b4a438508b98feb11b8a7'
#         url = 'https://openexchangerates.org/api/latest.json?app_id=' + api_key
#         response = requests.get(url)
#         data = response.json()
#         rates = data['rates']
#         # сохраняем "рейтс" в базу
#         for name, rate in rates.items():
#             obj, created = Currency.objects.update_or_create(
#                 name=name,
#                 defaults={'rate': rate}
#                 )
#         messages.success(request, 'Курсы валют обновлены!')

def actual_rates(request):
    api_key = '0b3a0600039b4a438508b98feb11b8a7'
    url = 'https://openexchangerates.org/api/latest.json?app_id=' + api_key
    response = requests.get(url)
    api_data = response.json()
    for name, rate in api_data['rates'].items():
        Currency.objects.update_or_create(name=name, defaults={'rate': rate})
    return JsonResponse(api_data)

def convert_currency(request, currency):
    print(f'{currency=}')
    products = Product.objects.all()
    rate = Currency.objects.get(name=currency).rate
    base_rate = Currency.objects.get(name='RUB').rate
    for product in products:
        product.price = float(product.price) / float(base_rate) * float(rate)
    return HttpResponse(' jj oijq')

