from django.db import models
import datetime
from django.conf import settings
from django.utils.timezone import now
# from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model as User

# Create your models here.

class extUser(AbstractUser):
    is_org = models.BooleanField(default=False)
    reg_num = models.CharField(max_length=20,blank=True)
    cert_num = models.CharField(max_length=20,blank=True)
    phNum = models.IntegerField(default=0,blank=True)
    address = models.CharField(max_length=200,default="",blank=True)


class  medicine(models.Model):
    id=models.AutoField
    user_email=models.ForeignKey(User(), default=1, on_delete=models.CASCADE)
    update=models.BooleanField(default=None,null=True)
    MedName=models.CharField(max_length=30)
    MedExpiry=models.CharField(max_length=20,default="")
    MedQuantity=models.IntegerField(default=0)
    MedFor=models.CharField(max_length=10,default="")
    MedReason=models.CharField(max_length=100,default="",blank=True)
    MedPresc=models.ImageField(upload_to="images/",default="",blank=True)
    MedPic=models.ImageField(upload_to="images/",default="")
    MedPic2=models.ImageField(upload_to="images/",default="",blank=True)
    MedAddress=models.CharField(max_length=50,default="",blank=True)
    MedZip=models.CharField(default="0",max_length=6,blank=True)
    MedDate=models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.MedName

state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))

class dnr_address(models.Model):
    med = models.ForeignKey(medicine, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User(), on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length = 300,null=True)
    zipcode = models.IntegerField(null=True)
    city = models.CharField(max_length=20,null=True)
    state = models.CharField(choices=state_choices,max_length=255,null=True)

    def __str__(self):
       return self.med.MedName +'-->'+ self.user.email



class rq_medicine(models.Model):
    id=models.AutoField(primary_key = True)
    user_email=models.ForeignKey(User(), default=1, on_delete=models.CASCADE)
    update=models.BooleanField(default=False)
    MedName=models.CharField(max_length=30)
    MedQuantity=models.IntegerField()
    MedFor=models.CharField(max_length=10)
    MedReason=models.CharField(max_length=100)
    MedPresc=models.ImageField(upload_to="webapp/images")
    MedDate=models.DateField(default=now)

    def __str__(self):
        return self.MedName

del_choice = {

    ('Not Selected',None),
    ('org_pick','pickup by org'),
    ('courier','courier')
}

class applied_medicine(models.Model):
    med = models.ForeignKey(medicine, on_delete=models.CASCADE)
    user= models.ForeignKey(User(), on_delete=models.CASCADE)
    date= models.DateField(default=now)


    def __str__(self):
        return self.med.MedName

class org_update(models.Model):
    user = models.ForeignKey(User(), on_delete=models.CASCADE)
    rq_med = models.ForeignKey(rq_medicine, on_delete=models.CASCADE)
    rqst_med = models.BooleanField(default=False)
    mode_del = models.CharField(max_length=50 ,choices=del_choice)
    frm_date = models.DateField(default=None,null=True)
    to_date = models.DateField(default=None,null=True)
    med_rcvd = models.BooleanField(default=False)

    def __str__(self):
        return self.rq_med.MedName

class dnr_update(models.Model):
    med = models.ForeignKey(medicine, on_delete=models.CASCADE)
    user = models.ForeignKey(User(), on_delete=models.CASCADE)
    donor_address = models.ForeignKey(dnr_address,on_delete=models.CASCADE,null=True)
    mode_del = models.CharField(default=None,max_length=30,choices=del_choice,null=True)
    frm_date = models.DateField(default=None,null=True)
    to_date = models.DateField(default=None,null=True)
    select_date = models.DateField(default=None,null=True)
    rqst_user_email = models.CharField(default=None,null=True,max_length=50)
    med_dispatched = models.BooleanField(default=False)

    def __str__(self):
        return self.med.MedName
        

class reg_org(models.Model):
    name = models.CharField(max_length = 50)
    reg_num = models.IntegerField()
    cert_num = models.CharField(max_length =20)
    contact_num = models.BigIntegerField()
    address = models.CharField(max_length = 200,blank=True)
    email = models.CharField(max_length = 50,blank=True)

    def __str__(self):
        return self.name



# update

# ORG
# requested for medicine
# accepted request of medicine----
# select mode of delivery 
# range of date field  
# medicine receive


# DONOR
# medicine uploaded for donation
# accept request of medicine from org
# details of org will be shown---
# donor will be notified of delivery mode
# Select date from range provided by org
# Medicine dispatched
