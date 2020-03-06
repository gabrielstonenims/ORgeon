from django import forms
from .models import (Volunteer, 
JoinTrip, Partnership, NewsLetter,
 Report,Post,InstantMessage,Comments,Comments,NewsUpdate
 )


class NewsUpdateForm(forms.ModelForm):

    class Meta:
        model = NewsUpdate
        fields = ['title','message']



class VolunteerForm(forms.ModelForm):

    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'profession','phone', 'why_join_Orgeon']


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

class InstantMessageForm(forms.ModelForm):

    class Meta:
        model = InstantMessage
        fields = ['title','recipient','message_content']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','message','poster']


class CommentsForm(forms.ModelForm):
    reply = forms.CharField( widget=forms.Textarea(
        attrs={'placeholder': 'reply here....', 'rows': '3', 'cols': '35', 'id': 'commentform','name':'commentform'}))

    class Meta:
        model = Comments
        fields = ['reply']







