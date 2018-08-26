from django.test import TestCase
from datetime import date, timedelta
from data_storage.models import GroupModel


class GroupModelTestCase(TestCase):
    def setUp(self):
        GroupModel.objects.create(name="NTNUI Sprint")

    @staticmethod
    def get_group():
        return GroupModel.objects.get(name="NTNUI Sprint")

    def test_has_name(self):
        group = self.get_group()
        self.assertEqual(group.name, "NTNUI Sprint")

    def test_has_slug(self):
        group = self.get_group()
        self.assertEqual(group.slug, "ntnui-sprint")

    def test_default_founding_date(self):
        ''' The default founding date should be the object creation date '''
        group = self.get_group()
        self.assertEqual(group.founding_date, date.today())

    def test_changing_founding_date(self):
        ''' Ensure that we can also change the founding date '''
        group = self.get_group()
        yesterday = date.today() - timedelta(days=1)

        # Update the model
        group.founding_date = yesterday
        group.save()

        # Test to ensure the change took place
        self.assertEqual(group.founding_date, yesterday)
