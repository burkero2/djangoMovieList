from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    # Meta class gives the form some information about itself
    class Meta:
        # What is Item here?
        model = Item
        fields = ['name', 'done']