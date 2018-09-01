from django.forms import Form, CharField
from django.core.validators import validate_email
from database.models import GroupInvitationModel
from database.models import GroupModel


class GroupInvitationForm(Form):
    email = CharField(max_length=100, validators=[validate_email])

    def __init__(self, *args, **kwargs):
        self.group = kwargs.pop('group') if 'group' in kwargs else ''
        super(GroupInvitationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data['email']

        print(email, self.group)
