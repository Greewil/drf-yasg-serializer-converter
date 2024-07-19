import pytest
from drf_yasg import openapi

from .fixtures.conftest import *  # noqa: F401, F403

from drf_yasg_serializer_converter.swaggers_schema_properties.openapi_schema_converters import get_schema
from tests.fixtures.serializers import HouseSerializer, HouseBasicSerializer, HouseOccupierSerializer, \
    HouseWithOccupiersSerializer, HouseOccupierWithHouseSerializer, HouseOccupierWithBasicHouseSerializer
from .fixtures.openapi_schemas import house_basic_schema, house_schema, house_occupier_schema, \
    house_with_occupiers_schema, house_occupier_with_house_schema, house_occupier_with_basic_house_schema


def assert_generated_and_correct_schemas(generated_schema: openapi.Schema, correct_schema: openapi.Schema):
    generated_schema_prop_items = generated_schema.properties.items()
    correct_schema_prop_items = correct_schema.properties.items()
    assert len(correct_schema_prop_items) == len(generated_schema_prop_items)
    for key, value in correct_schema_prop_items:
        print(key, value)
        print(f'prop_item_key: {key}, value_dict: {dict(value)}')
        assert dict(value) == dict(generated_schema.properties[key])


@pytest.mark.parametrize("serializer, correct_schema", [
    (HouseBasicSerializer, house_basic_schema), (HouseSerializer, house_schema),
    (HouseOccupierSerializer, house_occupier_schema),
    # (HouseWithOccupiersSerializer, house_with_occupiers_schema),
    # TODO whats happening when lists attached in serializers?
    (HouseOccupierWithHouseSerializer, house_occupier_with_house_schema),
    (HouseOccupierWithBasicHouseSerializer, house_occupier_with_basic_house_schema),
])
def test_basic_convert(serializer, correct_schema):
    generated_schema = get_schema(serializer)
    assert_generated_and_correct_schemas(generated_schema, correct_schema)
