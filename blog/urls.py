from django.urls import path

from . import views
from .views import Volunteers,VolunteerFormView,OurVolunteers
from .views import (PostCreateView, PostListView, EventCreateView, EventDetailView, ReportListView,
                    ClientInfoCreateView, ClientInfoListView, ClientInfoUpdateView, ClientInfoDeleteView)

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('success/', views.success_stories, name='success'),
    path('stories_of_need/', views.needy_stories, name='stories_of_need'),
    path('inspirational_stories/', views.inspirational_stories, name='inspirational_stories'),
    path('somevids/', views.some_videos, name='somevids'),
    path('volunteer/new/', VolunteerFormView.as_view(), name='volunteer_join'),
    path('volunteers/', Volunteers.as_view(), name='volunteers'),
    path('ourvolunteers/',OurVolunteers.as_view(),name='ourvolunteers'),
    path('events/', views.events, name='events'),
    path('join-trip/new/', views.join_trip, name='jointrip'),
    path('partner/new/', views.become_partner, name='become_a_partner'),
    path('partners/', views.partners, name='partners'),
    path('donate/', views.donate, name='donate'),
    path('reports/', ReportListView.as_view(), name='reports'),
    path('report/<int:id>/', views.report_detail, name='report_detail'),
    path('report/new/', views.create_report, name='create_report'),
    path('employees/', views.employees, name='employees'),
    path('notification/new/', PostCreateView.as_view(), name='post_new'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('main/', views.main, name='main'),
    path('newsletter/', views.news_letter, name='newsletter_create'),
    path('event/new/', EventCreateView.as_view(), name='event_new'),
    path('event/<int:pk>/', EventDetailView.as_view(), name="event_detail"),
    path('activities/', views.user_activities, name='activities'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout, name='logout'),
    path('direct/', views.all_users, name="allusers"),
    path('direct/<str:username>/', views.user_detail, name="userdetail"),
    path('chat/', views.group_chat, name="chat"),
    path("contact-us/", views.contact_us, name='contact'),
    path('clients/', ClientInfoListView.as_view(), name='clients'),
    path('clients/new/', ClientInfoCreateView.as_view(), name='clients_new'),
    path('client/<int:id>/', views.client_detail, name='client_detail'),
    path('client/<int:pk>/update/', ClientInfoUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientInfoDeleteView.as_view(), name='client_delete')
]
