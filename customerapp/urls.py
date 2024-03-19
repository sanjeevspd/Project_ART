"""
URL configuration for artgallery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from. import views
from django.conf import settings


urlpatterns = [
     path("contact/",views.contactfunction,name="contactfunction"),
     path("greeitng",views.greeting,name="greeting"),
     path('search/', views.search_view, name='search'),
     path('search1/', views.search_view1, name='search1'),
     path('search_suggestions/', views.search_suggestions, name='search_suggestions'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
