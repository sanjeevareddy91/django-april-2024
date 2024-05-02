from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teams(models.Model):
    f_name = models.CharField(max_length=30)
    f_nickname = models.CharField(max_length=4)
    f_started_year = models.IntegerField()
    f_trophies = models.IntegerField()
    f_logo = models.FileField(upload_to='logos/',blank=True,null=True)


    def __str__(self):
        return self.f_name
    
class User_Details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10) # 2147483647
    otp = models.IntegerField()
    
    def __str__(self):
        return self.user.username