from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from management.utils import group_decorators
from api.utils.json import JSONView
from database.models import GroupModel
from database.models import UserModel
from database.models import GroupInvitationModel

membership_decorators = [login_required, group_decorators.is_member]


@method_decorator(login_required, name='dispatch')
class GroupMembers(JSONView):
    ''' Returns an html template containing all groups based on membership of the active user'''

    def get(self, request):
        slug = request.GET.get('slug')

        return self.render_to_response(slug)

    def get_data(self, slug):
        ''' Implement the get_data method from the JSONResponse Mixin '''
        group = GroupModel.objects.get(slug=slug)

        # Return a dictionary to be serialized containing the given fields
        members = list(group.members.filter().values(
            'ntnui_no', 'first_name', 'last_name', 'email', 'gender', 'phone_no'))

        return {group.name: members}


@method_decorator(login_required, name='dispatch')
class InviteUser(JSONView):
    ''' Returns an html template containing all groups based on membership of the active user'''

    def get(self, request):
        return self.render_to_response(context=request.GET)

    def get_data(self, context):
        ''' Implement the get_data method from the JSONResponse Mixin '''
        email = context.get('email') or ''
        slug = context.get('slug') or ''

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return {'message': 'UserDoesNotExist'}

        try:
            group = GroupModel.objects.get(slug=slug)
        except GroupModel.DoesNotExist:
            return {'message': 'GroupDoesNotExist'}

        invitation = GroupInvitationModel(
            member=user, group=group)

        try:
            invitation.save()
        except ValidationError:
            return {'message': 'UserAlreadyInGroup'}

        return {'message': 'InvitationSent'}
