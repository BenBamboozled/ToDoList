
from django import forms 
from django.contrib.auth.models import User
from .models import Item

class AddTaskForm(forms.ModelForm):
    class META:
        model = Item
        fields=['task', 'date']
