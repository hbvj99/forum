from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Discussion
        fields = ['title', 'content', 'category', 'tags', 'img']

        labels = {
            'title': 'Title',
            'content': 'Description',
            'category': 'Category',
            'tags': 'Tags (Optional)',
            'img': 'Optional (JPEG/PNG)'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter new discussion title'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Add keyword separate by comma (,)'}),
        }


class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['content']
        labels = {
            'content': '',
        }

