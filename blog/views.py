from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Volunteer, Events, JoinTrip, Partnership, NewsLetter, Report, InstantMessage,Post,Comments,NewsUpdate,Usermsg
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import pytz
from datetime import datetime,date,time,timedelta
from django.core.paginator import Paginator
from .forms import (VolunteerForm,
                    JoinTripForm,
                    PartnershipForm,
                    NewsLetterForm,
                    ReportForm,
                    PostForm,InstantMessageForm,CommentsForm,
                    NewsUpdateForm
                    )
from django.contrib.auth.models import User

from django.views.decorators.cache import cache_control


@login_required()
def news_letter(request):
    suscribed_users = NewsLetter.objects.all()
    print(suscribed_users)
    if request.method == "POST":
        form = NewsUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title').upper()
            update_message = form.cleaned_data.get('message')
            subject = title
            message = f"\n {update_message}"
            from_email = settings.EMAIL_HOST_USER
            to_list = suscribed_users
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            messages.success(request,f"News update messages sent successfully.")
            return redirect('newsletter_create')
    else:
        form = NewsUpdateForm()

    context = {
        "form": form
    }

    return render(request,"blog/newsletter.html",context)






def home(request):
    if request.method == "POST":
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if NewsLetter.objects.filter(email=email).exists():
                messages.info(request, "This email already exists.")
            else:
                form.save()
                subject = "Thank you for subcribing to our newsletter."
                message = f"We will send you all the necessary updates."
                from_email = settings.EMAIL_HOST_USER
                to_list = [email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
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


def volunteer_register(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            v_email = form.cleaned_data.get('email')
            if Volunteer.objects.filter(email=v_email).exists():
                messages.info(request, f"Volunteer with {v_email} already exist.")
            else:
                form.save()
                name = form.cleaned_data.get('name')
                # mail to personal email
                subject1 = f"{name} has just volunteered."
                message1 = f"{name} wishes to volunteer for Orgeon."
                from_email = settings.EMAIL_HOST_USER
                to_list = [settings.EMAIL_HOST_USER]
                send_mail(subject1, message1, from_email, to_list, fail_silently=True)
                # to user volunteering email
                subject = "Orgeon of Stars welcomes you."
                message = f"Thank you for volunteering with Orgeon of stars,in order to know more about \n you we will contact you soon,stay blessed."
                from_email = settings.EMAIL_HOST_USER
                to_list = [v_email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
                messages.success(request, f"Thank you for joining.")
                return redirect('volunteers')

    else:
        form = VolunteerForm()

    context = {
        'form': form
    }

    return render(request, "blog/volunteer_form.html", context)


class Volunteers(ListView):
    model = Volunteer
    template_name = 'blog/volunteers.html'
    context_object_name = 'volunteers'
    ordering = ['-date_volunteered']


def events(request):
    events = Events.objects.all().order_by('-date_posted')[:1]

    context = {
        'events': events
    }

    return render(request, "blog/events.html", context)


def join_trip(request):
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
            subject1 = f"{name} wants to join the trip."
            message1 = f"More details below \n 1.Email: {email}\n2.Phone: {phone}"
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER]
            send_mail(subject1, message1, from_email, to_list, fail_silently=True)

            subject = "Thank you."
            message = f"Orgeon of stars is so delighted that you have decided to join our trip,\n saving lives and helping the vulnerable children is our top priority and we are \n happy that you've made it yours too.\nWe will let you know of any other information before we embark on this journey.\nStay blessed."
            from_email = settings.EMAIL_HOST_USER
            to_list = [trip_email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            messages.success(request, f"Thank you for joining us on this trip.")

    else:
        form = JoinTripForm()

    context = {
        'form': form
    }

    return render(request, "blog/jointrip_form.html", context)


def become_partner(request):
    if request.method == "POST":
        form = PartnershipForm(request.POST)
        if form.is_valid():
            partner_email = form.cleaned_data.get('email')
            if Partnership.objects.filter(email=partner_email).exists():
                messages.info(request, f"A partner with the same email already exits.")

            else:
                form.save()
                name = form.cleaned_data.get('name')
                email = form.cleaned_data.get('email')
                phone = form.cleaned_data.get('phone')
                subject = "Thank you for your partnership"
                message = f"We are happy to see you and also work with you.We will contact you soon for additional information.Stay blessed."
                from_email = settings.EMAIL_HOST_USER
                to_list = [partner_email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)

                # mail to personal email
                subject1 = "Got new partner"
                message1 = f"{name} wants to partner with Orgeon of stars.\nMore details are below\n1.Email: {email}\n2.Phone: {phone}"
                from_email = settings.EMAIL_HOST_USER
                to_list = [settings.EMAIL_HOST_USER]
                send_mail(subject1, message1, from_email, to_list, fail_silently=True)
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


@login_required()
def reports(request):
    reports = Report.objects.all().order_by('-date_posted')

    context = {
        "reports": reports
    }

    return render(request, "blog/reports.html", context)


@login_required()
def report_detail(request, id):
    report = get_object_or_404(Report, id=id)
    reports = Report.objects.all().order_by('-date_posted')

    context = {
        'report': report,
        'reports': reports
    }

    return render(request, "blog/report_detail.html", context)


@login_required()
def create_report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            report = form.cleaned_data.get('report')
            Report.objects.create(user=request.user, title=title, report=report)
            reporter = request.user

            subject = f"New report from {reporter}"
            message = f"Login to orgeon of stars in order to view message"
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            messages.success(request, f"Report '{title}' successfullly created.")
            return redirect('reports')

    else:
        form = ReportForm()

    context = {
        'form': form
    }

    return render(request, "blog/create_report.html", context)


@login_required()
def employees(request):
    employees = User.objects.all()

    context = {
        'employees': employees
    }

    return render(request, "blog/employees.html", context)


@login_required()
def create_message(request):
    if request.method == "POST":
        form = InstantMessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            message_content = form.cleaned_data.get('message_content')
            recipient = form.cleaned_data.get('recipient')
            InstantMessage.objects.create(title=title,sender=request.user,recipient=recipient,message_content=message_content)
            return redirect('main')

    else:
        form = InstantMessageForm()

    context = {
        'form': form
    }
    return render(request,"blog/instantmessage_form.html",context)

@login_required()
def user_messages(request,username):
    logged_in_user = get_object_or_404(User, username=request.user.username)
    user_messages = InstantMessage.objects.filter(recipient=logged_in_user).order_by('-date_posted')
    unread_count = InstantMessage.objects.filter(recipient=logged_in_user, read=False).count
    
    context = {
        'user_messages': user_messages,
        'notification_count': unread_count,
    }

    return render(request, "blog/messages.html", context)

@login_required()
def instantmessage_detail(request,username,id):
    user = get_object_or_404(User,username= request.user.username)
    instant_message = get_object_or_404(InstantMessage,recipient=user,id=id)
    has_read = False
    if instant_message:
        instant_message.read = True
        has_read = True
        instant_message.save()

    context = {
        "instant_message": instant_message,
        'has_read': has_read
    }

    return render(request,"blog/instant_message_detail.html",context)


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','message','poster']
    success_url = '/main'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']



@login_required()
def post_detail(request,id):
    post = get_object_or_404(Post,id=id)

    if post:
        post.views += 1
        post.save()

    comments = Comments.objects.filter(post=post).order_by('-date_posted')

    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment_content = request.POST.get('comment_content')
            comment = Comments.objects.create(post=post,user=request.user,reply = comment_content)
            comment.save()

    else:
        form = CommentsForm()

    context = {
        "post": post,
        'form': form,
        'comments': comments
    }

    if request.is_ajax():
        html = render_to_string("blog/comment_form.html",context,request=request)
        return JsonResponse({"form": html})
    return render(request,"blog/post_detail.html",context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required()
def main(request):
    reports = Report.objects.all().order_by('-date_posted')[:6]
    posts = Post.objects.all().order_by('-date_posted')[:6]

    context = {
        'reports': reports,
        'posts': posts,
    }

    return render(request,"blog/main.html",context)

