from django import forms
from . models import *



class UserAdminCreationForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'

class UserAdminChangeForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'

class AttributionsForm(forms.ModelForm):

    class Meta:
        model = Attribution
        fields = '__all__'
        
    