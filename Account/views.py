from django.shortcuts import render
from .models import UserProfile



def add_education (request):
    if request.method=="GET":
        return render(request,"add-education.html")

def add_experience (request):
    if request.method=="GET":
        return render(request,"add-experience.html")

def create_profile (request):
    if request.method=="GET":
        return render(request,"create-profile.html")
    
def dashboard (request):
    if request.method=="GET":
        return render(request,"dashboard.html")
    
def login (request):
    if request.method=="GET":
        return render(request,"login.html")

def profile (request):
    if request.method=="GET":
        return render(request,"profile.html")
    
def profiles (request):
    if request.method=="GET":
        profiles= UserProfile.objects.all()
        return render(request,"profiles.html" , context={"profiles":profiles})
    
def register (request):
    if request.method=="GET":
        return render(request,"register.html")