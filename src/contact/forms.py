from django import forms


class contactForm(forms.Form):
    name = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    comment = forms.CharField(required = True, widget = forms.Textarea, max_length=250, help_text = '250 characters max') 