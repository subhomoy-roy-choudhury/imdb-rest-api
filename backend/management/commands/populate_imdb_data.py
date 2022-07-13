from django.core.management.base import BaseCommand
from backend.models import Movie, Genre
from django.conf import settings
import json

class Command(BaseCommand):
    help = 'Populate the Database with imdb.json'

    def add_arguments(self, parser):
        parser.add_argument('-r', '--filename', type=str, help='Name of the IMDB JSON File', default='imdb.json')
        pass

    def handle(self, *args, **kwargs):
        filename = kwargs.get('filename')
        print(kwargs)
        try:

            json_file = f'{settings.BASE_DIR}/{filename}'

            with open(json_file) as file:
                movies_data = file.read()
                movies_list = json.loads(movies_data)
                
                for movie_obj in movies_list:
                    single_movie = dict()
                    single_movie['popularity'] = movie_obj.get('99popularity')
                    single_movie['director'] = movie_obj.get('director')
                    single_movie['imdb_score'] = movie_obj.get('imdb_score')
                    single_movie['name'] = movie_obj.get('name')

                    movie, created = Movie.objects.get_or_create(**single_movie)
                    genres = movie_obj.get('genre')

                    # create and link genres to movies
                    for genre in genres:
                        name = genre.strip()
                        genre, created = Genre.objects.get_or_create(name=name)
                        movie.genre.add(genre)
                    movie.save()

                print('Successfully populated the database')
                return

        except Exception as e:
            print(str(e))
            return