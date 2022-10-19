from rest_framework import serializers
from .models import Calendar, CalendarDates, Routes, Agency, Stops, Shapes, Trips, StopTimes, Notes
from datetime import datetime

class AgencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'

class RoutesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'
        # ['id', 'agency', 'route_short_name', 'route_long_name', 'route_desc', ] 
        # all field exposes internal representation

class StopsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stops
        fields = '__all__'

class CalendarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'

class ShapesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shapes
        fields = '__all__'

class TripsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trips
        fields = '__all__'

class StopTimesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StopTimes
        fields = '__all__'

class CalendarDatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CalendarDates
        fields = '__all__'

class NotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'