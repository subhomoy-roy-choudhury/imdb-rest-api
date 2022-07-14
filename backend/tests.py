from django.test import TestCase, Client
from .utils import populate_db
import json
from rest_framework import status
from django.urls import reverse
from .models import Movie
from .serializer import MovieSerializer

# Create your tests here.
class IMDBTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.movies_url = reverse("search-movies")
        populate_db('imdb_test.json')

    def test_populate_imdb_data(self):
        assert populate_db()

    def test_search_movies_api(self):
        response = self.client.get(self.movies_url)
        movie_data = Movie.objects.all()
        serialized_movie_list = MovieSerializer(movie_data, many=True).data
        self.assertEqual(response.json()['results'][0],json.loads(json.dumps(serialized_movie_list))[0])
        self.assertEqual(response.status_code, status.HTTP_200_OK)