from django.urls import path
from users.views import login

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
]
