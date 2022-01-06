from django.shortcuts import render,redirect 
from django.http import HttpResponse



#middleware to check session for user routes
def sessioncheckuser_middleware(get_response):
	def middleware(request):
		if request.path=='/user/':
			if request.session['sunm']==None or request.session['srole']!="user":
				response = redirect('/login/')
			else:
				response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware


# Create your views here.

def userhome(request):
    return render(request,"userhome.htm",{"sunm":request.session['sunm']})