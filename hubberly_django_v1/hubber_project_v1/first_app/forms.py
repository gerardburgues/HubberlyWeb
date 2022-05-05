from django import forms
from django.contrib.auth.models import User
from first_app.models import Contact

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User

        fields = ('username','first_name', 'email', 'password')
        help_texts = {
            'username': None,

        }

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ['name','email','message',]