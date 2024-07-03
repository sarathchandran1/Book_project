from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User


# Create your views here.


def reister_user(request):

    if request.method=='POST':
     
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'this mail already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
         
            return redirect('login')

        else:
            messages.info(request,'password is not match')
            return redirect('register')

    return render(request,'register.html')
    

def login_user(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'please provide correct deatiles')
            return redirect('login')

    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def home(request):
    return render(request,'home.html')






 



