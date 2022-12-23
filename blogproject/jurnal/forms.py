from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)
from .models import UserBase
class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, error_messages={'required': 'Incorrect email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput, help_text='Password has to be at least 8 characters and 1 digit')
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = UserBase
        fields = ('email',)
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']
    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['user_name'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'E-mail'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat Password'})
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))









