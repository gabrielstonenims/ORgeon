from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import School, Student, SchoolLoginCode
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .forms import (KidsSchoolRegister, KidsSchoolUpdateForm, KidsSchoolProfileUpdate, )
from email.message import EmailMessage
from django.conf import settings
import smtplib
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect


def summerhome(request):
    return render(request, "summerschool/summerhome.html")


def register_school(request):
    msg = EmailMessage()
    if request.method == "POST":
        form = KidsSchoolRegister(request.POST)
        if form.is_valid():
            kids_email = form.cleaned_data.get('email')
            kids_school = form.cleaned_data.get('school')

            if User.objects.filter(email=kids_email).exists():
                messages.info(request, f"Sorry,a user with the same email already exists")
            else:
                form.save()
                Student.objects.create(student_email=kids_email)
                msg["Subject"] = "Thank you for joining our summer tutoring program."
                msg["From"] = settings.EMAIL_HOST_USER
                msg["To"] = kids_email
                msg.set_content(
                    "We are glad you have decided to join us in this studies,so you know it's going to be more fun than you expected,stay blessed and see you in class.")
                hml = f"""
                    <!Doctype html>
                    <html>
                    <body>
                    <h1 style='font-style:italic;'>Thank you for joining our summer tutoring program.</h1>
                    <p style='color:SlateGray;'> We are glad you have decided to join us in this studies,so you know it's going to be more fun than you expected,stay blessed and see you in class.</p>
                    <p style='color:SlateGray;'>ORgeonofstars</p>
                    </body>
                    </html>
                    </html>
                    """
                msg.add_alternative(hml, subtype='html')
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                    smtp.send_message(msg)
                    messages.success(request, f"Thank you for joining our summer tutoring program.")
                    return redirect('school_login')
                # to organization email
                msg["Subject"] = "A new Kid just joined the gradeschool summer tutoring program"
                msg["From"] = settings.EMAIL_HOST_USER
                msg["To"] = settings.EMAIL_HOST_USER
                msg.set_content(
                    "Got a new kid for the summer tutoring program.")
                hml = f"""
                    <!Doctype html>
                    <html>
                    <body>
                    <h1 style='font-style:italic;'>A new Kid just joined the gradeschool summer tutoring program</h1>
                    <p style='color:SlateGray;'> Got a new kid for the summer tutoring program.</p>
                    <p style='color:SlateGray;'>ORgeonofstars</p>
                    </body>
                    </html>
                    </html>
                    """
                msg.add_alternative(hml, subtype='html')
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                    smtp.send_message(msg)
        else:
            messages.info(request, f"Something went wrong")
    else:
        form = KidsSchoolRegister()

    context = {
        "form": form
    }
    return render(request, "summerschool/schoolregister.html", context)


@login_required
def kids_profile_school(request):
    if School.objects.filter(user=request.user).exists():
        user = get_object_or_404(School, user=request.user)
        if user:
            user.verified = True
            user.save()
    
        if request.method == "POST":
            ug_form = KidsSchoolUpdateForm(request.POST, instance=request.user)
            ugp_form = KidsSchoolProfileUpdate(request.POST, request.FILES, instance=request.user.school)
            if ug_form.is_valid() and ugp_form.is_valid():
                ug_form.save()
                ugp_form.save()
                return redirect('schoolhome')
        else:
            ug_form = KidsSchoolUpdateForm(instance=request.user)
            ugp_form = KidsSchoolProfileUpdate(instance=request.user.school)
    else:
        messages.info(request, f"sorry you are not in our school list")
        return redirect('summerhome')

    context = {
        "ug_form": ug_form,
        "ugp_form": ugp_form
    }

    return render(request, "summerschool/schoolprofile.html", context)


def school_login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            uname = request.POST['username']
            upassword = request.POST['password']
            user = authenticate(username=uname, password=upassword)
            if user is not None:
                login(request, user)
                uemail = user.email
                suser = get_object_or_404(School, user=user)
                if Student.objects.filter(student_email=uemail).exists():
                    if suser.verified:
                        return redirect('schoolhome')
                    else:
                        return redirect('school_profile')
                else:
                    messages.info(request, f"sorry we don't have your name in our school lists")
                    return redirect('main')
                # Redirect to a success page.
            else:
                messages.info(request, f"invalid username or password")
        else:
            messages.info(request, f"invalid information given")
    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }

    return render(request, "summerschool/school_login.html", context)


@login_required
def schoolhome(request):
    try:
        user = request.user
        can_attend_class = False
        is_in_gradeschool = False
        is_in_preschool = False
        is_in_kindergarten = False

        if School.objects.filter(user=user).exists():
            can_attend_class = True
        school_kid = School.objects.get(user=user)

        if school_kid.school == "GradeSchool":
            is_in_gradeschool = True
        elif school_kid.school == "PreSchool":
            is_in_preschool = True

        elif school_kid.school == "Kindergarten":
            is_in_kindergarten = True
            
    except Exception as error:
        messages.info(request, "Sorry you are not in our school list")

    context = {
        "can_attend_class": can_attend_class,
        "is_in_gradeschool": is_in_gradeschool,
        "is_in_preschool": is_in_preschool,
        "is_in_kindergarten": is_in_kindergarten
    }

    return render(request, 'summerschool/school_home.html', context)


@login_required
def school_logout(request):
    return render(request, "summerschool/logout.html")
