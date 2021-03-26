from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        return render(request, 'portal/home.html')
    else:
        return redirect('/')


def complaint(request):
    if request.user.is_authenticated:
        return render(request, 'portal/complaint.html')
    else:
        return redirect('/')


def contact(request):
    if request.user.is_authenticated:
        return render(request, 'portal/contactUs.html')
    else:
        return redirect('/')


def about(request):
    if request.user.is_authenticated:
        return render(request, 'portal/aboutUs.html')
    else:
        return redirect('/')


def status(request):
    if request.user.is_authenticated:
        return render(request, 'portal/status.html')
    else:
        return redirect('/')
