"""
URL configuration for ankuraurdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from vege.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('myApp/', include('myApp.urls')),
    path('receipes/',receipes, name='receipe'),
    path('receipes_list/',receipes_list, name='receipes_list'),
    path('delete_receipe/<id>/', delete_receipe, name = "delete_receipe"),      #dynamic id <id>
    path('update_receipe/<id>/', update_receipe, name = "update_receipe"),      #dynamic id <id>
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name = "logout_page"),
    path('register/', register_page, name="register_page"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()