# Generated by Django 3.1.3 on 2020-11-28 18:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adrress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.CharField(blank=True, max_length=50, null=True)),
                ('alley', models.CharField(blank=True, max_length=50, null=True)),
                ('plaque', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
