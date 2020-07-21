from django import forms
from Verna.models import OwnerInformation,CarInformation

class OwnerInformationForm(forms.ModelForm):
    # email = forms.EmailField()
    class Meta:
        model = OwnerInformation
        fields =  '__all__'

class CarInformationForm(forms.ModelForm):
    class Meta:
        model = CarInformation
        fields = '__all__'

# ******* for creating contact form using Formview ********
class ContactForm(forms.Form):
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField()