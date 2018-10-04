from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('0', CoachInstantiatorView.as_view(), name="Coach Instantiator"),
    path('1', CoachSignerInfoView.as_view(), name="Coach Signer Info"),
    path('2', CoachSignerView.as_view(), name="Coach Signer"),



]