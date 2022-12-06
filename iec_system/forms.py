from django import forms
from .models import IecMaterial

class IecMaterialForm(forms.ModelForm):
    class Meta:
        model=IecMaterial
        fields='__all__'
