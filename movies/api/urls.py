from django.conf.urls import url
from api.views import MovieView, MovieDetailView

urlpatterns = [
    url(r'^movies/$', MovieView.as_view(), name='movies'), # To create a movie on our db
    url(r'^movies/(?P<id>[0-9]+)$', MovieDetailView.as_view(), name='movie_detail')
]

