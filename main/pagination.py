from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status

class MainLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 50

    def paginate_queryset(self, queryset, request, view=None):
        self.limit = int(request.GET.get('limit',self.get_limit(request)))
        print(self.limit)
        if self.limit is None:
            return None

        self.count = self.get_count(queryset)
        self.offset = int(request.GET.get('offset',self.get_offset(request)))
        self.request = request
        if self.count > self.limit and self.template is not None:
            self.display_page_controls = True

        if self.count == 0 or self.offset > self.count:
            return []
        return list(queryset[self.offset:self.offset + self.limit])

    def get_paginated_response(self, data):
        return Response({
            "status": True,
            "code": status.HTTP_200_OK,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.count,
            'results': data
        })