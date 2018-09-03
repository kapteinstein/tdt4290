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


def get_group_member_info(group):
    members = get_member_list(group)
    invitations = get_member_invitations(group)
    requests = get_member_requests(group)

    return {
        'members': members,
        'requests': requests,
        'invitations': invitations
    }


def get_member_role(user, group):
    ''' Get the role of <user> in <group>'''
    if user not in group:
        return None

    return group.board.get_role(user)


def get_member_list(group):
    ''' Get a list of all the members in a group '''
    return group.members.filter()


def get_member_invitations(group):
    ''' Get a list of all pending invitations '''
    return group.invitations.all()


def get_member_requests(group):
    ''' Get a list of all pending requests '''
    return group.requests.all()
