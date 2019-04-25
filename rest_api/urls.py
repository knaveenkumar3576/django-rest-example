from django.conf.urls import url

from .views import AddScore, GetScore

urlpatterns = [
    url(r'^(?P<player>[A-Z a-z 0-9]+)/(?P<score>[0-9]+)$', AddScore.as_view(), name="AddScore"),
    url(r'^(?P<player>[A-Z a-z 0-9]+)/$', GetScore, name="GetScore"),
]
