from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,'homepage.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def history(request):
    return render(request,'history.html')

def TermsAndCon(request):
    return render(request,'termsnCon.html')

def check_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    cred_email = ['shivam@gmail.com','muskan@gmail.com','admin@gmail.com']
    cred_password = ['123','456','admin']


    #cred_email.append()
    a=0
    b=0

    for temp in cred_email:
        if temp == email:
            pass
        if temp != email:
            a+=1
            pass

    for temp in cred_password:
        if temp == password:
            pass
        if temp != password:
            b+=1
            pass

    null=''
    if email == null or password == null:
        return HttpResponse('Login Failed')

    if a == b:
        return HttpResponse('Login Success')
    else:
        return HttpResponse('Login Failed')



    #creds={"shivam@gmail.com":"123","muskan@gmail.com":"456","admin@gmail.com":"admin1"}

    #siple username check login
    # for key in creds:
    #     if key == email :
    #         return HttpResponse(email+'\t Login Done')
    # for key in creds:
    #     if key != email:
    #         return HttpResponse(email+'\t Login failed')

    #Login using dictionary
    # for (key,values) in set(creds.items()):
    #     if key == email and values == password:
    #         return HttpResponse('Login Done')
    # for (key,values) in set(creds.items()):
    #     if key != email or values != password:
    #         return HttpResponse('Login failed')






