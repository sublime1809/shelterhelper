from django.conf.urls import url, patterns, include
from django.views.decorators.csrf import csrf_exempt

from api.views import dog_views


dog_patterns = patterns(
    '',
    url('^$', csrf_exempt(dog_views.DogListView.as_view()), name='list'),
    url('^(?P<pk>[\d]+)/$', csrf_exempt(dog_views.DogIndexView.as_view()), name='index'),
    url('^(?P<filter_params>.+)/$', csrf_exempt(dog_views.DogQueryView.as_view()), name='query'),
)

urlpatterns = patterns(
    '',
    url(r'^pet/dog/', include(dog_patterns, namespace='dog')),
)
