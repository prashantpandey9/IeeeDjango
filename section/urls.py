from django.contrib import admin
from django.urls import path,include
from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.main,name='main'),
    path('xtreme/',views.xtreme,name='xtreme')
]
# urlpatterns+=staticfiles_urlpatterns
