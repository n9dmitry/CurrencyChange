from django.urls import path
from users.views import LoginUser, LogoutUser
from .views import register

app_name = 'users'

urlpatterns = [
    path('login/', LoginUser, name='login'),
    path('logout/', LogoutUser, name='logout'),
    path('registration/', register, name='registration'),

]
