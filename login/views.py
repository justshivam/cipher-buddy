from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/portal/home')
        else:
            messages.info(request, 'Invalid credentials.')
            return redirect('/')
    else:
        return render(request, 'login/login.html')


def createUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_c = request.POST['password_repeat']

        if password == password_c:
            if User.objects.filter(email=email).exists():
                messages.info(request, "User already exists.")
                return redirect('/')
            user = User.objects.create_user(
                email=email, password=password, first_name=first_name, last_name=last_name, username=email)
            user.save()
            print("user created")
            messages.info(request, 'User created succesfully.')
            return redirect('/')

        else:
            print('here')
            messages.info(request, 'Passwords don\'t match')
            return redirect('/register')
    else:
        print('not here')
        return render(request, 'login/createUser.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, "Logged out Sucessfully")
        return redirect('/logout')
    return redirect('/')
