from django.urls import path
from .views import *
from django.conf.urls import url
from .form_types import FORM_TYPES

app_name = 'forms'
urlpatterns = [
    #path('3', FormTextSaverView.as_view(), name="Form Text Saver"),
    #path('4', FormTextTestView.as_view(), name="Form Text Test View"),
    path('incoming-list/', IncomingView.as_view(), name="incoming-list"),
    path('outgoing-list/', OutgoingView.as_view(), name="outgoing-list"),
    path('archive-incoming-list/', IncomingArchiveView.as_view(), name="archive-incoming-list"),
    path('archive-outgoing-list/', OutgoingArchiveView.as_view(), name="archive-outgoing-list"),
    path('signer-info/<str:slug>/<int:id>/', InfoView.as_view(), name="signer-info"),
    path('instantiator/', InstantiatorView.as_view(), name="instantiator"),
    path('signer/<str:slug>/<int:id>/', SignerView.as_view(), name="signer"),
    path('', IncomingView.as_view(), name="forms-default"),
    path('sign/', SignView.as_view(), name='sign'),
]
