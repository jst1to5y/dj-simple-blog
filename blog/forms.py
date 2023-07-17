from django import forms
from .models import Post

class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        
        # Get all fields from model
        # fields = '__all__'
        
        # Get choosen fields from model
        # fields = ['title', 'content']

        # Get Everything except
        exclude = ('author', )