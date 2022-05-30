from django import forms

class SMTPForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput())
    context = forms.CharField(widget=forms.Textarea())