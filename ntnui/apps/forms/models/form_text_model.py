from django.db import models
from django import forms

"""
Form text is the document shown in InfoView and SignedFormView.
When a form is instantiated, it saves the highest primary key of a form text with the same slug.
This makes it possible to change the form text for future signees, while
already signed forms will still be associated with the text that was present during signing.

New form text instances should be added through the admin panel.
The form_slug should correspond to a respective string in FORM_TYPES in form_types.py
form_text_content is parsed as html when presented in views.
"""

class FormTextModel(models.Model):

    form_slug = models.CharField(max_length=200)
    form_text_content = models.TextField()

    def get_form_name(self):
        return self.form_slug

    def get_form_(self):
        return self.form_text_content
