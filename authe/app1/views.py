import datetime
from django.shortcuts import render ,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . models import blood_details
from django.views.generic.list import ListView
# Create your views here.
def FirstPage(request):
    return render(request, 'FirstPage.html')

@login_required(login_url='login')
def DashboardPage(request):
    return render(request, 'Dashboard.html')

def SignupPage(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password != cpassword:
            return HttpResponse("password and confirm password must be same")
        else:
            my_user=User.objects.create_user(email,email,password)
            my_user.save()
            return redirect('signup3')
        
    return render (request,'Signup.html')

def LoginPage(request):
    return render (request,'login.html')

def LoginPage(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('signup3')
        else:
            return HttpResponse("Your username or password is incorrect")
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def Signup3Page(request):
    if request.method == 'POST':
        blood_type=request.POST.get('blood_type')
        amount=request.POST.get('amount')
        # days=datetime.datetime.now()-request.POST.get('dod')
        days=5
        b_details=blood_details(blood_type=blood_type,amount=amount,days=days)
        b_details.save()
    from django.core import serializers
    data=serializers.serialize("python",blood_details.objects.all())

    context={
        'data': data,
    }
    return render(request,'signup3.html',context)


    