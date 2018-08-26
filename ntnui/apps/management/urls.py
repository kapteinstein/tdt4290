from django.urls import include, path
from .views import *

urlpatterns = [
    # TEMPORARY PATH
    path('home/', group.group_list, name="home"),
    path('groups/', group.group_list, name="group-list"),
    path('<slug:slug>/', group.group_home, name="group-home")
]
