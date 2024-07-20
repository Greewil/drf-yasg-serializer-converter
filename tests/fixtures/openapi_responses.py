from copy import deepcopy

from drf_yasg import openapi

from tests.fixtures.openapi_schemas import house_basic_schema, house_occupier_with_basic_house_schema, \
    house_occupier_schema, house_with_occupiers_schema

listed_house_basic_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'total': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='Total number of objects without limiting.',
            example='100'
        ),
        'items': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            description='List of returning items.',
            items=house_basic_schema
        )
    }
)
listed_house_basic_response = openapi.Response('', listed_house_basic_schema)

listed_house_occupier_response = deepcopy(listed_house_basic_response)
listed_house_occupier_response.schema.properties['items'].items = house_occupier_schema

listed_house_with_occupiers_response = deepcopy(listed_house_basic_response)
listed_house_with_occupiers_response.schema.properties['items'].items = house_with_occupiers_schema

listed_house_occupier_with_basic_house_response = deepcopy(listed_house_basic_response)
listed_house_occupier_with_basic_house_response.schema.properties['items'].items = house_occupier_with_basic_house_schema
