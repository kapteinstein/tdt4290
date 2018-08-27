from django.shortcuts import get_object_or_404
from database.models import GroupModel, RoleModel, BoardModel


def get_group_info(request, slug):
    user = request.user
    group = get_object_or_404(GroupModel, slug=slug)

    # TODO: Implement a request object
    return {
        'group': group,
        'role': get_member_role(user, group),
        'board': group.board,
        'meta': group.meta,
        'media': group.media,
    }


def get_member_role(user, group):
    ''' Get the role of <user> in <group>'''
    if user not in group:
        return None

    return group.board.get_role(user)
