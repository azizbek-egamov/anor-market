"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from main.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', homePage, name='home'),
    path('about/', aboutPage, name='about'),
    path('contact/', contactPage, name='contact'),
    path("update/<int:id>/", UpdatePage, name='update'),
    path("delete/<int:id>/", DeletePage, name='delete'),
    path("login/", LoginPage, name='login'),
    path("signup/", SignupPage, name='signup'),
    path("logout/", LogoutPage, name='logout'),
    path('category/<str:some_value>/', CategoryPage, name='CategoryPage'),
    path('product/<str:some_value>/<int:id>/', ProductPage, name='CategoryPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
