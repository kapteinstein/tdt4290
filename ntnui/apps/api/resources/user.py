from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from management.utils import group_decorators
from api.utils.json import JSONView
from database.models import UserModel

membership_decorators = [login_required, group_decorators.is_member]


@method_decorator(login_required, name='dispatch')
class User(JSONView):
    ''' Returns an html template containing a spesific user '''
    # TODO: Require board permissions to actually read a user's profile

    def get(self, request):
        return self.render_to_response(request.GET)

    def get_data(self, context):
        ''' Implement the get_data method from the JSONResponse Mixin '''
        user_id = context.get('user_id') or ''

        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return {'message': 'UserDoesNotExist'}

        # Return a dictionary to be serialized containing the given fields
        user = list(user.values(
            'ntnui_no', 'first_name', 'last_name', 'email', 'gender', 'phone_no'))

        return {'message': user}
