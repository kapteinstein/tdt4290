from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from management.utils import group_decorators, time_utils
from api.utils.json import JSONView
from database.models import GroupModel
from database.models import UserModel
from database.models import GroupInvitationModel

from time import sleep

membership_decorators = [login_required, group_decorators.is_member]


@method_decorator(login_required, name='dispatch')
class GroupMembers(JSONView):
    ''' Returns an html template containing all groups based on membership of the active user'''

    def get(self, request):
        return self.render_to_response(request.GET)

    def get_data(self, context):
        ''' Implement the get_data method from the JSONResponse Mixin '''
        slug = context.get('slug') or ''

        try:
            group = GroupModel.objects.get(slug=slug)
        except GroupModel.DoesNotExist:
            return {'message': 'GroupDoesNotExist'}

        # Return a dictionary to be serialized containing the given fields
        members = list(group.members.filter().values(
            'ntnui_no', 'first_name', 'last_name', 'email', 'gender', 'phone_no'))

        return {'message': members}


@method_decorator(login_required, name='dispatch')
class GroupInvites(JSONView):
    ''' Returns an html template containing all groups based on membership of the active user'''

    def get(self, request):
        return self.render_to_response(request.GET)

    def get_data(self, context):
        ''' Implement the get_data method from the JSONResponse Mixin '''
        slug = context.get('slug') or ''

        try:
            group = GroupModel.objects.get(slug=slug)
        except GroupModel.DoesNotExist:
            return {'message': 'GroupDoesNotExist'}

        # Filter the member values of the invitation objects
        invitations = list(group.invitations.filter().values(
            'member__pk', 'member__first_name', 'member__last_name', 'member__email', 'time'
        ))

        # Convert all the time elements to a readable format
        for invitation in invitations:
            invitation['time'] = time_utils.humanize_time_difference(
                invitation['time'])

        # Return all the invitation objects
        return {'message': invitations}


@method_decorator(login_required, name='dispatch')
class GroupRequests(JSONView):
    ''' Returns an html template containing all groups based on membership of the active user'''

    def get(self, request):
        return self.render_to_response(request.GET)

    def get_data(self, context):
        ''' Implement the get_data method from the JSONResponse Mixin '''
        slug = context.get('slug') or ''

        try:
            group = GroupModel.objects.get(slug=slug)
        except GroupModel.DoesNotExist:
            return {'message': 'GroupDoesNotExist'}

        # Filter the member values of the invitation objects
        requests = list(group.requests.filter().values(
            'member__pk', 'member__first_name', 'member__last_name', 'member__email', 'time'
        ))

        # Convert all the time elements to a readable format
        for request in requests:
            request['time'] = time_utils.humanize_time_difference(
                request['time'])

        sleep(3)  # TODO: Remove this after demo

        # Return all the invitation objects
        return {'message': requests}


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


@method_decorator(login_required, name='dispatch')
class UninviteUser(JSONView):
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

        try:
            invitation = GroupInvitationModel.objects.get(
                member=user, group=group)
        except GroupInvitationModel.DoesNotExist:
            return {'message': 'InvitationDoesNotExist'}

        try:
            invitation.delete()
        except ValidationError:
            return {'message': 'UserAlreadyInGroup'}

        return {'message': 'InvitationRevoked'}
