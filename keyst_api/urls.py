from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import KeystDataView, KeystDataDetailsView

urlpatterns = {
    url(r'^$', KeystDataView.as_view(), name="keystdata"),
    url(r'^(?P<pk>[\w.@+-]+)/$',
        KeystDataDetailsView.as_view(), name="keystdata-details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
