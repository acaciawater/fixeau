'''
Created on Jan 11, 2018

@author: theo
'''
from rest_framework.viewsets import ModelViewSet
from ..data.models import Timeseries, Measurement, Datasource
from .serializers import TimeseriesSerializer, MeasurementSerializer,\
    DatasourceSerializer

from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
from rest_framework_filters.backends import DjangoFilterBackend
from .filters import MeasurementFilter

class CreateListModelMixin(object):

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)
    
class DatasourceViewSet(ModelViewSet):
    queryset = Datasource.objects.all()
    serializer_class = DatasourceSerializer
    filter_fields = ('name',)
    search_fields = ('name',)
    
class TimeseriesViewSet(ModelViewSet):
    queryset = Timeseries.objects.all()
    serializer_class = TimeseriesSerializer
    filter_fields = ('name','parameter')
    search_fields = ('name',)

class MeasurementViewSet(CreateListModelMixin,ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_fields = ('time','parameter','value')
    filter_class = MeasurementFilter
    search_fields = ('name','parameter')
    distance_filter_field = 'location'
    distance_filter_convert_meters = True
    filter_backends = (DjangoFilterBackend, DistanceToPointFilter, InBBoxFilter)
    