from django import template
from database.models import MembershipModel
from datetime import timedelta, datetime
from management.utils import time_utils

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


@register.filter
def time_since(time):
    ''' Return a formatted string of elapsed time since <time>'''
    # Get the current time and add the tzinfo cause python...
    nozone_time = time.replace(tzinfo=None)

    return time_utils.humanize_time_difference(datetime.now(), nozone_time)
