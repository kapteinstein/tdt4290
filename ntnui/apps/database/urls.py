from django.urls import path, include
from django.contrib import admin
from django.contrib import admin

from graphene_django.views import GraphQLView

''' Configure Admin '''
admin.site.site_header = "NTNUI Admin"
admin.site.site_title = "NTNUI Site Admin"
admin.site.index_title = "Welcome to the NTNUI Admin Portal"

urlpatterns = [
    path('', admin.site.urls),
    path('graphiql/', GraphQLView.as_view(graphiql=True))
]
