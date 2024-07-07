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


class HouseWithOccupiersSerializer(ModelSerializer):
    class Meta:
        model = HouseModel
        fields = ['id', 'address', 'description', 'time_build', 'square_meters', 'rooms_number',
                  'owners_number', 'is_abandoned',
                  'house_occupiers']
        depth = 1


class HouseOccupierSerializer(ModelSerializer):
    class Meta:
        model = HouseOccupierModel
        fields = '__all__'
