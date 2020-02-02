# Generated by Django 3.0.2 on 2020-01-31 17:28

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boro_code', models.FloatField()),
                ('boro_name', models.CharField(max_length=254)),
                ('county_fip', models.CharField(max_length=254)),
                ('ntacode', models.CharField(max_length=254)),
                ('ntaname', models.CharField(max_length=254)),
                ('shape_area', models.FloatField()),
                ('shape_leng', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
