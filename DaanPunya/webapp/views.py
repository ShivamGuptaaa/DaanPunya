from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import medicine,rq_medicine,dnr_update,org_update,applied_medicine,dnr_address,reg_org
from django.contrib import messages
# from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import get_user_model 
from django.contrib.auth import authenticate,login as user_login ,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from django.core.mail import send_mail 
import random

User = get_user_model()

#for basic registeration
fname=''
lname=''
email=''
password=''
username=''

#To pass generated otp value
gen_otp=0

#for org registeration
reg_num=''
cert_num=''
phone=''
address=''

# Functions for Html pages
def index(request):
    org = User.objects.filter(is_org=True)
    params = {'orgs':org}
    return render(request,'webapp/index.html',params)

def login(request):
    return render(request,'webapp/login.html')

def register(request):
    return render(request,'webapp/register.html')

def orgRegister(request):
    return render(request,'webapp/orgRegister.html')

def about(request): 
    return render(request, 'webapp/about.html')

def contact(request):
    return render(request, 'webapp/contact.html')

def term(request):
    return render(request, 'webapp/term.html')

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
        MedPic=request.FILES.get('MedPic')
        MedPic2=request.FILES.get('MedPic2')
        # MedAddress=request.POST['MedAddress']
        # MedZip=request.POST['MedZip']
        ins = medicine(user_email=user_email,MedName=MedName,MedExpiry=MedExpiry,MedQuantity=MedQuantity,MedFor=MedFor,
                       MedReason=MedReason,MedPresc=MedPresc,MedPic=MedPic,MedPic2=MedPic2)
        ins.save()
        messages.success(request,"Your submission to donate medicine is successfull , THANKYOU!")
        update = dnr_update(user=request.user, med=ins)
        update.save()
        return redirect('status1')
    return render(request, 'webapp/donateMed.html')

@login_required(login_url='/login/')
def medView(request,id):
    displayMed = medicine.objects.filter(id=id)
    params = {'med': displayMed[0]}
    if request.method == 'POST':
        rqst_user_med = dnr_update.objects.filter(med=displayMed[0]).first()
        print(rqst_user_med)
        rqst_user_med.rqst_user_email = request.user.email
        rqst_user_med.save()
        print(displayMed)
        displayMed[0].update = True
        displayMed[0].save
        # To create applied_medicine table we are using below command
        tmp = applied_medicine(med=rqst_user_med.med,user=request.user)
        tmp.save()
        donor = displayMed[0].user_email
        subject = 'Your medicine got a receiver'
        message = f'Hi {donor.first_name}{donor.last_name}, {request.user.first_name} has requested to get your {displayMed[0].MedName} medicine, PLease follow the link below for more details are proceed further or to decline the request'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [donor.email, ] 
        send_mail( subject, message, email_from, recipient_list ) 
        return render(request, 'webapp/medView.html',{'med': displayMed[0],'ack': 'Requested to donor for medicine'})
    if displayMed[0].update:
        params = {'med': displayMed[0],'ack': 'Requested to donor for medicine'}
    return render(request, 'webapp/medView.html',params)

@login_required(login_url='/login/')
def searchResult(request):
    flag=1
    # This variable flag is used to fix repeating similar meds issue
    if request.GET['searchMed'] == "all":
        meds = medicine.objects.all()
        similar_meds=None
        flag=None
    else:
        searchMed = request.GET['searchMed']
        meds = medicine.objects.filter(MedName__iexact = searchMed).exclude(update = True)
        similar_meds = medicine.objects.filter(MedName__icontains = searchMed).exclude(MedName__iexact = searchMed).exclude(update = True)
        if meds and similar_meds :
            flag=None
        if not meds and not similar_meds :
            flag=None
    print(flag)
    params={ 'meds': meds, 'similar_meds':similar_meds, 'flag': flag}
    return render(request, 'webapp/searchResult.html',params)

