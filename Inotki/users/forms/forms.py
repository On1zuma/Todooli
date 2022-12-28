from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django.views.generic import FormView
from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models.users import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def update(self):
        pass


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']


class UserProfileForm(forms.ModelForm):

    login_form = ProfileUpdateForm()
    signup_form = UserUpdateForm()
