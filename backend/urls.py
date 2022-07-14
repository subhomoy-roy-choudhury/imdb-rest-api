from django.urls import path
from .views import *

urlpatterns = [
    path('movie',SearchMovieAPI.as_view(),name = 'search-movies'),
]