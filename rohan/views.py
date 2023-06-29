from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from rohan.models import contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

# RohanMistry -> Rohan123@
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    # context = {
    #     "variable" : "Rohan is the best"
    # }
    # messages.success(request,"This the home page")
    # return HttpResponse("This is Home Page")
    return render(request,'index.html')

def loginUser(request) :
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password= password)

        if user is not None :
            login(request,user)
            return redirect("/")
        
        else :
            return render(request,'login.html')
    
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")




def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    # return HttpResponse("This is about Page")
    return render(request,'about.html')

def services(request):
    if request.user.is_anonymous:
        return redirect("/login")
    # return HttpResponse("This is Services Page")
    return render(request,'services.html')

def contactus(request):
    if request.user.is_anonymous:
        return redirect("/login")
    # return HttpResponse("This is contactus Page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        contacts = contact(name = name,email = email,password = password,phonenumber=phonenumber,date = datetime.today())
        contacts.save()
        messages.success(request, "Your Data has been registered...")

    return render(request,'contactus.html')

