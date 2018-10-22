from django.db import models
from django import forms

"""
From text is shown before a signee fills out a form.
When a form is instantiated, it saves the highest primary key of a form text with the same slug.
This makes it possible to change the form text for future signees, while
already signed forms will still be associated with the text that was present during signing.
"""

class FormTextModel(models.Model):

    form_slug = models.CharField(max_length=200)
    form_text_content = models.TextField()

    def get_form_name(self):
        return self.form_slug

    def get_form_(self):
        return self.form_text_content