@login_required(login_url='/login/')
def status(request,rq_med_id=0):
    med_lst = {}
    user = request.user
    if request.method == "POST":
        if request.POST['flag'] == "rq_med":
            del_mode = request.POST['del_mode']
            from_date = request.POST['from_date']
            to_date = request.POST['to_date']
            rqst_med = rq_medicine.objects.filter(id=rq_med_id).first()
            print(rqst_med)
            update = org_update.objects.filter(rq_med=rqst_med).first()
            print(update)
            update.mode_del = del_mode
            update.frm_date = from_date
            update.to_date = to_date
            update.save()
            rqst_med.update=True
            rqst_med.save()
        elif request.POST['flag'] == "app_med":
            del_mode = request.POST['del_mode']
            from_date = request.POST['from_date']
            to_date = request.POST['to_date']
            # applied_med = dnr_update.objects.filter(med=rq_med_id)
            applied_med = medicine.objects.filter(id=rq_med_id).first()
            print(applied_med)
            update_med = dnr_update.objects.filter(med=applied_med).first()
            print(update_med)
            update_med.mode_del = del_mode
            update_med.frm_date = from_date
            update_med.to_date = to_date
            update_med.save()
            # mail to donor that org has chosen mode of delivery and date range
            subject = f'Update on your medicine ( {update_med.med.MedName} )'
            message = f'Hi {update_med.user.first_name}{update_med.user.last_name}, {request.user.first_name} {request.user.last_name} has chosen mode of delivery( Note: All charges needed in delivery process will be taken care by {request.user.first_name} {request.user.last_name}) and range of date when they need that medicine, PLease follow the link below and select the date from that range according to your preference of medicine to be picked http://127.0.0.1:8000/status1 '
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [update_med.user.email, ] 
            send_mail( subject, message, email_from, recipient_list )

            print(applied_med.update)
            applied_med.update = True
            print(applied_med.update)
            applied_med.save()
        else:
            HttpResponse("error")
        med = org_update.objects.filter(user=user)
        app_med = dnr_update.objects.filter(rqst_user_email=user.email)
        med_lst = {'lst' : med,'app_med' : app_med}
        messages.success(request,"Medicne details updated")
        return render(request, 'webapp/status.html' ,med_lst)
    else:
        med = org_update.objects.filter(user=user)
        app_med = dnr_update.objects.filter(rqst_user_email=user.email)
        print(med,app_med)
        med_lst = {'lst' : med,'app_med' : app_med }
        return render(request, 'webapp/status.html' ,med_lst)

def status1(request,rq_med_id=0):
    med_lst = {}
    user = request.user
    if request.method == "POST":
        address = request.POST['address']
        state = request.POST['state']
        city = request.POST['city']
        zipcode = request.POST['zipcode']
        sel_date= request.POST['sel_date']
        med_search = dnr_update.objects.filter(med=rq_med_id).first()
        med_obj = medicine.objects.filter(id=rq_med_id).first()
        address_save = dnr_address(user=user,med=med_obj)
        address_save.address=address
        address_save.state=state
        address_save.city=city
        address_save.zipcode=zipcode
        address_save.save()
        med_search.select_date = sel_date
        med_search.save()
        org_user = User.objects.filter(email=med_search.rqst_user_email).first()
        print(org_user)
        subject = f'Date chosen by donor for {med_search.med.MedName} '
        message = f'Hi {org_user.first_name}{org_user.last_name}, {user.first_name} {user.last_name} has chosen date of pick up from given range and address is also provided to pickup medicine( Note: All charges for this transaction in delivery of this mediicne will be covered by you ), please click on this below link for selected date http://127.0.0.1:8000/status1 '
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [org_user.email, ] 
        send_mail( subject, message, email_from, recipient_list )

        tmp = applied_medicine.objects.filter(med=rq_med_id)
        med_lst = dnr_update.objects.filter(user=user)
        meds= {'lst': med_lst,'app_med': tmp}
        messages.success(request,"Medicine details updated")
        return render(request, 'webapp/status1.html',meds)
    else:
        med_lst = dnr_update.objects.filter(user=user)
            
        params= {'lst': med_lst}
        return render(request, 'webapp/status1.html' ,params)



