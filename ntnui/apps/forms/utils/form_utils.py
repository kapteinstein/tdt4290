from database.models import GroupModel, RoleModel

def is_authorized(user):
    is_authorized = False
    for group in GroupModel.objects.all():
        if user not in group:
            continue
        if group.board.get_role(user) == "President/Leader":
            is_authorized = True
    return is_authorized
    