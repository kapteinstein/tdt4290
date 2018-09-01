from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from management.utils import group_decorators
from api.utils.json import JSONView
from database.models import GroupModel
from database.models import UserModel

membership_decorators = [login_required, group_decorators.is_member]


@method_decorator(login_required, name='dispatch')
class UserNotInGroup(JSONView):
    ''' Returns an html template containing all groups based on membership of the active user'''

    def get(self, request, email, slug):
        return self.render_to_response(context={
            'email': email,
            'slug': slug

        })

    def get_data(self, context):
        ''' Implement the get_data method from the JSONResponse Mixin '''
        email = context.get('email')
        slug = context.get('slug')

        user_exists = UserModel.objects.filter(email=email)
        user_in_group = GroupModel.objects.get(
            slug=slug).members.filter(email=email)

        if user_in_group:
            return {'status': 'userInGroup'}

        if user_exists:
            return {'status': 'userNotInGroup'}

        return {'status': 'userDoesNotExist'}
