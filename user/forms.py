from django import forms
from user.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=10, min_length=8, label="Password", widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=10, min_length=8, label="Confirm Password", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['email','password']

    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
    #     password1 = self.cleaned_data.get("password1")
    #     if password and password1 and password != password1:
    #         raise ValidationError("Passwords don't match")
    #     return password1

    # def save(self, commit=True):
    #     user = User.objects.create_user(email=self.cleaned_data.get("email"), password=self.cleaned_data.get('password'))
    #     return user