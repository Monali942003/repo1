from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .models import Signup
from .models import Registration
from .models import Donation
from .models import Record
from .models import Contact
from .models import Report

# Create your views here.
def display(request):
    return render(request,'login form.html')


def login(request):
    if request.method=='POST':
      email=request.POST.get('email')
      password=request.POST.get('password')
      z=Login(email=email,password=password)
      z.save()
      return HttpResponse("Data successfully enterd")
    else:
      return HttpResponse("invalid request")
    
def clear(request):
    return render(request,'login form.html')
def dosign(request):
    if request.method=='POST':
      email=request.POST.get('email')
      password=request.POST.get('password')
      password2=request.POST.get('password2')
      z=Signup(email=email,password=password,password2=password2)
      z.save()
      return HttpResponse("sigh-up successfully.")
    else:
      return HttpResponse("invalid request")
    

def show(request):
    return render(request,'register.html')

def register(request):
   if request.method=='POST':
      email=request.POST.get('email')
      password=request.POST.get('password')
      password2=request.POST.get('password2')
      firstname=request.POST.get('firstname')
      lastname=request.POST.get('lastname')
      Applicationdate=request.POST.get('Applicationdate')
      area=request.POST.get('area')
      city=request.POST.get('city')
      postalcode=request.POST.get('postalcode')
      state=request.POST.get('state')
      anum=request.POST.get('anum')
      vid=request.POST.get('vid')
      schemes=request.POST.get('schemes')
      gender=request.POST.get('gender')
      cb1=request.POST.get('cb1')
      cb2=request.POST.get('cb2')
      z=Registration(email=email,password=password,password2=password2,firstname=firstname,lastname=lastname,Applicationdate=Applicationdate,area=area,city=city,postalcode=postalcode,state=state,anum=anum,vid=vid,schemes=schemes,gender=gender,cb1=cb1,cb2=cb2)
      z.save()
      return HttpResponse("registration successfully")
   else:
       return HttpResponse("invalid request")
    

def new(request):
    return render(request,'Donation.html')


def dodonate(request):
    if request.method=='POST':
      name=request.POST.get('name')
      email=request.POST.get('email')
      amount=request.POST.get('amount')
      paymentmethod=request.POST.get('paymentmethod')
      z=Donation(name=name,email=email,amount=amount,paymentmethod=paymentmethod)
      z.save()
      return HttpResponse("Thank you ")
    else:
      return HttpResponse("invalid request")
    

def start(request):
    return render(request,'index.html')

def cause(request):
    return render(request,'causes.html')

def mission(request):
    return render(request,'mission.html')

def rules(request):
    return render(request,'rules.html')

def gallary(request):
    return render(request,'gallary.html')

def wel(request):
    return render(request,'user.html')

def hellow(request):
        return render(request,'schemes-user.html')

def wildlife(request):
        return render(request,'wildlife.html')

def app2(request):
         return render(request,'accidental record 2.html')


def app3(request):
    return render(request,'Ai.html')

def app4(request):
    return render(request,'table.html')


def dorecord(request):
    if request.method=='POST':
     fullname=request.POST.get('fullname')
     email=request.POST.get('email')
     vnum=request.POST.get('vnum')
     vname=request.POST.get('vname')
     date=request.POST.get('date')
     area=request.POST.get('area')
     AccidentType=request.POST.get('AccidentType')
     typeofwhether=request.POST.get('typeofwhether')
     typeofcollision=request.POST.get('typeofcollision')
     rname=request.POST.get('rname')
     rnumber=request.POST.get('rnumber')
     roadtype=request.POST.get('roadtype')
     SpeedLimit=request.POST.get('SpeedLimit')
     RoadFeatures=request.POST.get('RoadFeatures')
     physicaldivider=request.POST.get(' physicaldivider')  
     z=Record(fullname=fullname,email=email,vnum=vnum,vname=vname,date=date,area=area,AccidentType=AccidentType,typeofwhether=typeofwhether,typeofcollision=typeofcollision,rname=rname,rnumber=rnumber,roadtype=roadtype,SpeedLimit=SpeedLimit,RoadFeatures=RoadFeatures,physicaldivider=physicaldivider)
     z.save()
     return HttpResponse("Recorded Successfully ")
    else:
       return HttpResponse("invalid request")
    

def ctcn(request):
        return render(request,'index.html')


def docontact(request):
    if request.method=='POST':
     fullname=request.POST.get('fullname')
     email=request.POST.get('email')
     msg=request.POST.get('msg')       
     z=Contact(fullname=fullname,email=email,msg=msg)
     z.save()
     return HttpResponse("message recorded successfully")
    else:
      return HttpResponse("invalid request")
    

def app5(request):
    return render(request,'Accidents report.html')


def doreport(request):
    if request.method=='POST':
      name=request.POST.get('name')
      email=request.POST.get('email')
      phone=request.POST.get('phone')
      age=request.POST.get('age')
      area=request.POST.get('area')
      gender=request.POST.get('gender')
      date=request.POST.get('date')
      description=request.POST.get('description')
      z=Report(name=name,email=email,phone=phone,age=age,area=area,gender=gender,date=date,description=description)
      z.save()
      return HttpResponse("report recorded successfeully ")
    else:
      return HttpResponse("invalid request")
        
    


     


        