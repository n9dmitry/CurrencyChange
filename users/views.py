from django.shortcuts import render

# Create your views here.

def registration(request):
    context = {
        'text': 'Регистрация'
    }
    return render(request, 'registration.html', context)