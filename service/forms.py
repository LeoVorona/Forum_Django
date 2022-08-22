from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Comment, Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        vidgets = {
            'title': forms.TextInput(attrs={'class':'form-label'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        vidgets = {
            'description': forms.Textarea(attrs={'class':'form-control'}),
            }

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']