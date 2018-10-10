from django.db import models
from django import forms


class FormTextModel(models.Model):

    form_name = models.CharField(max_length=200)
    form_text_content = models.TextField()

    def get_form_name(self):
        return self.form_name

    def get_form_(self):
        return self.form_text_content

class FormTextSaverForm(forms.ModelForm):
    class Meta:
        model = FormTextModel
        fields = ['form_name', 'form_text_content']