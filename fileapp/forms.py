from django import forms
from .models import UploadedFile

class FileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'description']