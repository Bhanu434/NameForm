from django import forms

class NameForms(forms.Form):
    Sname=forms.CharField()
    Sage=forms.IntegerField()