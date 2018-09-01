from django.urls import path
from api.resources import group

''' Include URL Patterns '''
urlpatterns = [
    path('members', group.GroupMembers.as_view()),
    path('invite-user',
         group.InviteUser.as_view())
]
