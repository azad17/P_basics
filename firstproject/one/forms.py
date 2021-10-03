from django.db.models.base import Model
from django.db.models.fields import DateField
from django import forms
from django.forms import ModelForm, fields
from .models import Books

class DateInput(forms.DateInput):
    input_type = 'date'

class BooksForm (ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        widgets = {
            'pub_date':DateInput(),
        }
