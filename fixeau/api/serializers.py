'''
Created on Jan 10, 2018

@author: theo
'''
from ..data.models import Timeseries, Measurement, Datasource
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers

class DatasourceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Datasource
        fields = '__all__'

class TimeseriesSerializer(HyperlinkedModelSerializer):
    unit = serializers.StringRelatedField()
    class Meta:
        model = Timeseries
        fields = '__all__'
        geo_field = 'location'
            
class MeasurementSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
        geo_field = 'location'
