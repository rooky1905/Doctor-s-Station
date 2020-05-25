from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request, 'home/about.html')