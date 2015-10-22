from rest_framework import serializers

from ..models import Place

# Serializers define the API representation.
class PlaceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Place
    fields = ('id', 'status', 'latitude', 'longitude')
