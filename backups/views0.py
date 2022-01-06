from django.http import HttpResponse


def home(request):
    return HttpResponse("<h2> 'home/'  involked home</h2>" )

def about(request):
    return HttpResponse("<h1> 'about/' involked about</h1>") 

def service(request):
    return HttpResponse("<h1>  'service/'involked service</h1>")    

def contact(request):
    return HttpResponse("<h1>  'contact/' involked contact</h1>")  

def login(request):
    return HttpResponse("<h1>  'login/' involked login</h1>")


def register(request):
    return HttpResponse("<h1>  'register/' involked login</h1>")