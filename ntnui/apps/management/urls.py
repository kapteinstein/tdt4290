from django.urls import include, path
from .views import *

urlpatterns = [
    # TEMPORARY PATH

    # Group paths
    path('home/', group.GroupList.as_view(), name='home'),
    path('groups/', group.GroupList.as_view(), name='group-list'),
    path('<slug:slug>/', group.GroupHome.as_view(), name='group-home'),
    path('<slug:slug>/members', group.GroupMembers.as_view(), name='group-members'),
    path('<slug:slug>/settings', group.GroupHome.as_view(), name='group-settings'),

    # User paths
    path('user/settings', user.UserSettings.as_view(), name='user-settings')
]
