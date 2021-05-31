from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm , forms

class UserRegistrationForm(UserCreationForm):
    first_name=forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

class Meta:
    model=User
    fields=[
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',
    ]


class ProfileUpdateForm(forms.ModelForm):
    profile_picture=forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = [
            'profile_picture',

        ]


class UserUpdateForm(forms.ModelForm):
    username=forms.CharField(max_length=20,required=False)
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    email = forms.CharField(max_length=30, required=False)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',

        ]

class RegistrationProfileForm(forms.ModelForm):
    user_type_choices=[('admin','Admin'),('customer','Customer')]
    #user_type=forms.CharField(forms.Select(choices=user_type_choices))
    class Meta:
        model = UserProfile
        fields = [
            'user_type',


        ]