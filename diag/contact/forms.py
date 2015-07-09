from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Your Email Address'})) #received email address that could be contacted with
    guest_name = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Your Name'})) #name of the guy
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'})) #subject of the contact info
    context = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Message'})) #receives the content of contact

