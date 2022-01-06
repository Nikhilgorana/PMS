from django.http import HttpResponse
urlroute="""<h2> click link to redirect</h2>
<a href="/"> home page </a><br>
<a href="/about/"> about page </a><br>
<a href="/service/"> service page </a><br>
<a href="/login/"> login page </a><br>
<a href="/register/"> register page </a><br>
<a href="/contact/"> contact page </a><br>

"""


def home(request):
    print("url path:",request.path)
    print("url method:",request.method)
    return HttpResponse("<h2>   involked home</h2>"+urlroute )

def about(request):
    return HttpResponse("<h1>  involked about</h1>"+urlroute) 

def service(request):
    return HttpResponse("<h1>  involked service</h1>"+urlroute)    

def contact(request):
    return HttpResponse("<h1>   involked contact</h1>"+urlroute)  

def login(request):
    return HttpResponse("<h1>   involked login</h1>"+urlroute)


def register(request):
    return HttpResponse("<h1>  involked register</h1>"+urlroute)