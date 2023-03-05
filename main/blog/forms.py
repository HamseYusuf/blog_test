from django import forms 
from .models import Post

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content'
        ]