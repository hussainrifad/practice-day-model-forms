from django import forms
from datetime import date
from . import models

class PersonalForm(forms.Form):
    name = forms.CharField(max_length=100)
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    phone = forms.CharField()
    email = forms.EmailField()
    birth_date = forms.DateField(initial=date.today(), widget=forms.DateInput(attrs={'type': 'date'}))
    location = forms.MultipleChoiceField(choices=[('dhaka', 'Dhaka'), ('khulna', 'Khulna'), ('rangpur', 'Rangpur')])
    # address = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[('dhaka', 'Dhaka'), ('khulna', 'Khulna'), ('rangpur', 'Rangpur')])
    school_education = forms.ChoiceField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),(8, 8), (9, 9), (10, 10) ])
    agree = forms.BooleanField()

class Artist(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'