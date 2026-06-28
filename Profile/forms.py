from django import forms
from . models import Profile
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    name=forms.CharField(max_length=50,required=True)
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=['username','name','email']
    def clean(self):
        cleaned_data=super().clean()

        username=cleaned_data.get('username')
        email=cleaned_data.get('email')

        if username and email:
            if User.objects.filter(Q(email=email) and Q(email=email)).exists():
                if User.objects.filter(email=email).exists():
                    self.add_error('email','Email Already Registered')
                if User.objects.filter(username=username).exists():
                    self.add_error('username','Username Already Taken')
            return cleaned_data
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        common_class='form-control'

        for field in self.fields.values():
            field.widget.attrs.update({'class':common_class})

            field.help_text=None

class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['gender','phone']

    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        common_class='form-control'
        for field in self.fields.values():
            field.widget.attrs.update({'class':common_class})
            field.help_text=None