from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Admin,Photo
from customerapp .models import Feedback


@login_required(login_url='login')
def adminhome(request):
    return render(request,"adminapp/adminhome.html")

def upload_photo(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        Photo.objects.create(title=title, image=image)
        return redirect('static/images')

    return render(request, 'adminapp/uploadopt.html')

def logout(request):
    return render(request,"login.html")

def feedbackpage(request):
    data=Feedback.objects.all()
    return render(request,'adminapp/feedbacks.html',{'data':data})



