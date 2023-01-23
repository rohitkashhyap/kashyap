from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    phone = forms.CharField(min_length=7, max_length=12, required=False,help_text="Phone No. is optional")
    email = forms.EmailField(max_length=50, required=True, help_text="Email will be required to contact you")
    message = forms.CharField(widget=forms.Textarea, required=True)


