'''
Created on Jan 10, 2018

@author: theo
'''
from django.db import models
import uuid
from django.utils.translation import ugettext as _
from django.contrib.gis.db import models as geo
from django.db.models.deletion import CASCADE, SET_NULL

class Unit(models.Model):
    name = models.CharField(max_length=40,verbose_name=_('name'))
    description = models.TextField(blank=True,verbose_name=_('description'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name=_('unit')
        verbose_name_plural=_('units')

class UnitConversion(models.Model):
    source = models.ForeignKey(Unit,related_name='source',verbose_name=_('source'),on_delete=CASCADE)
    target = models.ForeignKey(Unit,related_name='target',verbose_name=_('target'),on_delete=CASCADE)
    scale = models.FloatField(default=1,verbose_name=_('scale'))
    offset = models.FloatField(default=0,verbose_name=_('offset'))

    def __str__(self):
        return _('{} => {}').format(self.source,self.target)

    class Meta:
        verbose_name=_('Unit conversion')
        verbose_name_plural=_('Unit conversions')
        
class Datasource(models.Model):
    ''' Datasource '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40,verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name=_('datasource')
        verbose_name_plural=_('datasources')
    
class Timeseries(geo.Model):
    ''' Timeseries metadata '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, verbose_name=_('name'))
    location = geo.PointField(verbose_name=_('location'))
    parameter = models.CharField(max_length=100,verbose_name=_('parameter'))
    unit = models.ForeignKey(Unit,on_delete=SET_NULL,null=True,verbose_name=_('unit'))
    sourceID = models.ForeignKey(Datasource,null=True,blank=True,on_delete=CASCADE,verbose_name=_('datasource'))
    
    def fetch_measurements(self, **kwargs):
        return self.measurement_set.filter(**kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name=_('Timeseries')
        verbose_name_plural=_('Timeseries')
        #unique_together = ('name', 'sourceID')
        
class Measurement(geo.Model):
    ''' Single measurement that can be part of a Timeseries ''' 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = geo.PointField(null=True,blank=True,verbose_name=_('location'))
    time = models.DateTimeField(verbose_name=_('time'))
    parameter = models.CharField(max_length=100,verbose_name=_('parameter'))
    value = models.FloatField(verbose_name=_('value'))
    unit = models.CharField(max_length=40,verbose_name=_('unit'))
    source = models.CharField(max_length=40,blank=True,null=True,verbose_name=_('source'))
    series = models.ForeignKey(Timeseries,on_delete=SET_NULL,blank=True,null=True,verbose_name=_('timeseries'))

    class Meta:
        verbose_name=_('measurement')
        verbose_name_plural=_('measurements')
