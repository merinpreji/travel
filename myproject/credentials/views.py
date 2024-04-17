from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpass = request.POST['confirmpass']

        if password == confirmpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email exists")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                print("User created")
                return redirect('login')
        else:
            messages.info(request,"Passwords not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
