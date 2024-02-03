from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import admin
from .forms import CreateUserForm,LoginForm

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    
    return render(request,'index.html')






 


#registering a user

def register(request):
     form=CreateUserForm()
     if request.method=='POST':
          form=CreateUserForm(request.POST)
          if form.is_valid():
               form.save()
               
               return HttpResponse("User registered Sucessfully")
          
     context={'form':form}
     
     return render(request,'register.html',context=context)     
  
  
  
  
          
#-----------Login in a user-----#
    
def myllogin(request):
     form=LoginForm
     if  request.method == 'POST':
          form =LoginForm(request,data=request.POST)
          if form.is_valid():
               username=request.POST.get('username')
               password=request.POST.get('password')
               
               user=authenticate(request,username=username,password=password)
               if user is not None:
                    auth.login(request , user)
                    return redirect('dashboard')
               
     context={'form':form}
     return render(request,'my-login.html',context=context)    


#---------- Dashboard-page --------#
@login_required(login_url='myllogin')
def dashboard(request):
     return render(request,'dashboard.html')

#---------------user logout------#
def userllogout(request):
     auth.logout(request)  
     
     return redirect("")