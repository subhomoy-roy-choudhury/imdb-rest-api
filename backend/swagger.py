from drf_yasg import openapi

STRING = openapi.Schema(type=openapi.TYPE_STRING, description='Edited Meta Data for the document')

OFFSET_PARAM = openapi.Parameter(
    "offset",
    openapi.IN_QUERY,
    required=False,
    description="offset param",
    type=openapi.TYPE_INTEGER,
)
LIMIT_PARAM = openapi.Parameter(
    "limit",
    openapi.IN_QUERY,
    required=False,
    description="limit param",
    type=openapi.TYPE_INTEGER,
)
SEARCH_QUERY_PARAM = openapi.Parameter(
    "search_query",
    openapi.IN_QUERY,
    required=False,
    description="search query param",
    type=openapi.TYPE_STRING,
)