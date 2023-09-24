from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def signup_Page(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse('<h1 style="color:red;">Please...Check Your Passwords....</h1>')
        else:
            my_user = User.objects.create_user(name, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')

def login_Page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        my_user = authenticate(request, username = username, password = pass1)
        if my_user is not None:
            login(request, my_user)
            return redirect('home')
        else:
            return HttpResponse('<h1 style="color:red;">Please Check Your Credentials...</h1>')
    return render(request, 'login.html')

def home_Page(request):
    return render(request, 'home.html')