"""My_Tech_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from login_app import views as login_views
from blog_app import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.index,name='index'),
    path('login/',include('login_app.urls')),
    path('logout/',login_views.user_logout,name='logout'),
    path('blog_app/',include('blog_app.urls',namespace='blog_app'))
    ]
