from django.core.management.base import BaseCommand
from backend.utils import populate_db

class Command(BaseCommand):
    help = 'Populate the Database with imdb.json'

    def add_arguments(self, parser):
        parser.add_argument('-r', '--filename', type=str, help='Name of the IMDB JSON File', default='imdb.json')
        pass

    def handle(self, *args, **kwargs):
        filename = kwargs.get('filename')
        populate_db(filename)