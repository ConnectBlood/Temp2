from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User

# Create your models here.
# class User(AbstractUser):
#     pass

class details(models.Model):
    organization_name = models.CharField(max_length=100)
    oraganization_contact = models.IntegerField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class blood_details(models.Model):
    
    blood_type = models.CharField(max_length=128)
    amount=models.IntegerField()
    days=models.IntegerField()
    # users=models.ManyToManyField(User,related_name='blood') # user.blood.all()
    def __str__(self):
        return self.blood_type