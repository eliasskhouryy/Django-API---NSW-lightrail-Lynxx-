from statistics import mode
from turtle import shape
from django.db import models
from django import utils
from django.forms import DecimalField
from datetime import datetime



class Agency(models.Model):
    agency_id = models.CharField(primary_key=True, max_length=100, default=0)
    agency_name = models.CharField(max_length=255)
    agency_url = models.URLField(max_length=200)
    agency_timezone = models.CharField(max_length=255)
    agency_lang = models.CharField(max_length=255)
    agency_phone = models.CharField(max_length=255, null=True)
    agency_fare_url = models.URLField(max_length=200, null=True)
    agency_email = models.EmailField(null=True)
    def __str__(self) -> str:
        return self.agency_name

class Routes(models.Model):
    route_id = models.CharField(primary_key=True, max_length=100)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, default=0)
    route_short_name = models.CharField(max_length=255)
    route_long_name = models.CharField(max_length=255)
    route_desc = models.TextField()
    route_type = models.CharField(max_length=255)
    route_color = models.CharField(max_length=255)
    route_url = models.URLField(max_length=200, null=True, blank=True)


class Stops(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    stop_code = models.CharField(max_length=255, null=True)
    stop_name = models.CharField(max_length=255)
    stop_desc = models.TextField()
    stop_lat = models.DecimalField(max_digits=30, decimal_places=6)
    stop_lon = models.DecimalField(max_digits=30, decimal_places=6)
    zone_id = models.CharField(max_length=255)
    stop_url = models.URLField(max_length=200)
    location_type = models.CharField(max_length=255)
    parent_station = models.CharField(max_length=255)
    stop_timezone = models.CharField(max_length=255)
    wheelchair_boarding = models.IntegerField()
    platform_code = models.IntegerField()

        
class Calendar(models.Model):
    service_id = models.IntegerField()
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()

class Shapes(models.Model):
    id = models.AutoField(primary_key=True)
    shape_identifier = models.CharField(max_length=255, default=0)
    shape_pt_lat = models.DecimalField(max_digits=30, decimal_places=6)
    shape_pt_long = models.DecimalField(max_digits=30, decimal_places=6)
    shape_pt_sequence = models.IntegerField()
    shape_dist_traveled = models.DecimalField(max_digits=30, decimal_places=2)

class Trips(models.Model):
    id = models.CharField(primary_key=True, max_length=100, default=0)
    route = models.ForeignKey(Routes, on_delete=models.PROTECT, default=0)
    service_id = models.BigIntegerField()
    trip_headsign = models.CharField(max_length=255)
    trip_short_name = models.CharField(max_length=255, null=True)
    direction_id = models.BooleanField()
    block_id = models.BigIntegerField()
    shape_name = models.CharField(max_length=255, null=True)
    wheelchair_accessible = models.BooleanField()
    bikes_allowed = models.BooleanField()
    trip_note = models.CharField(max_length=255)
    route_direction = models.CharField(max_length=255)
    
class StopTimes(models.Model):
    trip = models.ForeignKey(Trips, on_delete=models.PROTECT, default=0)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    stop = models.ForeignKey(Stops, on_delete=models.PROTECT, default=0)
    stop_sequence = models.IntegerField()
    stop_headsign = models.CharField(max_length=255)
    pickup_type = models.BooleanField()
    drop_off_type = models.BooleanField()
    shape_dist_traveled = models.DecimalField(max_digits=30, decimal_places=2)
    timepoint = models.BooleanField()
    stop_note = models.CharField(max_length=255, default="empty note", null=True)

class CalendarDates(models.Model):
    service_id = models.IntegerField()
    date = models.DateField()
    exception_type = models.CharField(max_length=255)

class Notes(models.Model):
    note_text = models.TextField()