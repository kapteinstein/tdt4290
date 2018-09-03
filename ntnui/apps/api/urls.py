from django.urls import path
from api.resources import group
from api.resources import user

''' Include URL Patterns '''
urlpatterns = [
    path('members', group.GroupMembers.as_view()),
    path('invitations', group.GroupInvites.as_view()),
    path('requests', group.GroupRequests.as_view()),
    path('invite-user',
         group.InviteUser.as_view()),
    path('uninvite-user',
         group.UninviteUser.as_view()),
    path('user', user.User.as_view())
]
