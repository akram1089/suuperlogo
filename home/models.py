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







class ChartData(models.Model):
    data_json = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)



class Top_Gainer(models.Model):
 top_gainers = models.TextField()

class Top_Loser(models.Model):
 top_losers = models.TextField()



