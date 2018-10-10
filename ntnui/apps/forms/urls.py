from django.urls import path
from .views import *
from django.conf.urls import url
from .form_types import FORM_TYPES
from forms.models import *

app_name = 'forms'
urlpatterns = [
    path(CoachFormModel.form_slug+"-instantiator", CoachInstantiatorView.as_view(), name=CoachFormModel.form_slug+"-instantiator"),
    path(CoachFormModel.form_slug+'-signer-info/<int:id>/', CoachSignerInfoView.as_view(), name=CoachFormModel.form_slug+"-signer-info"),
    path(CoachFormModel.form_slug+'-signer/<int:id>/', CoachSignerView.as_view(), name=CoachFormModel.form_slug+"-signer"),
    path('incoming-list', IncomingView.as_view(), name="incoming-list"),
    path('outgoing-list', OutgoingView.as_view(), name="outgoing-list"),
    path('instantiate-form-list', InstantiateListView.as_view(), name="instantiate-form-list"),
]