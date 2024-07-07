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
    **{
        "x-nullable": False
    }
)
address_property = openapi.Schema(
    type=openapi.TYPE_STRING,
    read_only=False,
    **{
        "x-nullable": False
    }
)
description_property = openapi.Schema(
    type=openapi.TYPE_STRING,
    read_only=False,
    **{
        "x-nullable": True
    }
    # TODO default=None
)

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
        # TODO
        # 'time_build': time_build_property,
        # 'square_meters': square_meters_property,
        # 'rooms_number': rooms_number_property,
        # 'owners_number': owners_number_property,
        # 'is_abandoned': is_abandoned_property
    }
)
