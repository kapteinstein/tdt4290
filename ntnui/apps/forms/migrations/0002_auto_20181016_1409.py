# Generated by Django 2.1 on 2018-10-16 12:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoachModel',
            new_name='CoachFormModel',
        ),
        migrations.RenameModel(
            old_name='TrusteeModel',
            new_name='TrusteeFormModel',
        ),
        migrations.AddField(
            model_name='abstractformmodel',
            name='current_action',
            field=models.IntegerField(null=True),
        ),
    ]
