from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor
from django.contrib import messages
import datetime
import random

def register(request):
    if request.method=='POST': #checking if the request is POST, stating it is requested upon some user action
        fname=request.POST['fname']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        phone=request.POST['phone']
        typ=request.POST['type']
        if pass1==pass2:
            if User.objects.filter(username=email).exists():
                messages.info(request,"Email Id already Exists!")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=fname,last_name=typ,username=email,password=pass1,email=email)
                if typ=="Doctor":
                    pro=Doctor(user=user,phone=phone)
                    pro.save()
                    messages.info(request,"Account Created Successfully")
                    return redirect('login')
                if typ=="Patient":
                    pro=Patient(user=user,phone=phone)
                    pro.save()
                    messages.info(request,"Account Created Successfully")
                    return redirect('login')
        else:
            messages.info(request,"Passwords not matching!")
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request, user)
            if request.user.last_name=="Reception":
                return redirect('reception')
            if user.last_name=="Doctor":
                pro= Doctor.objects.filter(user=user).first()
                return redirect('uprofile')
            if user.last_name=="Patient":
                pro= Patient.objects.filter(user=user).first()
                return redirect('uprofile')
            else:
                return redirect('profile')
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

@login_required #decorator
def uprofile(request):
    if request.user.last_name=='Doctor':
        pro=Doctor.objects.filter(user=request.user).first()
    if request.user.last_name=='Patient':
        pro=Patient.objects.filter(user=request.user).first()
    if request.user.last_name=='Reception':
        pid=request.POST['pid']
        pro=Patient.objects.filter(pid=pid).first()
    if request.method=='POST':
        if request.user.last_name=='Reception':
            pid=request.POST['pid']
            pro=Patient.objects.filter(pid=pid).first()
        
        pro.phone=request.POST['phone']
        pro.age=request.POST['age']
        pro.gender=request.POST['gender']
        if pro.user.last_name=='Patient':
            pro.address=request.POST['address']
            pro.casepaper=request.POST['casepaper']
            pro.bloodgroup=request.POST['bloodgroup']
        if pro.user.last_name=='Doctor':
            pro.status=request.POST['status']
            pro.salary=request.POST['salary']
            pro.Department=request.POST['dept']
            pro.attendance=request.POST['attn']
        pro.save()
        if request.user.last_name=='Reception':
            return redirect("reception")
        return redirect('profile')
    c={'pro':pro}
    return render(request,'accounts/uprofile.html',c)


@login_required
def profile(request):
    if request.user.last_name=='Doctor':
        pro=Doctor.objects.filter(user=request.user).first()
    if request.user.last_name=='Patient':
        pro=Patient.objects.filter(user=request.user).first()
    c={'pro':pro}
    return render(request,'accounts/profile.html',c)

def logout(request):
    auth.logout(request)
    return redirect('login')