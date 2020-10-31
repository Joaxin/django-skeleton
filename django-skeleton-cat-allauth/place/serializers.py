# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import place
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        return self._choices[obj]


class placeSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()
    
    ## Unfortunately, it doesn't work for POST requests. 
    # city = serializers.CharField(source='get_city_display', read_only=True)

    city = ChoiceField(choices=place.CITY_CHOICES)

    class Meta:
        model = place
        fields = '__all__'