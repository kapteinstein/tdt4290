# Generated by Django 2.1 on 2018-08-26 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20180826_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolemodel',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='database.BoardModel'),
        ),
        migrations.AlterField(
            model_name='rolemodel',
            name='member',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
