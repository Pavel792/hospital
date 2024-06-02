from django.shortcuts import render

# Create your views here.


def prime(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/prime.html', data)


def info(request):
    data = {
        'title': 'Информация'
    }
    return render(request, 'main/info.html', data)
