# -*- coding: utf-8 -*-
from rest_framework import routers
from place.viewsets import placeViewSet

router = routers.DefaultRouter()
router.register('place', placeViewSet)