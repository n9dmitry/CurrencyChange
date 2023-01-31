from django.urls import path
from .views import product_list, actual_rates, convert_currency
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('actual_rates/', actual_rates, name='actual_rates'),
    path('convert/<str:currency>/', convert_currency, name='convert_currency'),

]

