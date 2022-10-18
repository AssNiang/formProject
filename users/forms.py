from django import forms
from .models import Professeur

class ProfesseurForm(forms.ModelForm):
    
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'example@ept.sn'}))
    contact_prof = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '+221 xx xxx xx xx'}))
    date_d_adhesion = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    class Meta:
        model = Professeur
        fields = "__all__"
