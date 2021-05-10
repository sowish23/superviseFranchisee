from django.forms import ModelForm
from django import forms
from .models import UploadImgMenu

class UploadMenu(ModelForm):
    class Meta:
        model = UploadImgMenu
        fields = [ 'menu_no', 'image',]
        exclude = ('user_id',)