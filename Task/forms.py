from django import forms
from . models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'status']
        labels = {
            'name': 'Enter Task',
            'status': 'Select Status'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter task name'}),
            'status': forms.RadioSelect()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the blank "--------" option Django adds by default
        self.fields['status'].empty_label = None
        self.fields['status'].choices = Task.status_choices

        common_class = "form-control"
        for field in self.fields.values():
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs.update({'class': common_class})