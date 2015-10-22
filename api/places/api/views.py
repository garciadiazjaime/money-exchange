from rest_framework import viewsets

from ..models import Place
from .serializers import PlaceSerializer

# ViewSets define the view behavior.
class PlaceViewSet(viewsets.ModelViewSet):
  queryset = Place.objects.all()
  serializer_class = PlaceSerializer

  def get_queryset(self):
    queryset = Place.objects.all()
    return queryset.order_by('id')
