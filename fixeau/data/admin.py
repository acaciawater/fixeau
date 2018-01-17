'''
Created on Jan 10, 2018

@author: theo
'''

from django.contrib.admin import ModelAdmin
from django.contrib.admin.decorators import register
from .models import Timeseries, Unit, Datasource, Measurement, UnitConversion

@register(Unit)
class UnitAdmin(ModelAdmin):
    model = Unit

@register(UnitConversion)
class UnitConversionAdmin(ModelAdmin):
    model = UnitConversion
    list_display = ('__str__','scale','offset')
    list_filter = ('source', 'target')
    
@register(Datasource)
class DatasourceAdmin(ModelAdmin):
    model = Datasource
    
@register(Timeseries)
class TimeseriesAdmin(ModelAdmin):
    model = Timeseries
    list_display = ('name','unit')
    
@register(Measurement)
class MeasurementAdmin(ModelAdmin):
    model = Measurement
    list_display = ('parameter','time','value')
    list_filter =('parameter','time','series','source')
