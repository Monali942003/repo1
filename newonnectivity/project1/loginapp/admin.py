from django.contrib import admin
from .models import *
# Register your models here.
class LoginAdmin(admin.ModelAdmin):
  list_display=['email','password']


admin.site.register(Login,LoginAdmin)


class SignupAdmin(admin.ModelAdmin):
  list_display=['email','password','password2']


admin.site.register(Signup,SignupAdmin)


class RegistrationAdmin(admin.ModelAdmin):
  list_display=['email','password','password2','firstname','lastname','Applicationdate','area','postalcode','state','city','anum','vid','schemes','cb1','cb2','gender']


admin.site.register(Registration,RegistrationAdmin)

class DonationAdmin(admin.ModelAdmin):
  list_display=['name','email','amount','paymentmethod']


admin.site.register(Donation,DonationAdmin)


class RecordAdmin(admin.ModelAdmin):
  list_display=['fullname','email','vnum','vname','date','area','AccidentType','typeofwhether','typeofcollision','rname','rnumber','roadtype','SpeedLimit','RoadFeatures','physicaldivider']


admin.site.register(Record,RecordAdmin)

class ContactAdmin(admin.ModelAdmin):
  list_display=['fullname','email','msg']


admin.site.register(Contact,ContactAdmin)


class ReportAdmin(admin.ModelAdmin):
  list_display=['name','email','phone','age','area','gender','date','description']


admin.site.register(Report,ReportAdmin)
