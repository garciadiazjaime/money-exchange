from rest_framework import routers

from .views import PlaceViewSet

# Routers provide an easy way of automatically determining the URL conf.
# These are the Django Rest available routes
router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)