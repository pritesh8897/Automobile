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