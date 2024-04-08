from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'class-controls'}),
            "last_name": forms.TextInput(attrs={'class': 'class-controls'}),
            "mob_no": forms.NumberInput(attrs={'class': 'class-controls'})

        }