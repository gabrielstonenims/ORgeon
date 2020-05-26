from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import School


class KidsSchoolRegister(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class KidsSchoolUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class KidsSchoolProfileUpdate(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school', 'grade', 'age', 'fullname', 'photo', 'name_of_parent_or_guardian', 'contact_number']

