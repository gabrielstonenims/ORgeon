from django import forms
from django.contrib.auth.models import User
from .models import (Volunteer, JoinTrip, Partnership, NewsLetter,
                     Report, Post, Comments, Comments, NewsUpdate, MessageD, Message, ContactUs, ClientInfoProgress
                     )


class NewsUpdateForm(forms.ModelForm):
    class Meta:
        model = NewsUpdate
        fields = ['title', 'message']


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'profession','country','photo', 'phone', 'why_join_Orgeon','additional_message']


class JoinTripForm(forms.ModelForm):
    class Meta:
        model = JoinTrip
        fields = ['name', 'email', 'phone']


class PartnershipForm(forms.ModelForm):
    class Meta:
        model = Partnership
        fields = ['partnership', 'name', 'email', 'phone']


class NewsLetterForm(forms.ModelForm):
    email = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your working email'}))

    class Meta:
        model = NewsLetter
        fields = ['email']


class ReportForm(forms.ModelForm):
    title = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Report Title'}))
    report = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Report....', 'rows': '2', 'cols': '35', 'id': 'reportform', 'name': 'reportform'}))

    class Meta:
        model = Report
        fields = ['title', 'report']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'message', 'poster']


class CommentsForm(forms.ModelForm):
    reply = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'reply here....', 'rows': '3', 'cols': '35', 'id': 'commentform', 'name': 'commentform'}))

    class Meta:
        model = Comments
        fields = ['reply']


class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'password'}))

    # class Meta:
    #     model = User
    #     fields = ['username','password']


class MessageD_Form(forms.ModelForm):
    message = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'Message....', 'rows': '3', 'cols': '35', 'id': 'directmessage',
               'name': 'directmessage'}))

    class Meta:
        model = MessageD
        fields = ['message']


class Message_Form(forms.ModelForm):
    message = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'Message....', 'rows': '3', 'cols': '35', 'id': 'directmessage',
               'name': 'directmessage'}))

    class Meta:
        model = Message
        fields = ['message']


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'name'}))
    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'email'}))
    phone = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'phone'}))
    message = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'Message....', 'rows': '3', 'cols': '35', 'id': 'contact_message',
               'name': 'contact_message'}))

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone', 'message']


class ClientProgressUpdateForm(forms.ModelForm):
    name = forms.CharField(label='Clients name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'name'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'email'}))
    phone = forms.CharField(label='Phone', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'phone'}))

    emergency_phone = forms.CharField(label='Emergency Phone', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'emergency contact'}))
    next_of_kin = forms.CharField(label='Next of kin', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'next of kin'}), required=False)
    issue = forms.CharField(label='Issue', max_length=100, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'issue'}))
    progress = forms.Select()

    class Meta:
        model = ClientInfoProgress
        fields = ['name', 'email', 'phone', 'emergency_phone', 'next_of_kin', 'issue', 'progress']
