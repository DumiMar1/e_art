from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


AuthUser = get_user_model()

class RegisterForm(UserCreationForm):

    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email']


class LoginForm(AuthenticationForm):

    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = AuthUser
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form=control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']