from django.test import TestCase
from . import *

class AbstractFormModelTestCase(TestCase):

    def setUp(self):
      pass

    def create_form(self):
        return AbstractFormModel.objects.create()


    def test_form_creation(self):
        f = self.create_form()
        l = AbstractFormModel()
        self.assertEqual(f.getRequiredSignLevel(), 0)