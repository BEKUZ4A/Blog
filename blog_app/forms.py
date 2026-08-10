from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="Ismi")
    last_name = forms.CharField(max_length=150, required=False, label="Familiyasi")
    email = forms.EmailField(required=True, label="Email")
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'username': 'Foydalanuvchi nomi',
            'password1': 'Parol',
            'password2': 'Parolni tasdiqlang'
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Foydalanuvchi nomi")
    password = forms.CharField(widget=forms.PasswordInput, label="Parol")

class UserAccountForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=True, label="Ismi")
    last_name = forms.CharField(max_length=150, required=False, label="Familiyasi")
    email = forms.EmailField(required=True, label="Email")
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Foydalanuvchi nomi',
        }

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, label="Eski parol")
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="Yangi parol")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="Yangi parolni tasdiqlang")
