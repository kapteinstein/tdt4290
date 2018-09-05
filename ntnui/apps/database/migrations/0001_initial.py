# Generated by Django 2.1 on 2018-09-05 16:14

import database.models.group_media
import database.models.membership
import database.utils.user_manager
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('-', 'N/A')], default='-', max_length=10)),
                ('ntnui_no', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('customer_no', models.CharField(max_length=20, unique=True)),
                ('register_date', models.DateField(default=datetime.date.today)),
                ('card_no', models.CharField(max_length=50, null=True)),
                ('contract_no', models.IntegerField(null=True)),
                ('contract_expiry_date', models.DateField(null=True)),
                ('language', models.CharField(choices=[('no', 'Norwegian'), ('en', 'English')], default='no', max_length=5)),
                ('calling_code', models.IntegerField(null=True)),
                ('phone_no', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='e-mail')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', database.utils.user_manager.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('board_id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Boards',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='GroupInvitationModel',
            fields=[
                ('invitation_id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'Group Invitation Object',
                'verbose_name_plural': 'Group Invitation Objects',
            },
        ),
        migrations.CreateModel(
            name='GroupMediaModel',
            fields=[
                ('media_id', models.AutoField(primary_key=True, serialize=False)),
                ('cover', models.ImageField(default='cover/ntnui.png', upload_to=database.models.group_media.get_upload_cover)),
                ('logo', models.ImageField(default='logo/ntnui.svg', upload_to=database.models.group_media.get_upload_logo)),
            ],
            options={
                'verbose_name': 'Group Media',
                'verbose_name_plural': 'Group Media',
            },
        ),
        migrations.CreateModel(
            name='GroupMetaModel',
            fields=[
                ('meta_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=200)),
                ('language', models.CharField(choices=[('no', 'Norwegian'), ('en', 'English')], default='no', max_length=5)),
            ],
            options={
                'verbose_name': 'Group Metadata',
                'verbose_name_plural': 'Group Metadata',
            },
        ),
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('slug', models.SlugField(editable=False)),
                ('founding_date', models.DateField(default=datetime.date.today)),
                ('payment_key', models.CharField(blank=True, max_length=40, null=True)),
                ('newsletter_key', models.CharField(blank=True, max_length=40, null=True)),
                ('access', models.CharField(choices=[('O', 'Open'), ('C', 'Closed')], default='O', max_length=20)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='GroupRelationshipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_group', to='database.GroupModel')),
                ('parent_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_group', to='database.GroupModel')),
            ],
            options={
                'verbose_name': 'Group Relation',
                'verbose_name_plural': 'Group Relations',
            },
        ),
        migrations.CreateModel(
            name='GroupRequestModel',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='database.GroupModel')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Group Request Object',
                'verbose_name_plural': 'Group Request Objects',
            },
        ),
        migrations.CreateModel(
            name='MembershipModel',
            fields=[
                ('membership_no', models.AutoField(primary_key=True, serialize=False)),
                ('date_joined', models.DateField(default=datetime.date.today)),
                ('group_expiry', models.DateField(default=database.models.membership.one_year_from_today)),
                ('sports_license_expiry', models.DateField(blank=True, default=None, null=True)),
                ('sports_license_no', models.CharField(blank=True, max_length=40, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.GroupModel')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Membership',
                'verbose_name_plural': 'Memberships',
            },
        ),
        migrations.CreateModel(
            name='RoleModel',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('P', 'President/Leader'), ('VP', 'Vice President/Secondary Leader'), ('C', 'Cashier'), ('-', 'Member/Other')], default='-', max_length=40)),
                ('date_joined', models.DateField(default=datetime.date.today)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_set', to='database.BoardModel')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.AddField(
            model_name='groupmodel',
            name='members',
            field=models.ManyToManyField(through='database.MembershipModel', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupmodel',
            name='parent',
            field=models.ManyToManyField(blank=True, related_name='child', through='database.GroupRelationshipModel', to='database.GroupModel'),
        ),
        migrations.AddField(
            model_name='groupmetamodel',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meta', to='database.GroupModel'),
        ),
        migrations.AddField(
            model_name='groupmediamodel',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='database.GroupModel'),
        ),
        migrations.AddField(
            model_name='groupinvitationmodel',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='database.GroupModel'),
        ),
        migrations.AddField(
            model_name='groupinvitationmodel',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='membership',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.MembershipModel'),
        ),
        migrations.AddField(
            model_name='boardmodel',
            name='group',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='board', to='database.GroupModel'),
        ),
        migrations.AddField(
            model_name='boardmodel',
            name='predecessor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.BoardModel'),
        ),
    ]
