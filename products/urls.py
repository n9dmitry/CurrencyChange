from django.urls import path
from .views import product_list
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
#    path('', views.index, name='products'),
    path('', product_list, name='product_list'),
]

