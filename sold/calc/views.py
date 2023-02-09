from django.shortcuts import render,redirect
from . import  views
from . models import *
from django.contrib. auth.models import User,auth
from django.contrib import messages

# Create your views here.

def home(request):
    result=[Domain.objects.all()]
    context={'res':result}
    return render(request,'home.html',context)

def feature(request):
    return render(request,'feature.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email is taken') 
                return redirect('register') 
            else:
                
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                user.save()  
                return redirect('login')            
        else:
            print('password is not matching')
            return redirect('register')    
    else:
        return render(request,'register.html')
    
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
        
    else:
       return render(request,'login.html')  