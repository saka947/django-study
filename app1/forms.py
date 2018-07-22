from django import forms


class UploadFileForm(forms.Form):
    user = forms.CharField(max_length=50)
    file = forms.FileField()