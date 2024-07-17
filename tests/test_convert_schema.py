from .fixtures.conftest import *  # noqa: F401, F403

from drf_yasg_serializer_converter.swaggers_schema_properties.openapi_schema_converters import get_schema
from tests.fixtures.serializers import HouseSerializer, HouseBasicSerializer
from .fixtures.openapi_schemas import house_basic_schema


def test_basic_convert():
    generated_schema = get_schema(HouseBasicSerializer)
    correct_schema = house_basic_schema
    generated_schema_prop_items = generated_schema.properties.items()
    correct_schema_prop_items = correct_schema.properties.items()
    assert len(correct_schema_prop_items) == len(generated_schema_prop_items)
    for key, value in correct_schema_prop_items:
        print(key, value)
        print(f'prop_item_key: {key}, value_dict: {dict(value)}')
        assert dict(value) == dict(generated_schema.properties[key])
