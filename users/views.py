from urllib import request
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Перенаправляем пользователя на главную страницу
            return redirect('index')
        else:
            # Аутентификация не удалась
            print('аутентификация не удалась')
            return redirect('login')
    else:
        return render(request, 'users/login.html', )

# def LogoutUser(request):
#     logout(request)
#     # redirect to a success page
#     return render(request, 'login.html')


# / вот выше нихуя не получается