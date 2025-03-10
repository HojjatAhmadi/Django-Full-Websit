from django import forms
from .models import Products, Category


class SearchForm(forms.Form):
    class Meta:
        model = Products
        fields = ['name']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control me-2', 'type': "search"}))


class CategorySearchForm(forms.Form):
    class Meta:
        model = Category
        fields = ['name']

    name = forms.CheckboxInput(attrs={'class': 'btn-check'})
