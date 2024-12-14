from django import forms

class ContactForm(forms.Form):
      names = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':"Your name"}))
      email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'Your email', "type":"email"}))
      message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your message'}))