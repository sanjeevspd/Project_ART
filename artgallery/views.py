from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from adminapp.models import Admin
from django.db.models import Q


def homefunction(request):
    return render(request, "customerapp/index.html")


def aboutfunction(request):
    return render(request, "customerapp/about.html")

def loginfunction(request):
    return render(request, "login.html")
def aboutfunction(request):
    return render(request, "customerapp/about.html")

def homefunction(request):
    return render(request, "customerapp/home.html")

def loginPage(request):
    return render(request,'login.html')

def signupfunction(request):
    if request.method=='POST':
        adminuname=request.POST.get('user')
        adminemail=request.POST.get('email')
        adminpwd=request.POST.get('pass1')
        adminpwd2=request.POST.get('pass2')
        print(adminuname,adminemail,adminpwd,adminpwd2)
        if adminpwd!=adminpwd2:
            message1="Passwords don't match!!"
            return render(request,'signup.html',{"msg1":message1})
        elif len(adminpwd)<8:
            message2="Length of the password must be more than 8 characters!!"
            return render(request,'signup.html',{"msg2":message2})
        check=User.objects.create_user(adminuname,adminemail,adminpwd)
        check.save()
        msg="Account sucessfully created!!"
        return render(request,'signup.html',{"message":msg})
    return render(request,'signup.html')

def checkuserlogin(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        user1=(username,password)
        print(user1)
        n=username
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'customerapp/greeting.html',{"name":n})
        else:
            adminuname=request.POST["uname"]
            adminpwd=request.POST["pwd"]
            flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
            print(flag)
            if flag:
                name=adminuname
                return render(request,'adminapp/adminhome.html',{"n":name})
            else:
                message="Invalid Credentials!!"
                return render(request,"login.html",{"msg":message})
    return render(request,"login.html")
'''
def checkadminlogin(request):
    adminuname=request.POST["uname"]
    adminpwd=request.POST["pwd"]
    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)
    if flag:
        return render(request,'adminhome.html')
    else:
        message="Invalid Credentials!!"
        return render(request,"login.html",{"msg":message})

'''
def userlogout(request):
    return render(request,"login.html")
def userabout(request):
    return render(request, "customerapp/userabout.html")
def home1(request):
    return render(request, "customerapp/home1.html")
def pd1(request):
    return render(request, "customerapp/pd1.html")
def decontact(request):
    return render(request,"customerapp/decontact.html")
