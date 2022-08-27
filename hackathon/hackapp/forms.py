from django import forms

class hackforms(forms.Form):
    excel_file=forms.FileField()