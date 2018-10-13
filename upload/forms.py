from django import forms
from memes.models import Type


class UploadForm(forms.Form):
    image = forms.FileField(required=False)
    transcribe = forms.CharField(widget=forms.Textarea)
    type = forms.ModelMultipleChoiceField(queryset=Type.objects, widget=forms.CheckboxSelectMultiple(), required=False)
    nsfw = forms.BooleanField(required=False)
