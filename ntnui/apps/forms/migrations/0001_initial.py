# Generated by Django 2.1 on 2018-10-15 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('database', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CoachFormModel',
            fields=[
                ('abstractformmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='forms.AbstractFormModel')),
                ('position', models.IntegerField(choices=[(0, 'Trener'), (1, 'Oppmann'), (2, 'Instruktør'), (3, 'Hjelpetrener')], null=True)),
                ('start_date', models.DateField(null=True)),
                ('compensation', models.IntegerField(choices=[(0, 'ingen'), (1, 'treningskort'), (2, 'betalt reise'), (3, 'annet')], null=True)),
                ('compensation_comments', models.TextField(blank=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='database.GroupModel')),
            ],
            bases=('forms.abstractformmodel',),
        ),
        migrations.CreateModel(
            name='TrusteeFormModel',
            fields=[
                ('abstractformmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='forms.AbstractFormModel')),
            ],
            bases=('forms.abstractformmodel',),
        ),
        migrations.AddField(
            model_name='abstractformmodel',
            name='form_approvers',
            field=models.ManyToManyField(blank=True, related_name='form_approvers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractformmodel',
            name='form_instantiatior',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='form_instantiatior', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractformmodel',
            name='form_signatures',
            field=models.ManyToManyField(blank=True, related_name='form_signatures', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractformmodel',
            name='form_signers',
            field=models.ManyToManyField(related_name='form_signers', to=settings.AUTH_USER_MODEL),
        ),
    ]
