from django.urls import path

#from main import sitemaps
from . import views
import re
from django.conf.urls import url, include
#from django.contrib.sitemaps.views import sitemap
#from main.sitemaps import ClientSiteMap

urlpatterns = [
    path("", views.home, name="home"),
    path("work/", views.work, name="work"),
    path("process/", views.process, name="process"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("potentialClientDetails/", views.getData, name="getData"),
    #path('sitemap.xml', sitemap, {'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap')  
]
