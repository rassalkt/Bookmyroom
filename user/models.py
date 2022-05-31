from django.db import models

# Create your models here.



class UserSignUp(models.Model):
    email=models.CharField(max_length=30)
    passw=models.CharField(max_length=20)
    reppass=models.CharField(max_length=20)