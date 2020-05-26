from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.conf import settings
from .models import Profile, MyProfileUser


@login_required()
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usermail = form.cleaned_data.get('email')
            if User.objects.filter(email=usermail).exists():
                messages.info(request, f"{usermail} already exists.")
            else:
                form.save()
                username = form.cleaned_data.get('username')
                MyProfileUser.objects.create(profiler_email=usermail)
                subject = f"New employee added."
                message = f"An employee with the username {username} was just added."
                from_email = settings.EMAIL_HOST_USER
                to_list = [settings.EMAIL_HOST_USER]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
                messages.success(request, f"{username}'s profile successfully created.")
                return redirect('employees')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, "users/register.html", context)


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)
