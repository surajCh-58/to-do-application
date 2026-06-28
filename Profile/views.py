from django.shortcuts import *
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from . forms import *
from . models import *
from django.http import *
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

# Create your views here.
@transaction.atomic
def RegisterView(request, pk=None):
    instance_user = get_object_or_404(User, id=pk) if pk else None
    instance_profile = get_object_or_404(Profile, user=instance_user) if instance_user else None

    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST, instance=instance_user)
        profile_form = ProfileRegistrationForm(request.POST, instance=instance_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            if not pk:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}! Your account has been created.")
                return redirect("Task:alltask")
            else:
                messages.success(request, "Profile updated successfully.")
                return redirect("Profile:dashboard", pk=user.pk)
    else:
        user_form = UserRegistrationForm(instance=instance_user)
        profile_form = ProfileRegistrationForm(instance=instance_profile)

    context = {
        'u_f': user_form,
        'p_f': profile_form,
        'instance': instance_user,
    }
    return render(request, "userregister.html", context)


@login_required
def Dashboard(request):
    from Task.models import Task
    tasks = Task.objects.filter(user=request.user)
    completed = tasks.filter(status='c').count()
    pending = tasks.filter(status='p').count()
    in_progress = tasks.filter(status='I').count()
    recent = tasks.order_by('-created_at')[:5]
    context = {
        'total': tasks.count(),
        'completed': completed,
        'pending': pending,
        'in_progress': in_progress,
        'recent': recent,
    }
    return render(request, "index.html", context)


def LoginView(request):
    if request.user.is_authenticated:
        return redirect("Profile:dashboard")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("Profile:dashboard")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, "Login.html", {'form': form})


@login_required
def LogoutView(request):
    logout(request)
    messages.success(request, "You've been signed out.")
    return redirect("Profile:login")
