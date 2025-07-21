from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')

        pwd = request.POST.get('password')
        pwd_reentered = request.POST.get('password_reentered')

        if pwd != pwd_reentered:
            messages.error(request, 'Passwords do not match!')
        elif User.objects.filter(username=username).exists():
            messages.error(request, f'user with {username} already exist, Please choose another one.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, f'{email} already registered, please log in instead')
        else:
            user = User.objects.create_user(username=username, email=email, password=pwd)
            user.save()

            login(request, user)
            messages.success(request, f'Registration successful. Welcome, {username}!')
            return redirect('home')
    
    return render(request, 'accounts/register.html')

def cj_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome again, {username}')
                return redirect('home')
            else:
                messages.error(request, 'Wrong password')
        else:
            messages.warning(request, 'User doesnot exist. Please register!')
    return render(request, 'accounts/login.html')

def cj_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'accounts/home.html')