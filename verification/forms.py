from django import forms

class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number', max_length=15)
