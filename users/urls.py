from django.urls import path
from users.views import LoginUser
from .views import register

app_name = 'users'

urlpatterns = [
    path('login/', LoginUser, name='login'),
    path('registration/', register, name='registration'),

]
