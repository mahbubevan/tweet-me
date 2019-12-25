from django.conf.urls import url
from . views import (
    TweetListView,
    TweetDetailView,
    TweetCreateView,
    TweetUpdateView,
    )

urlpatterns = [
    url(r'^$',TweetListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(),name='detail'),
    url(r'^create/$',TweetCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/update/$',TweetUpdateView.as_view(),name='update'),
]
