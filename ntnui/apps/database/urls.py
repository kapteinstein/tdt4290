from django.conf.urls import url
from django.contrib import admin
from django.contrib import admin

''' Configure Admin '''
admin.site.site_header = "NTNUI Admin"
admin.site.site_title = "NTNUI Site Admin"
admin.site.index_title = "Welcome to the NTNUI Admin Portal"

urlpatterns = [
    url(r'^', admin.site.urls),
]
