from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from management.utils import group_decorators
from api.utils.json import JSONView
from database.models import GroupModel
from database.models import UserModel

membership_decorators = [login_required, group_decorators.is_member]


@method_decorator(login_required, name='dispatch')
class GroupMembers(JSONView):
    ''' Returns an html template containing all groups based on membership of the active user'''

    def get(self, request, slug):
        return self.render_to_response(slug)

    def get_data(self, slug):
        ''' Implement the get_data method from the JSONResponse Mixin '''
        group = GroupModel.objects.get(slug=slug)

        # Return a dictionary to be serialized containing the given fields
        members = list(group.members.filter().values(
            'ntnui_no', 'first_name', 'last_name', 'email', 'gender', 'phone_no'))

        return {group.name: members}
