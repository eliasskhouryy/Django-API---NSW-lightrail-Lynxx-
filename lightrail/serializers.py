from rest_framework import serializers
from .models import Calendar, CalendarDates, Routes, Agency, Stops, Shapes, Trips, StopTimes, Notes
from datetime import datetime

class AgencySerializer(serializers.ModelSerializer):
        class Meta:
            model = Agency
            fields = '__all__'

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'
        # ['id', 'agency', 'route_short_name', 'route_long_name', 'route_desc', ] 
        # can also right fields = '__all__' - but exposes internal representation
    agency = serializers.HyperlinkedRelatedField(queryset=Agency.objects.all(), view_name='agency-detail')

class StopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stops
        fields = '__all__'
    # agency = serializers.HyperlinkedRelatedField(queryset=Agency.objects.all(), view_name='agency-detail')

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'

class ShapesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shapes
        fields = '__all__'

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = '__all__'
    route = serializers.HyperlinkedRelatedField(queryset=Routes.objects.all(), view_name='routes-detail')

class StopTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopTimes
        fields = '__all__'
    trip = serializers.HyperlinkedRelatedField(queryset=Trips.objects.all(), view_name='trips-detail')

class CalendarDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarDates
        fields = '__all__'

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'