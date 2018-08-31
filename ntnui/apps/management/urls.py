from django.urls import include, path
from django.views.generic.base import RedirectView
from .views import *

urlpatterns = [
    # Group paths
    path('home/', group.GroupList.as_view(), name='home'),
    path('groups/', group.GroupList.as_view(), name='group-list'),

    # Redirect the home view to the about page using a 301
    path('<slug:slug>/', RedirectView.as_view(url='about',
                                              permanent=True), name='group-home'),
    path('<slug:slug>/about', group.GroupHome.as_view(), name='group-about'),
    path('<slug:slug>/members', group.GroupMembers.as_view(), name='group-members'),
    path('<slug:slug>/settings', group.GroupHome.as_view(), name='group-settings'),

    # User paths
    path('user/settings', user.UserSettings.as_view(), name='user-settings')
]
