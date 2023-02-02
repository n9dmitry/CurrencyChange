from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import django.contrib.auth.views as auth_views
# Create your views here.

def login(request):
    if request.method == 'POST':
        # Запрашиваем имя пользователя и пароль из HTML-формы
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверяем правильность имени пользователя и пароля
        user = authenticate(username=username, password=password)
        if user is not None:
            # Аутентификация прошла успешно
            login(request, user)
            # Перенаправляем пользователя на главную страницу
            return redirect('index')
        else:
            # Аутентификация не удалась
            return redirect('login')