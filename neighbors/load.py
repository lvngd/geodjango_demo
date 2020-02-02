import os
from django.contrib.gis.utils import LayerMapping
from .models import Neighborhood

# Auto-generated `LayerMapping` dictionary for Neighborhood model
neighborhood_mapping = {
    'boro_code': 'boro_code',
    'boro_name': 'boro_name',
    'county_fip': 'county_fip',
    'ntacode': 'ntacode',
    'ntaname': 'ntaname',
    'shape_area': 'shape_area',
    'shape_leng': 'shape_leng',
    'geom': 'MULTIPOLYGON',
}


neighborhood_shapefile = '/Users/Christina/Downloads/NTA/geo_export_61339824-ff0c-4002-ae14-c1cd5103949d.shp'

def run(verbose=True):
	layermap = LayerMapping(Neighborhood,neighborhood_shapefile,neighborhood_mapping,transform=False)
	layermap.save(strict=True,verbose=verbose)
