from django.db import models
from django.contrib.auth.models import User #importing django built in user!

class Patient(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pid=models.AutoField(primary_key=True)
    phone=models.CharField(max_length=10)
    age=models.CharField(max_length=3)
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    bloodgroup=models.CharField(max_length=10)
    casepaper=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.first_name}'

class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    did=models.AutoField(primary_key=True)
    phone=models.CharField(max_length=10)
    age=models.CharField(max_length=3)
    gender=models.CharField(max_length=10)
    Department=models.CharField(max_length=20)
    attendance=models.CharField(max_length=10)
    status=models.CharField(max_length=15)
    salary=models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.user.first_name}'