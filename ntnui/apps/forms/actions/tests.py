from django.test import TestCase
from forms.models import AbstractFormModel
from forms.models import CoachFormModel
from .action_abstract_class import Action
from database.models import UserModel
from .notify import *
from .actions import *

email_data = {
            "subject": "test",
            "body": "test",
            "url_template": "test{}/{}",
            "get_emails_from_form": emails_notify_signers,
        }


class ActionsTestCase(TestCase):
    def setUp(self):
        self.form = AbstractFormModel.objects.create()
        self.form.current_action = 0
        self.form.actions = ["notify_signers"]
        self.form.save()

        self.actions = Actions(self.form)

    def test_actions(self):
        """Test status"""
        status = self.actions.status()

        self.assertEqual(status, "Send mail til signerere")

class ActionTestCase(TestCase):
    def setUp(self):
        self.action = Action()

    def test_action_abstract(self):
        """run and check do"""
        self.action.do()


        self.assertTrue(callable(self.action.do))

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


