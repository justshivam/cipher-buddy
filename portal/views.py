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
            x = Complaint(email=Email.objects.get(email=email), name=name,
                          phone=phone, subject=subject, details=details)
            x.save()
            messages.info(request, "Submitted successfully")
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
            x = SiteComplaint(email=Email.objects.get(email=email), name=name,
                              phone=phone, subject=subject, details=details, website=website)
            x.save()
            messages.info("Submitted successfully")
            return redirect('/portal/complaint')
        return render(request, 'portal/complaint.html')
    else:
        return redirect('/')


def contact(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.user.username
            time = request.POST['callTime']
            comm = request.POST['comments']
            if not Email.objects.filter(email=email).exists():
                x = Email.objects.create(email=email)
            x = Contact(email=Email.objects.get(email=email),
                        name=name, phone=phone, time=time, comments=comm)
            x.save()
            messages.info(request, 'Submitted Succesfully')
            return redirect('/portal/contact')
        return render(request, 'portal/contactUs.html')
    else:
        return redirect('/')


def about(request):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            if request.method == 'POST':
                name = request.POST['name']
                phone = request.POST['phone']
                email = request.user.username
                details = request.POST['details']
                callTime = request.POST['callTime']
                if len(phone) != 10:
                    messages.info(request, "Invalid phone number.")
                    return redirect('/portal/contact')
                if not Email.objects.filter(email=email).exists():
                    x = Email.objects.create(email=email)
                x = Contact(email=Email.objects.get(email=email), name=name,
                            phone=phone, details=details, time=callTime)
                x.save()
                messages.info(request, "Submitted successfully")
                return redirect('/portal/contact')
        return render(request, 'portal/aboutUs.html')
    else:
        return redirect('/')


def status(request):
    if request.user.is_authenticated:
        if not Email.objects.filter(email=email).exists():
            x = Email.objects.create(email=email)
        complaint = Complaint.objects.filter(
            email=Email.objects.get(email=request.user.username))
        return render(request, 'portal/status.html', {'com': complaint})
    else:
        return redirect('/')


def status_det(request, val):
    if request.user.is_authenticated:
        complaint = Complaint.objects.get(id=val)
        if not complaint.email.email == request.user.username:
            messages.info(request, 'Access Denied.')
            return redirect('/portal/status')
        return render(request, 'portal/status_det.html', {'com': complaint})
    else:
        return redirect('/')
