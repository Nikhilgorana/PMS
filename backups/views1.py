from django.http import HttpResponse


def home(request):
    return HttpResponse("<h2>welcome to django </h2>" )