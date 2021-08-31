from django.urls import path
from api.views import MovieView, MovieDetailView

urlpatterns = [
    path('^movies/$', MovieView.as_view(), name='movies'), # To create a movie on our db
    path('^movies/(?P<id>[0-9]+)$', MovieDetailView.as_view(), name='movie_detail')
]

