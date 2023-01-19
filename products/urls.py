from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.store_view, name='products'),
]

