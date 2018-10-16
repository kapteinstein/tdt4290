from django.db import models
from django import forms

class FormTextModel(models.Model):

    form_name = models.CharField(max_length=200)
    form_text_content = models.TextField()
    form_text_version_number = models.IntegerField(default=0)

    def get_form_name(self):
        return self.form_name

    def get_form_(self):
        return self.form_text_content

class FormTextSaverForm(forms.ModelForm):
        model = FormTextModel
        fields = ['form_name', 'form_text_content']