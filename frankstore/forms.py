from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Advert

class NewAdvertForm(forms.ModelForm):
  class Meta:
    model = Advert
    exclude = ['pub_date']  

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']