from django.urls import path
from .views import *
from django.conf.urls import url
from .form_types import FORM_TYPES
from forms.models import *

app_name = 'forms'
coach = CoachFormModel.form_slug
urlpatterns = [
    path('3', FormTextSaverView.as_view(), name="Form Text Saver"),
    path('4', FormTextTestView.as_view(), name="Form Text Test View"),
    path(coach+'-signer/<int:id>/', CoachSignerView.as_view(), name=coach+"-signer"),
    path('incoming-list', IncomingView.as_view(), name="incoming-list"),
    path('outgoing-list', OutgoingView.as_view(), name="outgoing-list"),
    path('instantiate-form-list', InstantiateListView.as_view(), name="instantiate-form-list"),
    path('archive-incoming-list', IncomingArchiveView.as_view(), name="archive-incoming-list"),
    path('archive-outgoing-list', OutgoingArchiveView.as_view(), name="archive-outgoing-list"),
    path('signer-info/<str:slug>/<int:id>', InfoView.as_view(), name="signer-info"),
    path('instantiator/<str:slug>', InstantiatorView.as_view(), name="instantiator"),
]
