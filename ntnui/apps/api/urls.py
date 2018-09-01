from django.urls import path
from api.resources import group
from api.resources import validator

''' Include URL Patterns '''
urlpatterns = [
    path('members/<slug:slug>', group.GroupMembers.as_view()),
    path('validate/usernotingroup/<str:email>&<slug:slug>',
         validator.UserNotInGroup.as_view())
]
