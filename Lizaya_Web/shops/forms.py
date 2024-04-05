from django import forms
from django.forms.models import modelformset_factory
from .models import ProductFeatured

class ProductFeaturedForm(forms.ModelForm):
    class Meta:
        model = ProductFeatured
        fields  = [
            'product',
            'name',
            'text',
            'active',
        ]




