from django.shortcuts import render


def home(request):
    return render(request, 'portal/home.html')


def complaint(request):
    return render(request, 'portal/complaint.html')


def contact(request):
    return render(request, 'portal/contactUs.html')


def about(request):
    return render(request, 'portal/aboutUs.html')


def status(request):
    return render(request, 'portal/status.html')
