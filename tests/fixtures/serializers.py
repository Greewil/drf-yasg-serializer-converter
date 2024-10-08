from rest_framework.serializers import ModelSerializer

from tests.fixtures.models import HouseModel, HouseOccupierModel


class HouseBasicSerializer(ModelSerializer):
    class Meta:
        model = HouseModel
        fields = ['id', 'address']


class HouseSerializer(ModelSerializer):
    class Meta:
        model = HouseModel
        fields = '__all__'


class HouseOccupierSerializer(ModelSerializer):
    class Meta:
        model = HouseOccupierModel
        # fields = '__all__'
        fields = ['id', 'name', 'is_adult', 'house_id']


class HouseOccupierWithHouseSerializer(ModelSerializer):
    house = HouseSerializer(read_only=False)

    class Meta:
        model = HouseOccupierModel
        fields = ['id', 'name', 'is_adult', 'house_id',
                  'house']
        depth = 1


class HouseOccupierWithBasicHouseSerializer(ModelSerializer):
    openapi_help_text = 'House occupier with house (id and address).'
    house = HouseBasicSerializer(read_only=True)

    class Meta:
        model = HouseOccupierModel
        fields = ['id', 'name', 'is_adult', 'house_id',
                  'house']
        depth = 1


class HouseWithOccupiersSerializer(ModelSerializer):
    house_occupiers = HouseOccupierSerializer(read_only=False, many=True)

    class Meta:
        model = HouseModel
        fields = ['id', 'address', 'description', 'time_build', 'square_meters', 'rooms_number',
                  'owners_number', 'is_abandoned',
                  'house_occupiers']
        depth = 1
