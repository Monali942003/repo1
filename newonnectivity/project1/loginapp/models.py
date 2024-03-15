from django.db import models
from .models import*
# Create your models here.
class Login(models.Model):
    email=models.CharField(max_length=25,null=True)
    password=models.CharField(max_length=6)


class Signup(models.Model):
    email=models.CharField(max_length=25,null=True)
    password=models.CharField(max_length=6,null=True)
    password2=models.CharField(max_length=6,null=True)

class Registration(models.Model):
    email=models.CharField(max_length=22,null=True) 
    password=models.CharField(max_length=22)
    password2=models.CharField(max_length=12,null=True)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    Applicationdate=models.CharField(max_length=6,null=True)
    area=models.CharField(max_length=10)
    city=models.CharField(max_length=10,null=True)
    postalcode=models.CharField(max_length=6,null=True)
    state=models.CharField(max_length=25,)
    anum=models.IntegerField()
    vid=models.CharField(max_length=25,)
    schemes=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length = 6,default =True)
    cb1=models.BooleanField(null=True)
    cb2=models.BooleanField(null=True)

class Donation(models.Model):
    name=models.CharField(max_length=25,)
    email=models.CharField(max_length=6,null=True)
    amount=models.IntegerField()
    paymentmethod=models.CharField(max_length=10)

class Record(models.Model):
    fullname=models.CharField(max_length=25,null=True)
    email=models.CharField(max_length=6,null=True)
    vnum=models.IntegerField()
    vname=models.CharField(max_length=10,null=True)
    date=models.CharField(max_length=6,null=True)
    area=models.CharField(max_length=8,null=True)
    AccidentType=models.CharField(max_length=34,null=True)
    typeofwhether=models.CharField(max_length=8,null=True)
    typeofcollision=models.CharField(max_length=34,null=True)
    rname=models.CharField(max_length=23,null=True)
    rnumber=models.CharField(max_length=12,null=True)
    roadtype=models.CharField(max_length=4,null=True)
    SpeedLimit=models.CharField(max_length=4,null=True)
    RoadFeatures=models.CharField(max_length=4,null=True)
    physicaldivider=models.CharField(max_length=4,null=True)

class Report(models.Model):
    name=models.CharField(max_length=25,null=True)
    email=models.CharField(max_length=6,null=True)
    phone=models.CharField(max_length=14,null=True)
    age=models.CharField(max_length=10,null=True)
    area=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=10,null=True)
    date=models.CharField(max_length=6,null=True)
    description=models.CharField(max_length=34,null=True)
    
    
class Contact(models.Model):
    fullname=models.CharField(max_length=25,null=True)
    email=models.CharField(max_length=11,null=True)
    msg=models.CharField(max_length=60,null=True)
