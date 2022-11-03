from django import forms 
from .models import Reviw

class ProudctReviewFrom(forms.ModelForm):
    class Meta:
        model = Reviw
        fields = ['commnt','rate']