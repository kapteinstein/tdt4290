# Generated by Django 2.1 on 2018-10-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20181010_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='formtextmodel',
            name='form_text_version_number',
            field=models.IntegerField(default=0),
        ),
    ]