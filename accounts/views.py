from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from blog.city import cities


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                raise ValidationError('User %s already exists' % username)
            elif User.objects.filter(email=email).exists():
                print('User email already exists')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name)
                user.save()
                user = auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                print('User login successful')
                return redirect('/')
        else:
            print('Password is incorrect')
        return redirect('register')
    return render(request, 'register.html', {'cities': cities})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            print('Wrong username or password')
            return redirect('login')
    return render(request, 'login.html', {'cities': cities})


def logout(request):
    auth.logout(request)
    return redirect('home')