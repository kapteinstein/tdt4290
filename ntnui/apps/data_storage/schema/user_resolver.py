from ..models import UserModel


def resolve_get_users(self, info, **kwargs):
    return UserModel.objects.all()
