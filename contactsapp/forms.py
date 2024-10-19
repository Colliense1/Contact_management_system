from os import name
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
        widgets = {
            'address': forms.TextInput(attrs={'size': '100'}),
        }

        # purpose of this method the current form data has changed compared to the initial data when the form was rendered.
        def has_changed(self):
            return any(field.widget.value_from_datadict(self.data, None, name) != initial for field, initial in zip(self, self.initial))


class ContactSearchForm(forms.Form):
    query = forms.CharField(label='Search Contacts', max_length=100)

