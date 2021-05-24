from django import forms
from django.db.models import fields
from .models import Write,Comment


class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = '__all__'
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['content']