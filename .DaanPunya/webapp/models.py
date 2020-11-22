from django.db import models
import datetime
from django.conf import settings

# Create your models here.
class  medicine(models.Model):
    id=models.AutoField
    user_email=models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    MedName=models.CharField(max_length=30)
    MedExpiry=models.CharField(max_length=20,default="")
    MedQuantity=models.IntegerField(default=0)
    MedFor=models.CharField(max_length=10,default="")
    MedReason=models.CharField(max_length=100,default="",blank=True)
    MedPresc=models.ImageField(upload_to="webapp/images",default="",blank=True)
    MedPic=models.ImageField(upload_to="webapp/images",default="")
    MedPic2=models.ImageField(upload_to="webapp/images",default="",blank=True)
    MedAddress=models.CharField(max_length=50,default="",blank=True)
    MedZip=models.CharField(default="0",max_length=6)
    MedDate=models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.MedName
