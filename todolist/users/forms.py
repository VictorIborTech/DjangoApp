from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]


# for profile update
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

    #     # Check if email is already in use!!
    #
    # def clean_email(self):
    #     data = self.cleaned_data['email']
    #     queryset = User.objects.exclude(id=self.instance.id).filter(email=data)
    #
    #     if queryset.exists():
    #         raise forms.ValidationError(' Email already in use.')
    #     return data


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','address','date_of_birth']



