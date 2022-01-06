from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.conf import settings
from .import emailAPI

import time
from . import models
from myadmin import models as myadmin_models

media_url=settings.MEDIA_URL



#middleware to check session for mainapp routes
def sessioncheck_middleware(get_response):
	def middleware(request):
		if request.path=='' or request.path=='/home/' or request.path=='/about/' or request.path=='/contact/' or request.path=='/login/' or request.path=='/service/' or request.path=='/register/':
			request.session['sunm']=None
			request.session['srole']=None
			
			response = get_response(request)
				
		else:
			response = get_response(request)		
		return response	
	return middleware





def home(request): 
    clist=myadmin_models.Category.objects.all()
    return render(request,"home.htm",{"clist":clist,"media_url":media_url})

def viewsubcat(request):
    catnm=request.GET.get('cnm')
    sclist=myadmin_models.SubCategory.objects.filter(catnm=catnm)
    clist=myadmin_models.Category.objects.all()
    return render(request,"viewsubcat.htm",{"clist":clist,"sclist":sclist,"media_url":media_url,"catnm":catnm})


def about(request):
    return render(request,"about.htm") 

def service(request):
    return render(request,"service.htm")     
 
def contact(request):
    return render(request,"contact.htm")  
    
def verify(request):
    vemail=request.GET.get("vemail")
    models.Register.objects.filter(username=vemail).update(status=1)
    return redirect('/login/') 


def checkEmail(request):
	unm=request.GET.get('unm')
	
	userDetails=models.Register.objects.filter(username__startswith=unm)
	
	if len(userDetails)==0:
		res=0
	else:
		res=1		
	return HttpResponse(res)      
     

def login(request):
    if request.method=="GET":
        return render(request,"login.htm",{"msg":""})
    else:
        username=request.POST.get("username")
        password=request.POST.get("password")
        userdetails=models.Register.objects.filter(username=username,password=password,status=1)
        if len(userdetails)==0:
            return render(request,"login.htm",{"msg":"invalid user or verified your account"})  
        else:
            # session to store user details
            request.session['sunm']=userdetails[0].username
            request.session['srole']=userdetails[0].role
            if userdetails[0].role=="user":
                return redirect("/user/")
            else:    
                return redirect("/myadmin/")
def register(request):
    if request.method=="GET":
        return render(request,"register.htm",{"msg":" "}) 
    else:
        #to recieve data on views from from 
        #print(request.POST)
        name=request.POST.get("name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        address=request.POST.get("address")
        mobile=request.POST.get("mobile")
        city=request.POST.get("city")
        gender =request.POST.get("gender")
        info=time.asctime()

        p=models.Register(name=name,username=username,password=password,address=address,mobile=mobile,city=city,gender=gender,role="user",status="1",info=info)
        p.save()  
        emailAPI.sendMail(username,password)     
        return render(request,"register.htm",{"msg":"user registered successfully "}) 