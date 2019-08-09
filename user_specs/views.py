from django.shortcuts import render,redirect
from . custom_form import CustomReg,UpdateReg,UpdateDp,RegisterDp,Login_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.


def login(request):
    if(request.method=="POST"):
        form=Login_form(request.POST)
        if(form.is_valid()):
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("User is logged in")
    if(request.method=="GET"):
        form=Login_form()
    return render(request,"user_specs/login_new.html",{"form":form})

def sign_up(request):
    if(request.method=="POST"):
        my_form=CustomReg(request.POST)
        pr_form= RegisterDp(request.POST,request.FILES)
        if my_form.is_valid() and pr_form.is_valid():
            my_form.save()
            x = Profile()
            username=my_form.cleaned_data.get("username")
            x.my_user = User.objects.get(username = username)
            x.dp = request.FILES['dp']
            if x.dp==None:
                x.dp=x.dp.default;
            x.save()
            messages.success(request, f' Hi {username}! You are successfully registered' )
            return redirect("login")
    else:
         my_form=CustomReg()
         pr_form= RegisterDp()
    return render(request,"user_specs/forms.html",{"forms":my_form,"dp":pr_form})


@login_required
def profile(request):
    if(request.method=='POST'):
        update_form=UpdateReg(request.POST,instance=request.user)
        update_dp=UpdateDp(request.POST,request.FILES,instance=request.user.profile)
        if(update_form.is_valid() and update_dp.is_valid()):
            update_form.save()
            update_dp.save()
            username=update_form.cleaned_data.get('username')
            messages.success(request,f'{username.title()}, Your profile is successfully updated')
            return redirect('profile')
    else:
        update_form=UpdateReg(instance=request.user)
        update_dp=UpdateDp(request.FILES,instance=request.user.profile)
    return render(request,"user_specs/profile.html",{"forms":update_form,"dps":update_dp})
