#to create a contact us form
from django import forms
class ContactForm(forms.Form):
    contact_name=forms.CharField(label='Enter Your Name',required=True)
    contact_email=forms.EmailField(label='Enter Your Email',required=True)
    content=forms.CharField(label='Your Message',required=True,widget=forms.Textarea)
