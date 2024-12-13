
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    email = forms.EmailField(label="Ваш email")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")

class MessageForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100, required=True)
    email = forms.EmailField(label="Ваш email", required=True)
    message = forms.CharField(label="Сообщение", widget=forms.Textarea, required=True)
