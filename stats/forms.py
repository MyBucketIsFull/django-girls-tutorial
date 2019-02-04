from django import forms

class ExecuteForm(forms.Form):
    input = forms.CharField(label='Integers (separated with comma)', max_length=100)
