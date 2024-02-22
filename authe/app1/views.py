import datetime
from django.shortcuts import render ,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . models import blood_details,hospital_details,FriendRequest, FriendList
from django.views.generic.list import ListView
import json
from .utils import get_friend_request_or_false

# Create your views here.
def FirstPage(request):
    return render(request, 'FirstPage.html')

@login_required(login_url='login')
def blood_view(request):
    all_blood=blood_details.objects.filter(hospital=request.user)
    print(all_blood)
    return render(request, 'Dashboard.html', {'all_blood': all_blood})

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
            return redirect('Firstpage')
        
    return render (request,'Signup.html')


def LoginPage(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            email_exists=hospital_details.objects.filter(hospital_id=request.user).exists()
            if email_exists:
                return redirect('Dashboard')
            else:
                return redirect('signup2')
        else:
            return HttpResponse("Your username or password is incorrect")
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def Signup2Page(request):
    if request.method == 'POST':
        org_name = request.POST.get('org_name')
        org_state = request.POST.get('org_state')
        hospital_details.objects.create(
            hospital_id=request.user,
            org_name=org_name,
            org_state=org_state
        )
    return render (request,'Signup2.html')

def Signup3Page(request):
    if request.method == 'POST':
        blood_type = request.POST.get('blood_type')
        amount = request.POST.get('amount')
        days = 5  # Assuming you calculate days elsewhere

        # Save the blood details with the current user's hospital
        blood_details.objects.create(
            hospital=request.user,
            blood_type=blood_type,
            amount=amount,
            days=days
        )
    # Filter blood details associated with the current user's hospital
    return render(request,'signup3.html')

def user_list(request):
    current_user = request.user
    user_list = User.objects.exclude(username=current_user.username)
    return render(request, 'user_list.html', {'user_list': user_list})

# def send_request(request, *args, **kwargs):
#     user=request.user
#     payload={}
#     if request.method == 'POST':
#         user_id=request.POST.get("receiver_user_id")
#         if user_id:
#             receiver=User.objects.get(pk=user_id)
#             try:
#                 friend_request=bloodrequest(sender=user,receiver=receiver)
#                 friend_request.save()
#                 # payload['result']="success"
#                 payload['response']="request sent."
#             except Exception as e:
#                 # payload['result']="error"
#                 payload['response']=str(e)
#             if payload['response']==None:
#                 payload['response']="Something went wrong."
#         else:
#             payload['response']="Unable to send friend request"
    
#     return HttpResponse(json.dumps(payload),content_type="application/json")