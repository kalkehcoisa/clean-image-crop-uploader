from django.db import models

# Create your models here.

from django import forms
from pycicu.widgets import pycicuUploaderInput
from example.settings import MEDIA_ROOT

class testModel (models.Model):
    image = models.ImageField(verbose_name="Main image", null=True, blank=True, upload_to=MEDIA_ROOT, max_length=300)

class freeCrop(forms.ModelForm):
    class Meta:
        model = testModel
        pycicuOptions = {
            'ratioWidth': '', #if image need to have fix-width ratio
            'ratioHeight':'', #if image need to have fix-height ratio
            'sizeWarning': 'False', #if True the crop selection have to respect minimal ratio size defined above.
        }
        widgets = {
            'image': pycicuUploaderInput(options=pycicuOptions)
        }

class fixedRatioCrop(forms.ModelForm):
    class Meta:
        model = testModel
        pycicuOptions = {
            'ratioWidth': '800', #if image need to have fix-width ratio
            'ratioHeight': '600', #if image need to have fix-height ratio
            'sizeWarning': 'False', #if True the crop selection have to respect minimal ratio size defined above.
        }
        widgets = {
            'image': pycicuUploaderInput(options=pycicuOptions)
        }

class warningSizeCrop(forms.ModelForm):
    class Meta:
        model = testModel
        pycicuOptions = {
            'ratioWidth': '100', #if image need to have fix-width ratio
            'ratioHeight': '50', #if image need to have fix-height ratio
            'sizeWarning': 'True', #if True the crop selection have to respect minimal ratio size defined above.
        }
        widgets = {
            'image': pycicuUploaderInput(options=pycicuOptions)
        }
