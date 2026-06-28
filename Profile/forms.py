from django import forms
from . models import Profile
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, label="First Name")
    last_name = forms.CharField(max_length=50, required=False, label="Last Name")
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if username and email:
            qs_email = User.objects.filter(email=email)
            qs_user = User.objects.filter(username=username)
            if self.instance.pk:
                qs_email = qs_email.exclude(pk=self.instance.pk)
                qs_user = qs_user.exclude(pk=self.instance.pk)
            if qs_email.exists():
                self.add_error('email', 'This email is already registered.')
            if qs_user.exists():
                self.add_error('username', 'This username is taken.')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None


class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'phone']
        widgets = {
            'gender': forms.Select(),
            'phone': forms.TextInput(attrs={'placeholder': 'e.g. 9800000000'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].choices = Profile.gender_choices
        for field in self.fields.values():
            field.help_text = None
