from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,password=password)
        user.save();
        return redirect('userapp:login')
    return render(request,'userapp/register.html')
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            return redirect("/")
        else:
            print("no user")    

    return render(request,"userapp/login.html")    