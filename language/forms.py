from django import forms 
from . import models 

class CreateLanguage(forms.ModelForm):
    class Meta:
        model = models.Language 
        fields = ["name", "nameInNativeScript", "description", "slug", "thumb"]