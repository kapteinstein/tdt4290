# Generated by Django 2.1 on 2018-10-22 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('database', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_completed', models.BooleanField(default=False)),
                ('form_created_time', models.DateTimeField(auto_now_add=True)),
                ('form_modified_time', models.DateTimeField(auto_now=True)),
                ('current_action', models.IntegerField(default=0, null=True)),
                ('meta_version', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='FormTextModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_slug', models.CharField(max_length=200)),
                ('form_text_content', models.TextField()),
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
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('forms.abstractformmodel',),
        ),
        migrations.AddField(
            model_name='abstractformmodel',
            name='form_approvers',
            field=models.ManyToManyField(blank=True, related_name='form_approvers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractformmodel',
            name='form_instantiator',
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
        migrations.AddField(
            model_name='abstractformmodel',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='database.GroupModel'),
        ),
        migrations.AddField(
            model_name='abstractformmodel',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_forms.abstractformmodel_set+', to='contenttypes.ContentType'),
        ),
    ]
