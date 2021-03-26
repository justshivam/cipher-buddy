from portal.models import Complaint, Email
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.user.username
            subject = request.POST['subject']
            details = request.POST['details']
            if len(phone) != 10:
                messages.info(request, "Invalid phone number.")
                return redirect('/portal/home')
            if not Email.objects.filter(email=email).exists():
                x = Email.objects.create(email=email)
            x = Complaint(Email.objects.get(email=email), name=name,
                          phone=phone, subject=subject, details=details)
            x.save()
            messages.info("Submitted successfully")
            return redirect('/portal/home')
        return render(request, 'portal/home.html')
    else:
        return redirect('/')


def complaint(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.user.username
            subject = request.POST['subject']
            details = request.POST['details']
            website = request.POST['site']
            if len(phone) != 10:
                messages.info(request, "Invalid phone number.")
                return redirect('/portal/complaint')
            if not Email.objects.filter(email=email).exists():
                x = Email.objects.create(email=email)
            x = SiteComplaint(Email.objects.get(email=email), name=name,
                              phone=phone, subject=subject, details=details, website=website)
            x.save()
            messages.info("Submitted successfully")
            return redirect('/portal/complaint')
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
