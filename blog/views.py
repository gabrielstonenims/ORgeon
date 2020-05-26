from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import (Volunteer, Events, JoinTrip, Partnership, NewsLetter, Report, Post, Comments, NewsUpdate, Gallery,
                     LoginCode, Online_user, MessageD, Message, ContactUs, ClientInfoProgress)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from email.message import EmailMessage
import smtplib
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import pytz
from django.db.models import Q
from datetime import datetime, date, time, timedelta
from django.core.paginator import Paginator
from .forms import (VolunteerForm,
                    JoinTripForm,
                    PartnershipForm,
                    NewsLetterForm,
                    ReportForm,
                    PostForm, CommentsForm,
                    NewsUpdateForm, Message_Form, MessageD_Form, ContactForm, ClientProgressUpdateForm
                    )
from django.contrib.auth.models import User
import random
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
import time
from summerschool.models import  School
from users.models import Profile, MyProfileUser
from summerschool.models import School,Student

# global time checker
CAN_STAY_LOGGED_IN1 = 30
CAN_STAY_LOGGED_IN2 = 45
CAN_STAY_LOGGED_IN3 = 55
CAN_STAY_LOGGED_IN4 = 15


@login_required()
def news_letter(request):
    msg = EmailMessage()
    suscribed_users = NewsLetter.objects.all()
    if request.method == "POST":
        form = NewsUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title').upper()
            update_message = form.cleaned_data.get('message')
            msg["Subject"] = title
            msg["From"] = settings.EMAIL_HOST_USER
            msg["To"] = suscribed_users
            msg.set_content(update_message)
            hml = f"""
            <!Doctype html>
            <html>
            <body>
            <h1 style='font-style:italic;'>{title}</h1>
            <p style='color:SlateGray;'>  {update_message} </p>
            </body>
            </html>
            </html>
            """
            msg.add_alternative(hml, subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                smtp.send_message(msg)
                messages.success(request, f"News update messages sent successfully.")
                return redirect('newsletter_create')
    else:
        form = NewsUpdateForm()

    context = {
        "form": form
    }

    return render(request, "blog/newsletter.html", context)


def home(request):
    if request.method == "POST":
        msg = EmailMessage()
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if NewsLetter.objects.filter(email=email).exists():
                messages.info(request, "This email already exists.")
            else:
                form.save()
                msg["Subject"] = "Thank you for subcribing to our newsletter."
                msg["From"] = settings.EMAIL_HOST_USER
                msg["To"] = email
                msg.set_content("We will send you all the necessary updates.")
                hml = f"""
                <!Doctype html>
                <html>
                <body>
                <h1 style='font-style:italic;'>Thank you for subcribing to our newsletter.</h1>
                <p style='color:SlateGray;'> We will send you all the necessary updates.</p>
                <p style='color:SlateGray;'>Stay blessed.</p>
                <p style='color:SlateGray;'>ORgeonofstars</p>
                </body>
                </html>
                </html>
                """
                msg.add_alternative(hml, subtype='html')
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
                    smtp.send_message(msg)
                    messages.success(request, f"Thank you,your email has been added to our newslist.")
                    return redirect('home')

    else:
        form = NewsLetterForm()

    context = {
        'form': form
    }
    return render(request, "blog/home.html", context)


def success_stories(request):
    return render(request, "blog/success-stories.html")


def needy_stories(request):
    return render(request, "blog/stories_of_need.html")


def inspirational_stories(request):
    return render(request, "blog/inspirational_stories.html")


def some_videos(request):
    return render(request, "blog/some_videos.html")


class VolunteerFormView(CreateView):
    model = Volunteer
    fields = ['name', 'email', 'profession', 'country', 'photo', 'phone', 'why_join_Orgeon', 'additional_message']
    success_url = '/volunteers'

    def form_valid(self, form):
        v_email = form.cleaned_data.get('email')
        msg = EmailMessage()
        msg1 = EmailMessage()

        msg["Subject"] = f"New volunteer."
        msg["From"] = settings.EMAIL_HOST_USER
        msg["To"] = settings.EMAIL_HOST_USER
        msg.set_content(f"Someone just  volunteered for Orgeon.")
        hml = f"""
        <!Doctype html>
        <html>
        <body>
        <h1 style='font-style:italic;'>New volunteer</h1>
        <p style='color:SlateGray;'> Someone just  volunteered for Orgeon.</p>
        </body>
        </html>
        </html>
        """
        msg.add_alternative(hml, subtype='html')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            smtp.send_message(msg)
        # to user volunteering email
        msg1["Subject"] = "Welcome to ORgeon of stars"
        msg1["From"] = settings.EMAIL_HOST_USER
        msg1["To"] = v_email
        msg1.set_content(
            "Thank you for volunteering with Orgeon of stars,in order to know more about  you we will contact you soon,stay blessed.")
        hml = f"""
        <!Doctype html>
        <html>
        <body>
        <h1 style='font-style:italic;'>Welcome to ORgeonofstars.</h1>
        <p style='color:SlateGray;'> Thank you for volunteering with Orgeon of stars,in order to know more about  you we will contact you soon.</p>
        <p style='color:SlateGray;'>Stay blessed.</p>
        <p style='color:SlateGray;'>ORgeonofstars</p>
        </body>
        </html>
        </html>
        """
        msg1.add_alternative(hml, subtype='html')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            smtp.send_message(msg1)
            # return redirect('volunteers')
        return super().form_valid(form)


class Volunteers(ListView):
    model = Volunteer
    template_name = 'blog/volunteers_list.html'
    context_object_name = 'volunteers'
    ordering = ['-date_volunteered']


class OurVolunteers(LoginRequiredMixin, ListView):
    model = Volunteer
    template_name = 'blog/ourvolunteer_list.html'
    context_object_name = 'ourvolunteers'
    ordering = ['-date_volunteered']


def events(request):
    events = Events.objects.all().order_by('-date_posted')[:1]

    context = {
        'events': events
    }

    return render(request, "blog/events.html", context)


def join_trip(request):
    msg = EmailMessage()
    msg1 = EmailMessage()

    if request.method == "POST":
        form = JoinTripForm(request.POST)
        if form.is_valid():
            trip_email = form.cleaned_data.get('email')
            if JoinTrip.objects.filter(email=trip_email).exists():
                messages.info(request, f"Email already exitst.")
        else:
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')

            # mail to personal email
            msg["Subject"] = f"{name} wants to join the trip."
            msg["From"] = settings.EMAIL_HOST_USER
            msg["To"] = settings.EMAIL_HOST_USER
            msg.set_content(
                f"More details below \n 1.Email: {email}\n2.Phone: {phone}")
            hml = f"""
            <!Doctype html>
            <html>
            <body>
            <h1 style='font-style:italic;'>{name} wants to join the trip.</h1>
            <p style='color:SlateGray;'> Name: {name} </p>
            <p style='color:SlateGray;'>Email: {email}</p>
            <p style='color:SlateGray;'>Email: {phone}</p>
            </body>
            </html>
            </html>
            """
            msg.add_alternative(hml, subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
                smtp.send_message(msg)
            msg1["Subject"] = "Thank you."
            msg1["From"] = settings.EMAIL_HOST_USER
            msg1["To"] = email
            msg1.set_content(
                f"Orgeon of stars is so delighted that you have decided to join our trip, saving lives and helping the vulnerable children is our top priority and we are happy that you've made it yours too.We will let you know of any other information before we embark on this journey.Stay blessed.")
            hml = f"""
            <!Doctype html>
            <html>
            <body>
            <h1 style='font-style:italic;'>Thank you for joining our trip.</h1>
            <p style='color:SlateGray;'>Orgeon of stars is so delighted that you have decided to join our trip, saving lives and helping the vulnerable children is our top priority and we are happy that you've made it yours too.We will let you know of any other information before we embark on this journey.Stay blessed."</p>
            <p style='color:SlateGray;'>ORgeonofstars</p>
            </body>
            </html>
            </html>
            """
            msg1.add_alternative(hml, subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(settings.EMAIL_HOST_USER,
                           settings.EMAIL_HOST_PASSWORD)
                smtp.send_message(msg1)
                messages.success(
                    request, f"Thank you for joining us on this trip.")
                return redirect('events')

    else:
        form = JoinTripForm()

    context = {
        'form': form
    }

    return render(request, "blog/jointrip_form.html", context)


def become_partner(request):
    msg1 = EmailMessage()
    msg = EmailMessage()
    if request.method == "POST":
        form = PartnershipForm(request.POST)
        if form.is_valid():
            partner_email = form.cleaned_data.get('email')
            if Partnership.objects.filter(email=partner_email).exists():
                messages.info(
                    request, f"A partner with the same email already exits.")

            else:
                form.save()
                name = form.cleaned_data.get('name')
                email = form.cleaned_data.get('email')
                phone = form.cleaned_data.get('phone')

                msg1["Subject"] = "Thank you for your partnership"
                msg1["From"] = settings.EMAIL_HOST_USER
                msg1["To"] = partner_email
                msg1.set_content(
                    f"We are happy to see you and also work with you.We will contact you soon for additional information.Stay blessed.")
                hml = f"""
                <!Doctype html>
                <html>
                <body>
                <h1 style='font-style:italic;'>Thank you for your partnership.</h1>
                <p style='color:SlateGray;'>We are happy to see you and also work with you.We will contact you soon for additional information.Stay blessed.</p>
                <p style='color:SlateGray;'>ORgeonofstars</p>
                </body>
                </html>
                </html>
                """
                msg1.add_alternative(hml, subtype='html')
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(settings.EMAIL_HOST_USER,
                               settings.EMAIL_HOST_PASSWORD)
                    smtp.send_message(msg1)

                # mail to personal email

                msg["Subject"] = "Got new partner"
                msg["From"] = settings.EMAIL_HOST_USER
                msg["To"] = partner_email
                msg.set_content(
                    f"{name} wants to partner with Orgeon of stars.")
                hml = f"""
                <!Doctype html>
                <html>
                <body>
                <h1 style='font-style:italic;'>New Partnership.</h1>
                <p style='color:SlateGray;'>{name} wants to partner with Orgeon of stars.</p>
                <p style='color:SlateGray;'>Email: {email}</p>
                <p style='color:SlateGray;'>Email: {phone}</p>
                </body>
                </html>
                </html>
                """
                msg.add_alternative(hml, subtype='html')
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(settings.EMAIL_HOST_USER,
                               settings.EMAIL_HOST_PASSWORD)
                    smtp.send_message(msg)
                    messages.success(request, f"Thank you for joining us..")
                    return redirect('partners')
    else:
        form = PartnershipForm()

    context = {
        'form': form
    }

    return render(request, "blog/partnerform.html", context)


def partners(request):
    partners = Partnership.objects.all()

    context = {
        'partners': partners
    }

    return render(request, "blog/partners.html", context)


def donate(request):
    return render(request, "blog/donate.html")


class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = "blog/reports.html"
    context_object_name = "reports"
    ordering = ['-date_posted']
    paginate_by = 5


@login_required()
def report_detail(request, id):
    if LoginCode.objects.filter(user=request.user).exists():
        report = get_object_or_404(Report, id=id)
        hasRead = False
        if report:
            if not report.has_read.filter(id=request.user.id).exists():
                report.has_read.add(request.user)
                hasRead = True
        reports = Report.objects.all().order_by('-date_posted')[:6]
        this_time = datetime.now()
        this_min = this_time.minute
        if this_min == CAN_STAY_LOGGED_IN1 or this_min == CAN_STAY_LOGGED_IN2 or this_min == CAN_STAY_LOGGED_IN3 or this_min == CAN_STAY_LOGGED_IN4:
            return redirect('logout')
    else:
        messages.info(request, f"You were logged out")
        return redirect('login')

    context = {
        'report': report,
        'hasread': hasRead,
        'reports': reports
    }

    return render(request, "blog/report_detail.html", context)


@login_required()
def create_report(request):
    if LoginCode.objects.filter(user=request.user).exists():
        if request.method == "POST":
            form = ReportForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                report = form.cleaned_data.get('report')
                Report.objects.create(
                    user=request.user, title=title, report=report)
                reporter = request.user

                subject = f"New report from {reporter}"
                message = f"Login to orgeon of stars in order to read message"
                from_email = settings.EMAIL_HOST_USER
                to_list = [settings.EMAIL_HOST_USER]
                send_mail(subject, message, from_email,
                          to_list, fail_silently=True)
                messages.success(
                    request, f"Report '{title}' successfullly created.")
                return redirect('reports')

        else:
            form = ReportForm()
    else:
        messages.info(request, f"You were logged out")
        return redirect('login')

    context = {
        'form': form
    }

    return render(request, "blog/create_report.html", context)


@login_required()
def employees(request):
    if LoginCode.objects.filter(user=request.user).exists():
        employees = Profile.objects.filter(verified=True)
        this_time = datetime.now()
        this_min = this_time.minute
        if this_min == CAN_STAY_LOGGED_IN1 or this_min == CAN_STAY_LOGGED_IN2 or this_min == CAN_STAY_LOGGED_IN3 or this_min == CAN_STAY_LOGGED_IN4:
            return redirect('logout')
    else:
        messages.info(request, f"You were logged out")
        return redirect('login')
    context = {
        'employees': employees,
    }

    return render(request, "blog/employees.html", context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'message', 'poster', 'need_replies']
    success_url = '/main'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']


@login_required()
def post_detail(request, id):
    if LoginCode.objects.filter(user=request.user).exists():
        hasRead = False
        post = get_object_or_404(Post, id=id)

        if post:
            post.views += 1
            post.save()
            if not post.has_read.filter(id=request.user.id).exists():
                post.has_read.add(request.user)
                hasRead = True

        comments = Comments.objects.filter(post=post).order_by('-date_posted')

        if request.method == "POST":
            form = CommentsForm(request.POST)
            if form.is_valid():
                comment_content = request.POST.get('reply')
                comment = Comments.objects.create(post=post, user=request.user, reply=comment_content)
                comment.save()

        this_time = datetime.now()
        this_min = this_time.minute
        if this_min == CAN_STAY_LOGGED_IN1 or this_min == CAN_STAY_LOGGED_IN2 or this_min == CAN_STAY_LOGGED_IN3 or this_min == CAN_STAY_LOGGED_IN4:
            return redirect('logout')

        else:
            form = CommentsForm()
    else:
        messages.info(request, f"You were logged out")
        return redirect('login')

    context = {
        "post": post,
        'form': form,
        'comments': comments,
        'hasRead': hasRead
    }

    if request.is_ajax():
        html = render_to_string("blog/comment_form.html",
                                context, request=request)
        return JsonResponse({"form": html})
    return render(request, "blog/post_detail.html", context)


@login_required()
def main(request):
    if LoginCode.objects.filter(user=request.user).exists():
        on_line_users = Online_user.objects.all()
        v_users = []
        users = User.objects.exclude(id=request.user.id)
        for i in users:
            if i.profile.verified == True:
                v_users.append(i)
        reports = Report.objects.all().order_by('-date_posted')[:6]
        posts = Post.objects.all().order_by('-date_posted')[:6]
        td = date.today()
        tt = timezone.now()
        ntt = tt.time
        current_events = Events.objects.filter(date_of_event=td)
        this_time = datetime.now()
        this_min = this_time.minute
        if this_min == CAN_STAY_LOGGED_IN1 or this_min == CAN_STAY_LOGGED_IN2 or this_min == CAN_STAY_LOGGED_IN3 or this_min == CAN_STAY_LOGGED_IN4:
            return redirect('logout')
    else:
        # messages.info(request, f"You were logged out")
        return redirect('login')
    context = {
        'users': on_line_users,
        "chat": v_users,
        'reports': reports,
        'posts': posts,
        'current_events': current_events,
        # "last_message": last_message
    }

    return render(request, "blog/main.html", context)


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Events
    fields = ['theme', 'venue', 'date_of_event',
              'event_poster', 'description_of_event']
    success_url = '/events'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Events


@login_required()
def user_activities(request):
    if LoginCode.objects.filter(user=request.user).exists():
        users = Profile.objects.filter(verified=True).count()
        students = Student.objects.all().count()
        grade_school_students = School.objects.filter(school="GradeSchool")
        pre_school_students = School.objects.filter(school="PreSchool")
        kindergarten_students = School.objects.filter(school="Kindergarten")
        volunteers = Volunteer.objects.all().count()
        partners = Partnership.objects.all().count()
        subscribers = NewsLetter.objects.all().count()
        myclients = ClientInfoProgress.objects.all().count()
        for i in grade_school_students:
            print(i.user.email)
        

        this_time = datetime.now()
        this_min = this_time.minute
        if this_min == CAN_STAY_LOGGED_IN1 or this_min == CAN_STAY_LOGGED_IN2 or this_min == CAN_STAY_LOGGED_IN3 or this_min == CAN_STAY_LOGGED_IN4:
            return redirect('logout')
    else:
        messages.info(request, f"You were logged out")
        return redirect('login')

    context = {
        "users": users,
        "volunteers": volunteers,
        "partners": partners,
        "myclients": myclients,
        "subscribers": subscribers,
        "students": students,
        "grade_school_students": grade_school_students,
        "pre_school_students": pre_school_students,
        "kindergarten_students": kindergarten_students,
    }

    if request.is_ajax():
        return HttpResponse(context)

    return render(request, "blog/activities.html", context)


def gallery(request):
    gallery = Gallery.objects.all().order_by('-date_posted')
    context = {
        "gallery": gallery
    }
    return render(request, "blog/gallery.html", context)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            uname = request.POST['username']
            upassword = request.POST['password']
            user = authenticate(username=uname, password=upassword)
            if user is not None:
                login(request, user)
                if not user.profile.verified:
                    return redirect('schoolhome')
                if not LoginCode.objects.filter(user=user).exists():
                    LoginCode.objects.create(user=user)
                if not Online_user.objects.filter(user=user).exists():
                    Online_user.objects.create(user=user)
                # messages.success(request, f"login success")
                return redirect('main')
                # Redirect to a success page.
            else:
                messages.info(request, f"invalid username or password")
        else:
            messages.info(request, f"invalid information given")
    else:
        form = AuthenticationForm()

    context = {
        "form": form
    }

    return render(request, "users/login.html", context)


@login_required()
def logout(request):
    try:
        ul = LoginCode.objects.filter(user=request.user)
        on_user = Online_user.objects.filter(user=request.user)

        if ul:
            ul.delete()
        if on_user:
            on_user.delete()
        del request.session['username']
    except:
        pass

    return render(request, "blog/logout.html")


@login_required
def all_users(request):
    users = User.objects.exclude(id=request.user.id)

    context = {
        "users": users,
    }

    return render(request, "blog/users-direct.html", context)


@login_required
def user_detail(request, username):
    msg = EmailMessage()
    deuser = get_object_or_404(User, username=username)
    deuser_email = deuser.email
    users = User.objects.exclude(id=request.user.id)
    chatid = deuser.id * request.user.id
    chat = Message.objects.filter(chat_id=chatid)
    mychats = Message.objects.all().filter(chat_id=chatid).filter(sender=request.user).filter(receiver=deuser).order_by(
        'message')

    if request.method == "POST":
        form = Message_Form(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get('message')
            if not Message.objects.filter(chat_id=chatid).exists():
                Message.objects.create(chat_id=chatid, sender=request.user, receiver=deuser, message=message)
            else:
                Message.objects.create(chat_id=chatid, sender=request.user, receiver=deuser, message=message)
            # mail to personal email

            msg["Subject"] = f"Got new messages from {request.user}"
            msg["From"] = settings.EMAIL_HOST_USER
            msg["To"] = deuser_email
            msg.set_content(f"{request.user} has sent a private message to you,login to view and reply.")
            hml = f"""
            <!Doctype html>
            <html>
            <body>
            <h1 style='font-style:italic;'>Got new messages from {request.user}.</h1>
            <p style='color:SlateGray;'>{request.user} has sent a private message to you,login to view and reply.</p>
            </body>
            </html>
            </html>
            """
            msg.add_alternative(hml, subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                smtp.send_message(msg)
    else:
        form = Message_Form()

    context = {
        "form": form,
        "deuser": deuser,
        "chat": chat,
        "users": users,
        "mychats": mychats
    }
    if request.is_ajax():
        msg = render_to_string("blog/umessages.html", context, request=request)
        return JsonResponse({
            "form": msg
        })

    return render(request, "blog/user_direct_detail.html", context)


@login_required
def group_chat(request):
    if LoginCode.objects.filter(user=request.user).exists():
        all_messages = MessageD.objects.all().order_by('date_sent')
        users = User.objects.exclude(id=request.user.id)
        on_users = Online_user.objects.all()
        if request.method == "POST":
            form = MessageD_Form(request.POST)
            if form.is_valid():
                sender = request.user
                message = form.cleaned_data.get('message')
                MessageD.objects.create(sender=sender, message=message)

        else:
            form = MessageD_Form()

        this_time = datetime.now()
        this_min = this_time.minute
        if this_min == CAN_STAY_LOGGED_IN1 or this_min == CAN_STAY_LOGGED_IN2 or this_min == CAN_STAY_LOGGED_IN3 or this_min == CAN_STAY_LOGGED_IN4:
            return redirect('logout')
    else:
        messages.info(request, f"You were logged out")
        return redirect('login')

    context = {
        "form": form,
        "users": users,
        "all_messages": all_messages,
        "on_users": on_users
    }

    if request.is_ajax():
        msg_chat = render_to_string("blog/groupchat.html", context, request=request)
        return JsonResponse({
            "form": msg_chat,
        })

    return render(request, "blog/gchat.html", context)


def contact_us(request):
    msg = EmailMessage()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')
            ContactUs.objects.create(name=name, email=email, phone=phone, message=message)
            msg["Subject"] = f"Message from {name}"
            msg["From"] = settings.EMAIL_HOST_USER
            msg["To"] = "help@orgeonofstars.org"
            msg.set_content(f"{message}")
            hml = f"""
                <!Doctype html>
                <html>
                <body>
                <h1 style='font-style:italic;'>{name} sent an enquiry to you.</h1>
                <p style='color:SlateGray;'>{message}</p>
                <p style='color:SlateGray;'>{email}</p>
                <p style='color:SlateGray;'>{phone}</p>
                </body>
                </html>
                </html>
                """
            msg.add_alternative(hml, subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                smtp.send_message(msg)
                messages.success(request, f'Message sent.')
                return redirect('home')

    else:
        form = ContactForm()

    context = {
        "form": form
    }

    return render(request, "blog/contact-us.html", context)


class ClientInfoListView(LoginRequiredMixin, ListView):
    model = ClientInfoProgress
    template_name = "blog/clientinfoprogress_list.html"
    context_object_name = "clients"
    ordering = ['-date_issued']


@login_required
def client_detail(request, id):
    client = get_object_or_404(ClientInfoProgress, id=id)

    context = {
        "client": client
    }

    return render(request, "blog/client_detail.html", context)


class ClientInfoCreateView(LoginRequiredMixin, CreateView):
    model = ClientInfoProgress
    fields = ['care_plan', 'assessment_officer', 'name', 'age', 'email', 'phone', 'emergency_phone', 'gender',
              'client_image', 'next_of_kin', 'issue', 'progress', 'assessment_phase_details',
              'development_phase_details', 'planning_phase_details', 'implementation_phase_details',
              'evaluation_phase_details', 'star_phase_details']
    success_url = '/clients'

    def form_valid(self, form):
        form.instance.assessment_officer = self.request.user
        return super().form_valid(form)


class ClientInfoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ClientInfoProgress
    fields = ['care_plan', 'assessment_officer', 'name', 'age', 'email', 'phone', 'emergency_phone', 'gender',
              'client_image', 'next_of_kin', 'issue', 'progress', 'assessment_phase_details',
              'development_phase_details', 'planning_phase_details', 'implementation_phase_details',
              'evaluation_phase_details', 'star_phase_details']
    success_url = '/clients'

    def form_valid(self, form):
        form.instance.assessment_officer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        client = self.get_object()
        if self.request.user == client.assessment_officer:
            return True
        else:
            return False


class ClientInfoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ClientInfoProgress
    success_url = '/clients'

    def test_func(self):
        client = self.get_object()
        if self.request.user == client.assessment_officer:
            return True
        else:
            return False
