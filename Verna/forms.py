from django import forms
from Verna.models import OwnerInformation,CarInformation

# ** for signup **
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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

# *** for creating signup form ******
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']