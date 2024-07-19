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

# END properties --------------------------- START schemas

house_basic_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': id_property,
        'address': address_property,
    }
)

house_schema = openapi.Schema(
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
    }
)
