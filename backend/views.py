from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Movie
from .serializer import MovieSerializer
from main.pagination import MainLimitOffsetPagination

from .swagger import SEARCH_QUERY_PARAM, LIMIT_PARAM, OFFSET_PARAM
# Create your views here.

SWAGGER_TAGS = ['main']

class SearchMovieAPI(APIView, MainLimitOffsetPagination):
    @swagger_auto_schema(
        manual_parameters=[
            SEARCH_QUERY_PARAM,
            OFFSET_PARAM,
            LIMIT_PARAM,
        ],
        tags=SWAGGER_TAGS,
    )

    def get(self, request):
        search_query = request.GET.get('search_query','')
        movie_data = Movie.objects.filter(name__icontains=search_query)
        serialized_movie_list = MovieSerializer(movie_data, many=True).data
        results = self.paginate_queryset(serialized_movie_list, request, view=self)
        return self.get_paginated_response(results)