from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db import models
class User(AbstractUser):
    username=None
    full_name=models.CharField( max_length=50,null=True,blank=True)
    email=models.EmailField( max_length=254,unique=True)
    Mobile_number=models.CharField( max_length=50,null=True,blank=True)
    Phone_code=models.CharField( max_length=50,null=True,blank=True)
    password=models.CharField( max_length=500,null=True,blank=True)
    confirm_password=models.CharField( max_length=50,null=True,blank=True)
    Country=models.CharField( max_length=50,null=True,blank=True)
    State=models.CharField( max_length=50,null=True,blank=True)
    forget_password_token = models.CharField(max_length=100,null=True)
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]





    
