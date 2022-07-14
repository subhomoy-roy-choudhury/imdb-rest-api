from backend.models import Movie, Genre
from django.conf import settings
import json

def populate_db(filename='imdb.json'):
    try:

        json_file = f'{settings.BASE_DIR}/{filename}'

        with open(json_file) as file:
            movies_data = file.read()
            movies_list = json.loads(movies_data)
            
            for movie_obj in movies_list:
                single_movie_dict = dict()
                single_movie_dict['popularity'] = movie_obj.get('99popularity')
                single_movie_dict['director'] = movie_obj.get('director')
                single_movie_dict['imdb_score'] = movie_obj.get('imdb_score')
                single_movie_dict['name'] = movie_obj.get('name')

                movie, created = Movie.objects.get_or_create(**single_movie_dict)
                genres = movie_obj.get('genre')

                for genre in genres:
                    name = genre.strip()
                    genre, created = Genre.objects.get_or_create(name=name)
                    movie.genre.add(genre)
                movie.save()

            print('Successfully populated the database')
            return True

    except Exception as e:
        print(str(e))
        return False