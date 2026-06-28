from django.shortcuts import *
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from . forms import *
from . models import *
from django.http import *
from django.contrib.auth import login
# Create your views here.
@transaction.atomic
def RegisterView(request,pk=None):
    instance_user=get_object_or_404(User,id=pk) if pk else None
    instance_profile=get_object_or_404(Profile,id=pk) if pk else None
    if request.method=="POST":
        user_form=UserRegistrationForm(request.POST,instance=instance_user)
        profile_form=ProfileRegistrationForm(request.POST,instance=instance_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()

            login(request,user)
            return redirect("Profile:login")
    else:
            user_form=UserRegistrationForm(instance=instance_user)
            profile_form=ProfileRegistrationForm(instance=instance_profile)
    context={
                'u_f':user_form,
                'p_f':profile_form
            }
    return render(request,"userregister.html",context)
@login_required
def Dashboard(request):
     return HttpResponse("login Sucessful")

def LoginView(request):
     if request.method=="POST":
          form=AuthenticationForm(request,data=request.POST)
          if form.is_valid():
               user=form.get_user()
               login(request,user)
               messages.success(request,f"welcome back, {user.username}")
               return redirect("Profile:dashboard")
          else:
               messages.error(request,"Invalid username and password")
     else:
          form=AuthenticationForm()
     return render(request,"Login.html",{'form':form})