from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Appointment
from accounts.models import Doctor,Patient
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def reception(request):
    ap=Appointment.objects.all()
    p=Patient.objects.all()
    tot=len(ap)
    c={'ap': ap ,'p':p,'tot':tot}             
    return render(request,"appointments/reception.html",c)


@login_required
def createpat(request):
    if request.method=='POST':        
        
        fname=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        age=request.POST['age']
        add=request.POST['address']
        bg=request.POST['bloodgroup']
        casepaper=request.POST['casepaper']
        if User.objects.filter(username=email).exists():
            messages.info(request,"Email Id already Exists!")
            return redirect('crtpat')
        else:
            user=User.objects.create_user(first_name=fname,last_name='Patient',username=email,email=email)
            pro=Patient(user=user,phone=phone,gender=gender,age=age,address=add,bloodgroup=bg,casepaper=casepaper)
            pro.save()
            return redirect('reception')
    return render(request,'appointments/crtpat.html')

@login_required
def updatepat(request):
    if request.method=='POST':
        pid=request.POST['pid']
        pro=Patient.objects.filter(pid=pid).first()
        return render(request,'accounts/uprofile.html',{'pro':pro})

#Incomplete
# @login_required
# def appointments(request):
#     if request.user.last_name=="Patient":
#         pro=Patient.objects.filter(user=request.user).first()
#         ap=Appointment.objects.filter(patient=pro).all()            
#     
# 
#     return render(request,"appointments/appointments.html",c)