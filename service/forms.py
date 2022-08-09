from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Comment, Post
from django import forms

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