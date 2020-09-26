from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product, Review


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['author', 'product']

