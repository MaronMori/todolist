from django import forms
from .models import ToDoList


class add_task(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ["task"]
