from django import forms
from django.forms import ModelForm

from .models import Product

""" class ProductForm(forms.Form):
    name = forms.CharField() """


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_description(self):
        data = self.cleaned_data.get("description")
        if len(data) < 4:
            raise forms.ValidationError("Not long enough")
        return data
