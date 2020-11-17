from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import medicine
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as user_login ,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from django.core.mail import send_mail 
import random

fname=''
lname=''
email=''
password=''
username=''
gen_otp=0

def index(request):
    return render(request,'webapp/index.html')

def login(request):
    return render(request,'webapp/login.html')

def register(request):
    return render(request,'webapp/register.html')

def handleRegister(request):
    if request.method == 'POST':
        #Extracting POST parameters
        global username
        global fname
        global lname
        global password
        global email
        fname=request.POST['Fname']
        lname=request.POST['Lname']
        email=request.POST['email']
        password=request.POST['password']
        # username=fname+lname+'-'+email
        username=email
        global gen_otp
        gen_otp= str(random.randint(1000,9999))
        subject = 'Danpunya'
        message = f'Hi {fname}, your OTP to register in Daanpunya is {gen_otp}'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email, ] 
        send_mail( subject, message, email_from, recipient_list ) 
        return render(request, 'webapp/checkOtp.html')
    else:
        return render(request, 'webapp/register.html')

def handleOtp(request):
    if request.method == 'POST':
        otp=request.POST['otp']
        global gen_otp
        global username
        global fname
        global lname
        global password
        global email
        print(gen_otp)
        if otp == gen_otp:
            MyUser =User.objects.create_user(username,email=email,password=password)
            MyUser.first_name=fname
            MyUser.last_name=lname
            MyUser.save()
            messages.success(request,"Your DaanPunya account has been successfully created")
            return render(request, 'webapp/login.html')
        else:
            messages.error(request,"Your OTP didn't matched , PLease Try Again","danger")
            return redirect('home')
    else:
        return render(request, 'webapp/register.html')

def handleLogin(request):
    if request.method == 'POST':
        loginEmail = request.POST['loginEmail']
        loginPassword = request.POST['loginPassword']
        user = authenticate(username=loginEmail,password=loginPassword)
        if user is not None:
            user_login(request,user)
            messages.success(request,"Successfully LOGGED IN")
            if request.POST.get('next'):
                return redirect(request.POST['next'])
            return redirect('home')
        else:
            messages.error(request,"Wrong credentials provoided","danger")
            return redirect('home')
    else:
        HttpResponse("404-Not Found")

def handleLogout(request):
    logout(request) 
    messages.success(request,"Successfully LOGGED OUT","warning")
    return redirect('home')

def about(request): 
    return render(request, 'webapp/about.html')

def contact(request):
    return render(request, 'webapp/contact.html')

@login_required(login_url='/login/')
def medView(request,id):
    displayMed = medicine.objects.filter(id=id)
    return render(request, 'webapp/medView.html',{'med': displayMed[0]})

@login_required(login_url='/login/')
def searchResult(request):
    flag=1
    # This variable flag is used to fix repeating similar meds issue
    if request.GET['searchMed'] == "all":
        meds = medicine.objects.all()
        similar_meds=None
    else:
        searchMed = request.GET['searchMed']
        meds = medicine.objects.filter(MedName__iexact = searchMed)
        similar_meds = medicine.objects.filter(MedName__icontains = searchMed).exclude(MedName__iexact = searchMed)
        if meds and similar_meds :
            flag=None
    params={ 'meds': meds, 'similar_meds':similar_meds, 'flag': flag }
    return render(request, 'webapp/searchResult.html',params)

def status(request):
    return render(request, 'webapp/status.html')


@login_required(login_url='/login/')
def donateMed(request):
    if request.method == "POST":
        user_email = request.user
        MedName=request.POST['MedName']
        MedExpiry=request.POST['MedExpiry']
        MedQuantity=request.POST['MedQuantity']
        MedFor=request.POST['MedFor']
        MedReason=request.POST['MedReason']
        MedPresc=request.POST['MedPresc']
        MedPic=request.POST['MedPic']
        MedPic2=request.POST['MedPic2']
        MedAddress=request.POST['MedAddress']
        MedZip=request.POST['MedZip']
        # MedDate=request.POST['MedDate']
        # print(MedName,MedExpiry,MedQuantity,MedFor,MedReason,MedPresc,MedPic,MedAddress,MedZip,MedDate)
        ins = medicine(user_email=user_email,MedName=MedName,MedExpiry=MedExpiry,MedQuantity=MedQuantity,MedFor=MedFor,
                       MedReason=MedReason,MedPresc=MedPresc,MedPic=MedPic,MedPic2=MedPic2,MedAddress=MedAddress,
                       MedZip=MedZip)
        ins.save()
        messages.success(request,"Your submission to donate medicine is successfull , THANKYOU!")
    return render(request, 'webapp/donateMed.html')
