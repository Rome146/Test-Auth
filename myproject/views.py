from django.shortcuts import render,redirect

from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        user_type=request.POST.get("user_type")
        Profile_Pic=request.FILES.get("Profile_Pic")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
                Profile_Pic=Profile_Pic,
            )
            if user_type=='seeker':
                seekerProfileModel.objects.create(user=user)
                
            elif user_type=='recruiter':
                recruiterProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')


def homePage(request):
    
    
    return render(request,"base.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")