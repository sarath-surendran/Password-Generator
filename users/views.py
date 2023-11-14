from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
@login_required(login_url='login')
def home(request):
    user = request.user
    password = ''

    if request.method == 'POST':
        length = int(request.POST.get('length'))
        specialChars = request.POST.get('specialChars')
        lowercase = request.POST.get('lowercase')
        uppercase = request.POST.get('uppercase')
        numbers = request.POST.get('numbers')
        
        password_characters = []
        if lowercase:
            password_characters.extend("abcdefghijklmnopqrstuvwxyz")
        if uppercase:
            password_characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if specialChars:
            password_characters.extend('!@#$%^&*()<>?/.,')
        if numbers:
            password_characters.extend('1234567890')

        for i in range(length):
            password += random.choice(password_characters)
        
        

    context = {
        'user': user,
        'password':password,
    }
    return render(request, 'home.html', context)

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request,user)
            print('success')
            return redirect('home')
        else:
            messages.error(request, 'Please verify the credentials.')
            return render(request, 'login.html')
            # return redirect('login')
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # messages.error(request, "Passwords do not match.")
        # return render(request, 'register.html')
        try:
            if password == confirm_password and password and name and email:
                user = MyUser.objects.create(
                    name=name,
                    email=email,
                )
                user.set_password(password)
                user.save()
                    
                messages.success(request,"User registerd successfully.")
                return redirect('login')
            
            else:
                messages.error(request, "Passwords do not match")
                return render(request, 'register.html')
        except Exception as e:
            messages.error(request, "Some error happend")
            print(e)
            return render(request, 'register.html')
    
    return render(request, 'register.html')