# -*- coding: utf-8 -*-

from rest_framework import viewsets, filters
from .models import place
from .serializers import placeSerializer

class placeViewSet(viewsets.ModelViewSet):
    queryset = place.objects.all()
    serializer_class = placeSerializer
    
    filter_backends = (filters.SearchFilter,)
    search_fields = ('destination', 'address','notes','date')
