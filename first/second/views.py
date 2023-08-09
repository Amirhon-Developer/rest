from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "second/index.html")


def about(request):
    return HttpResponse(
        "<h1>Хусяенов Амирхан </h1> </br> <h2>мне 17 лет я дабию своих успехов и буду зарабатывать "
        "и стану самым лучшим програмистом в мире !!!</h1>")


def phone_number(request):
    return HttpResponse(" <h1>Мой номер телефона 998(97) 750-71-03</h1> ")


def leave(request):
    return HttpResponse(" <h1> Я живу на кукчу очень бол</h1>")

