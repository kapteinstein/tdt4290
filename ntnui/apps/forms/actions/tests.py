from django.test import TestCase
from forms.models import AbstractFormModel
from database.models import UserModel
from .notify import *

email_data = {
            "subject": "test",
            "body": "test",
            "url_template": "test{}/{}",
            "get_emails_from_form": emails_notify_signers,
        }

class NotifyTestCase(TestCase):
    def setUp(self):
        form = AbstractFormModel.objects.create()
        user = UserModel.objects.create()
        user.email = "test@test.no"
        user.save()
        form.form_signers.add(user)
        form.save()


    def test_notify_function_creation(self):
        """Testing notify funciton creation"""

        func = notify(email_data)

        self.assertTrue(callable(func))


    def test_emails_notify_signers(self):
        "Testing emails extraction"
        form = AbstractFormModel.objects.get()
        emails = emails_notify_signers(form)
        self.assertEqual([emails[0]], ["test@test.no"])

    def test_notify_instantiation(self):
        "Testing emails extraction"
        form = AbstractFormModel.objects.get()

        func = notify(email_data)

        notifyInstance = func(form)


        self.assertTrue(callable(notifyInstance.do))

    def test_define_url(self):
        "Testing define _url function"
        slug = "slug"
        url_string = "test/{}/{}"
        private_key = 1

        string = define_url(slug, private_key, url_string)

        self.assertEqual(string, "test/slug/1")


