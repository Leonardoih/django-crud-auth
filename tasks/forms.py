from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the title here",  # Placeholder text
                    "autofocus": True,  # Autofocus on this field
                    "required": True,  # Make title required
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter a detailed description",  # Placeholder text
                    "rows": 5,  # Adjust number of rows
                }
            ),
            "important": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
