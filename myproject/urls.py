
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static
from django.conf import settings
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', views.home),
    path('viewsubcat/' , views.viewsubcat),
    path('about/' , views.about),
    path('register/' , views.register),
    path('checkEmail/' , views.checkEmail),
    path('verify/' , views.verify),
   
    path('contact/' , views.contact),
    path('service/' , views.service),
    path('login/' , views.login),
    path('myadmin/',include('myadmin.urls')),
    path('user/',include('user.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
