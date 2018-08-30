from django import template
from database.models import MembershipModel

register = template.Library()


@register.filter
def member_role(member, group):
    return group.board.get_role(member)


@register.filter
def member_joined(member, group):
    try:
        return MembershipModel.objects.get(member=member, group=group).date_joined
    except:
        return "N/A"