def rqMed(request):
    if request.method == "POST":
        user_email = request.user
        MedName=request.POST['MedName']
        MedQuantity=request.POST['MedQuantity']
        MedFor=request.POST['MedFor']
        MedReason=request.POST['MedReason']
        MedPresc=request.POST['MedPresc']
        med = rq_medicine(user_email=request.user,MedName=MedName,MedFor=MedFor,MedReason=MedReason,MedPresc=MedPresc,MedQuantity=MedQuantity)
        med.save()
        messages.success(request,"Your request for medicine is been uplaoded, you will be notified as soon as any medicine matches")
        update= org_update(user=request.user,rq_med=med)
        update.save()
        return render(request,'webapp/rqMed.html')
    return render(request,'webapp/rqMed.html')


def sendAddress(request,id=0):
    if request.method == "POST":
        user = request.user
        med = medicine.objects.filter(id=id).first()
        print(med)
        address = dnr_address.objects.filter(med=med).first()
        print(address)
        subject = f'Address for the medicine ( {med.MedName} )'
        message = f'Hi {user.first_name} {user.last_name}, address for {med.MedName} is mentioned below \n {address.address} \n City: {address.city} \n State: {address.state} \n Zipcode: {address.zipcode}'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [user.email, ] 
        send_mail( subject, message, email_from, recipient_list )
        med = org_update.objects.filter(user=user)
        app_med = dnr_update.objects.filter(rqst_user_email=user.email)
        print(med,app_med)
        med_lst = {'lst' : med,'app_med' : app_med }
        return render(request, 'webapp/status.html' ,med_lst)

# APIs
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
        username=email
        global gen_otp
        gen_otp= str(random.randint(1000,9999))
        print(gen_otp)
        subject = 'Danpunya'
        message = f'Hi {fname}, your OTP to register in Daanpunya is {gen_otp}'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email, ] 
        send_mail( subject, message, email_from, recipient_list ) 
        return render(request, 'webapp/checkOtp.html')
    else:
        return render(request, 'webapp/register.html')

def handleOrgRegister(request):
    if request.method == 'POST':
        #Extracting POST parameters
        global username
        global fname
        global lname
        global password
        global email
        global cert_num
        global reg_num
        global phone
        global address
        fname=request.POST['Fname']
        lname=request.POST['Lname']
        email=request.POST['email']
        password=request.POST['password']
        reg_num=request.POST['reg_num']
        cert_num=request.POST['cert_num']
        phone=request.POST['phone']
        address=request.POST['address']
        org = (reg_org.objects.filter(Q(reg_num = reg_num) , Q(cert_num__iexact = cert_num)))
        print(org)
        if not org:
            messages.error(request,"Please enter proper registeration number or tax exemption certificate number","danger")
            return redirect('orgRegister')
        else: 
            username=email
            global gen_otp
            gen_otp= str(random.randint(1000,9999))
            print(gen_otp)
            subject = 'Danpunya'
            message = f'Hi {fname}, your OTP to register in Daanpunya is {gen_otp}'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email, ] 
            send_mail( subject, message, email_from, recipient_list ) 
            return render(request, 'webapp/checkOtp.html')
    else:
        return render(request, 'webapp/orgRegister.html')

def handleOtp(request):
    if request.method == 'POST':
        otp=request.POST['otp']
        global gen_otp
        global username
        global fname
        global lname
        global password
        global email
        global cert_num
        global reg_num
        global phone
        global address

        print(gen_otp)

        if (cert_num=='' and reg_num =='' and phone == '' and address == ''):

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
        elif (cert_num is not '' and reg_num is not '' and phone is not '' and address is not ''):
            if otp == gen_otp:
                MyUser =User.objects.create_user(username,email=email,password=password)
                MyUser.first_name=fname
                MyUser.last_name=lname
                MyUser.is_org =True
                MyUser.reg_num=reg_num
                MyUser.cert_num=cert_num
                MyUser.phNum=phone
                MyUser.address=address
                MyUser.save()
                reg_num = cert_num = phone = address = ''
                messages.success(request,"Your DaanPunya account has been successfully created")
                return render(request, 'webapp/login.html')
            else:
                messages.error(request,"Your OTP didn't matched , PLease Try Again","danger")
                return redirect('home')
        else:
            messages.error(request,"Please enter all credentials","danger")
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
            if request.GET.get('next'):
                return redirect(request.GET('next'))
            else:
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