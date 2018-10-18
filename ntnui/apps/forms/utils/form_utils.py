from database.models import GroupModel, RoleModel

def is_authorized(user):
    is_authorized = False
    for group in GroupModel.objects.all():
        if user not in group:
            continue
        if group.board.get_role(user) == "President/Leader":
            is_authorized = True
    return is_authorized


def get_leader_groups(user):
    ''' Returns a list of groups where the user is "President/Leader" '''
    all_groups = GroupModel.objects.all()
    leader_of_groups = []
    for group in all_groups: 
        if user not in group: 
            continue
        elif group.board.get_role(user) == "President/Leader":
            leader_of_groups.append(group)
    return leader_of_groups


def is_group_leader(user, group):
    if group.board.get_role(user) == 'President/Leader':
        return True
    return False

