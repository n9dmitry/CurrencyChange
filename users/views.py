from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'users/login.html',)
    # if request.method != 'POST':
    #     # Запрашиваем имя пользователя и пароль из HTML-формы
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #
    #     # Проверяем правильность имени пользователя и пароля
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         # Аутентификация прошла успешно
    #         login(request, user)
    #         # Перенаправляем пользователя на главную страницу
    #         return redirect('index')
    #     else:
    #         # Аутентификация не удалась
    #         return redirect('login')