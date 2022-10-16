from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Agency, Calendar, Routes, Stops, Shapes, Trips, StopTimes, CalendarDates, Notes
from .serializers import AgencySerializer, CalendarSerializer, RoutesSerializer, StopsSerializer, ShapesSerializer, TripsSerializer, StopTimesSerializer, CalendarDatesSerializer, NotesSerializer
from lightrail import serializers
from rest_framework.generics import ListCreateAPIView

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
import csv, io
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
fs = FileSystemStorage(location='tmp/')
from django.utils.datastructures import MultiValueDictKeyError

class RoutesViewSet(ModelViewSet):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer
    def get_serializer_context(self):
        return {'request': self.request}

class AgencyViewSet(ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    def get_serializer_context(self):
        return {'request': self.request}

class StopsViewSet(ModelViewSet):
    queryset = Stops.objects.all()
    serializer_class = StopsSerializer
    def get_serializer_context(self):
        return {'request': self.request}

class CalendarViewSet(ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    def get_serializer_context(self):
        return {'request': self.request}

class ShapesViewSet(ModelViewSet):
    queryset = Shapes.objects.all()
    serializer_class = ShapesSerializer
    def get_serializer_context(self):
        return {'request': self.request}

class TripsViewSet(ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer
    def get_serializer_context(self):
        return {'request': self.request}

class StopTimesViewSet(ModelViewSet):
    queryset = StopTimes.objects.all()
    serializer_class = StopTimesSerializer
    def get_serializer_context(self):
        return {'request': self.request}

class CalendarDatesViewSet(ModelViewSet):
    queryset = CalendarDates.objects.all()
    serializer_class = CalendarDatesSerializer
    def get_serializer_context(self):
        return {'request': self.request}

class NotesViewSet(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    def get_serializer_context(self):
        return {'request': self.request}


@permission_required('admin.can_add_log_entry')
def agency_upload(request):
    template = "agency_upload.html"
    prompt = {
        'order': 'Order of the CSV should be whatever the model is'
    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'this is not csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Agency.objects.update_or_create(
            agency_id=column[0],
            agency_name=column[1],
            agency_url=column[2],
            agency_timezone=column[3],
            agency_lang=column[4],
            agency_phone=column[5],
            agency_fare_url=column[6],
            agency_email=column[7],
        )
    context = {}
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def route_upload(request):
    template = "route_upload.html"
    prompt = {
        'order': 'Order of the CSV should be whatever the model is'
    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'this is not csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = Routes.objects.update_or_create(
            route_id=column[0],
            agency_id=column[1],
            route_short_name=column[2],
            route_long_name=column[3],
            route_desc=column[4],
            route_type=column[5],
            route_color=column[6],
            route_url=column[7],
        )
    context = {}
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def stops_upload(request):
    template = "stops_upload.html"
    prompt = {
        'order': 'Order of the CSV should be whatever the model is'
    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'this is not csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = Stops.objects.update_or_create(
            id=column[0],
            stop_code=column[1],
            stop_name=column[2],
            stop_desc=column[3],
            stop_lat=column[4],
            stop_lon=column[5],
            zone_id=column[6],
            stop_url=column[7],
            location_type=column[8],
            parent_station=column[9],
            stop_timezone=column[10],
            wheelchair_boarding=column[11],
            platform_code=column[12],
        )
    context = {}
    return render(request, template, context)