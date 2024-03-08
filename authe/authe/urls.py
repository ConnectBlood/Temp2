"""
URL configuration for authe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.FirstPage,name='Firstpage'),
    path('signup/',views.SignupPage,name='Signup'),
    path('login/',views.LoginPage,name='login'),
    path('Dashboard/',views.blood_view,name='Dashboard'),
    path('signup3/',views.Signup3Page,name='signup3'),
    path('signup2/',views.Signup2Page,name='signup2'),
    path('logout/', views.LogoutPage, name='logout'),
    path('userlist/',views.user_list,name='userlist'),
    path('updatedetails/',views.update_blood_details,name='Updatedetails'),
    path('add/',views.AddBlood,name='AddBlood'),
    path('edit/',views.Edit,name='edit'),
    path('update/',views.Update,name='update')
    # path('sendrequest/',views.send_request,name='sendrequest'),
]
