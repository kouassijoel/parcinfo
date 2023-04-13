from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from . models import *

from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UserAdminCreationForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Passwords don't match")
        return password1

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
class UserAdminChangeForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'

class AttributionsForm(forms.ModelForm):

    class Meta:
        model = Attribution
        fields = '__all__'
    password = ReadOnlyPasswordHashField()


class RestitutionAdminForm(forms.ModelForm):
    materiel = forms.ModelMultipleChoiceField(
        queryset=Materiel.objects.all(),
        widget=FilteredSelectMultiple(verbose_name='materiel', is_stacked=False))

    class Meta:
        model = Restitution
        fields = "__all__"
