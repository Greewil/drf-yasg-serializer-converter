from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class HouseModel(models.Model):
    address = models.CharField(max_length=256, null=False, blank=False)
    description = models.CharField(max_length=512, null=True, blank=True, default=None)
    time_build = models.DateTimeField(auto_now_add=True)
    square_meters = models.FloatField(default=100.1)
    rooms_number = models.IntegerField()
    owners_number = models.IntegerField(default=2, null=False, blank=False,
                                           validators=[MinValueValidator(1), MaxValueValidator(100)])
    is_abandoned = models.BooleanField(default=False, null=False, blank=False)

    class Meta:
        db_table = 'house'

    def __str__(self):
        return f'id: {self.id}, build: {self.time_build}'


class HouseOccupierModel(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    is_adult = models.BooleanField(default=False, null=False, blank=False)

    house = models.ForeignKey(HouseModel, on_delete=models.CASCADE, null=False, related_name='house_occupiers')

    class Meta:
        db_table = 'house_occupier'

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'
