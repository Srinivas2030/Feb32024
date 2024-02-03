from django.urls import path
from .import views

urlpatterns = [
    #-------- Register a  User--------#
    path('register',views.register,name="register"),
    path('',views.home,name=""),
    #------------ DashBoard-Page---- #
    
    path('dashboard',views.dashboard,name="dashboard"),
    
    path('home',views.home),
    
     #------------Login a User ------- #  
    
    path('myllogin',views.myllogin,name="myllogin"),
   
   
    
    
   
    
    
    #------------Login Out  User ------- #  
    path('userllogout',views.userllogout,name="userllogout"),
    
]
