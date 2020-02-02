from django.contrib.gis.db import models


class Neighborhood(models.Model):
    boro_code = models.FloatField()
    boro_name = models.CharField(max_length=254)
    county_fip = models.CharField(max_length=254)
    ntacode = models.CharField(max_length=254)
    ntaname = models.CharField(max_length=254)
    shape_area = models.FloatField()
    shape_leng = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)



