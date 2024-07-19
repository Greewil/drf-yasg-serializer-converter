from copy import deepcopy

from drf_yasg import openapi

# collection_schema = openapi.Schema(
#     type=openapi.TYPE_OBJECT,
#     properties={
#         'total': openapi.Schema(
#             type=openapi.TYPE_INTEGER,
#             description='Total number of objects without limiting.',
#             example='100'
#         ),
#         'items': openapi.Schema(
#             type=openapi.TYPE_ARRAY,
#             description='List of returning items.',
#             items=obj_to_use
#         )
#     }
# )

id_property = openapi.Schema(
    type=openapi.TYPE_INTEGER,
    read_only=True,
)
address_property = openapi.Schema(
    type=openapi.TYPE_STRING,
    **{
        "maxLength": 256,
    }
)
description_property = openapi.Schema(
    type=openapi.TYPE_STRING,
    default=None,
    **{
        "maxLength": 512,
        "x-nullable": True,
    }
    # TODO default=None
)
time_build_property = openapi.Schema(
    type=openapi.TYPE_STRING,
    read_only=True,  # TODO check why?
    format=openapi.FORMAT_DATETIME,
)
square_meters_property = openapi.Schema(
    type=openapi.TYPE_NUMBER,
    default=100.1,
)
rooms_number_property = openapi.Schema(
    type=openapi.TYPE_INTEGER,
)
owners_number_property = openapi.Schema(
    type=openapi.TYPE_INTEGER,
    default=2,
    **{
        "minimum": 1,
        "maximum": 100,
    }
)
is_abandoned_property = openapi.Schema(
    type=openapi.TYPE_BOOLEAN,
    default=False,
)

occupier_name_property = openapi.Schema(
    type=openapi.TYPE_STRING,
    **{
        "maxLength": 256,
    }
)
occupier_is_adult_property = openapi.Schema(
    type=openapi.TYPE_BOOLEAN,
    default=False,
)

# END properties --------------------------- START schemas

house_basic_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=[],
    properties={
        'id': id_property,
        'address': address_property,
    }
)

house_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=[],  # TODO get required in base schema (depth=0)
    properties={
        'id': id_property,
        'address': address_property,
        'description': description_property,
        'time_build': time_build_property,
        'square_meters': square_meters_property,
        'rooms_number': rooms_number_property,
        'owners_number': owners_number_property,
        'is_abandoned': is_abandoned_property,
    }
)

house_occupier_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': id_property,
        'name': occupier_name_property,
        'is_adult': occupier_is_adult_property,
    }
)

# here read_only in house_schema should be false, because it was specified in serializers
house_occupier_with_house_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=[],
    properties={
        'id': id_property,
        'name': occupier_name_property,
        'is_adult': occupier_is_adult_property,
        'house': house_schema,
    }
)

house_basic_schema_with_read_only = deepcopy(house_basic_schema)
house_basic_schema_with_read_only.read_only = True
house_occupier_with_basic_house_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=[],
    properties={
        'id': id_property,
        'name': occupier_name_property,
        'is_adult': occupier_is_adult_property,
        'house': house_basic_schema_with_read_only,
    }
)

house_occupiers_list_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['id', 'name'],
    properties={}  # TODO

    # type=openapi.TYPE_ARRAY,
    # # description='List of returning items.',
    # items=house_occupier_schema
)

house_with_occupiers_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': id_property,
        'address': address_property,
        'description': description_property,
        'time_build': time_build_property,
        'square_meters': square_meters_property,
        'rooms_number': rooms_number_property,
        'owners_number': owners_number_property,
        'is_abandoned': is_abandoned_property,
        'house_occupiers': house_occupiers_list_schema,
    }
)
