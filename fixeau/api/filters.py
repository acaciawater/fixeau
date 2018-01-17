'''
Created on Jan 13, 2018

@author: theo
'''
import rest_framework_filters as filters
from ..data.models import Measurement, Timeseries

ALL_LOOKUPS = '__all__'

class MeasurementFilter(filters.FilterSet):
    
    class Meta:
        model = Measurement
        fields = {
            'time': ALL_LOOKUPS,
            'value': ALL_LOOKUPS,
            'parameter': ALL_LOOKUPS,
        }
    
class TimeSeriesFilter(filters.FilterSet):
    
    class Meta:
        model = Timeseries
        fields = {
            'name': ALL_LOOKUPS,
        }
