from django.shortcuts import render


def login(request):
    return render(request, 'login/login.html')


def createUser(request):
    return render(request, 'login/createUser.html')
