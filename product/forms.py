from django import forms
from .models import FastFood

class FastFoodForm(forms.ModelForm):
    class Meta:
        model = FastFood
        fields = '__all__'