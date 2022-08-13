from django.shortcuts import render,HttpResponse,redirect
from .models import Signup
from .forms import SignupForm,Userformdata
from .models import Signup
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from website import settings
import random
# Create your views here.

def index(request):
    if request.method=="POST":
        if request.POST.get('signup')=='signup':
            myfrm=SignupForm(request.POST)
            if myfrm.is_valid():
                myfrm.save()
                print("Signup successfully")
                
                # sending mail
                otp = random.randint(1111, 9999)
                sub = 'Welcome to MySite'
                msg = f'Hope you will enjoy our company\nThank you for connecting with us!\nYour one time password is {otp}'
                from_id = settings.EMAIL_HOST_USER
                to_id = ['ankitramanuj.technocomet@gmail.com']
                send_mail(subject=sub, message=msg, from_email=from_id, recipient_list=to_id)
                
                return redirect('home')
            else:
                print(myfrm.errors)
        elif request.POST.get('login')=='login':
            unm = request.POST['email']
            pas = request.POST['password']
            userid = Signup.objects.get(email=unm)
            user = Signup.objects.filter(email=unm,password=pas)
            if user:
                request.session['userid']=email
                print("Login successfully")
                request.session['user']=unm
                request.session['userid']=userid.id
                return redirect('home')
            else:
                print("Login Faild, Try again")
    else:
        print("Something went wrong :(")
    return render(request, 'index.html')

def home(request):
    request.session.get('userid')
    user = request.session.get('user')
    if request.method=="POST":
        userfrm=Userformdata(request.POST,request.FILES)
        if userfrm.is_valid():
            userfrm.save()
            print("your Query has been uploaded")
            return redirect('home')
        else:
            print(userfrm.errors)
    else:
        userfrm=Userformdata()
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

def updateprofile(request):
    user = request.session.get('user')
    userid = request.session.get('userid')
    # id=Signup.objects.get(id=userid)
    if request.method=='POST':
        signupfrm=SignupForm(request.POST)
        id=Signup.objects.get(id=userid)
        if signupfrm.is_valid():
            signupfrm=SignupForm(request.POST,instance=id)
            signupfrm.save()
            print("your profile data has been updated!")
            return redirect('home')
        else:
            print(signupfrm.errors)
    else:
        print("Error....Something went wrong :(")
    return render(request,'updateprofile.html',{'user':user,'userid':Signup.objects.get(id=userid)})
    
def about(request):
    user = request.session.get('user')
    return render(request,'about.html',{'user':user})
    
def contact(request):
    user = request.session.get('user')
    return render(request,'contact.html',{'user':user})