from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    text1 = 'Игры'
    text2 = 'Извините ваша корзина пуста'
    context = {
        'text1': text1,
        'text2': text2,
    }
    return render(request, 'third_task/platform.html', context)

def index2(request):
    text3 = 'Игры'
    context = {
        'text3': text3,
    }
    return render(request, 'third_task/gemes.html', context)

def index3(request):
    text4 = 'Корзина'
    context = {
        'text4': text4,
    }
    return render(request, 'third_task/cart.html', context)
