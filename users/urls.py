from django.template.defaulttags import url
from django.urls import path
from users import views

urlpatterns = [
    path('', view.register, name='register'),
]