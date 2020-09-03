from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']

        widgets = {
            'content': forms.Textarea(attrs={'rows':'2', 'placeholder': 'write something'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Post your comment'})
        }
