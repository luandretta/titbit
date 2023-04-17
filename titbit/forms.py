from django import forms
from .models import Post


"""
Form to write a new post
Add bootstrap classes
"""
class PostForm(forms.ModelForm):
    body = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'placeholder': 'Share your titbit!',
                'class': 'form-control',
            }
        ),
        label='')

    class Meta:
        model = Post
        exclude = ('user', )

