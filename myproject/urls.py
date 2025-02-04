from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',signupPage,name="signupPage"),
    path("signInPage/", signInPage, name="signInPage"),
    path("homePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("ProfilePage/", profilePage, name="profilePage"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)