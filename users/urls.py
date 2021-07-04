from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^verify/(?P<uuid>[a-z0-9\-]+)/', VerifyView.as_view(), name='verify'),
]