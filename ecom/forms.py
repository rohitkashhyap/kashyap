from django import forms
from ecom.models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name','image']