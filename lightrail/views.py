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

@permission_required('admin.can_add_log_entry')
def calendar_upload(request):
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
        sd = column[8]
        ed = column[9]
        _, created = Calendar.objects.update_or_create(
            service_id=column[0],
            monday=column[1],
            tuesday=column[2],
            wednesday=column[3],
            thursday=column[4],
            friday=column[5],
            saturday=column[6],
            sunday=column[7],
            start_date='-'.join([sd[:4], sd[4:6], sd[6:]]),
            end_date='-'.join([ed[:4], ed[4:6], ed[6:]]),
         
        )
    context = {}
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def shapes_upload(request):
    template = "shapes_upload.html"
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
        _, created = Shapes.objects.update_or_create(
            shape_identifier=column[0],
            shape_pt_lat=column[1],
            shape_pt_long=column[2],
            shape_pt_sequence=column[3],
            shape_dist_traveled=column[4],
        )
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def trips_upload(request):
    template = "trips_upload.html"
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
        _, created = Trips.objects.update_or_create(
            id=column[2],
            route_id=column[0],
            service_id=column[1].replace('"', ""),
            trip_headsign=column[3],
            trip_short_name=column[4],
            direction_id=column[5].replace('"', ""),
            block_id=column[6].replace('"', ""),
            shape_name=column[7].replace('"', ""),
            wheelchair_accessible=column[8].replace('"', ""),
            bikes_allowed=column[9].replace('"', ""),
            trip_note=column[10],
            route_direction=column[11],
         
        )
    context = {}
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def stopTimes_upload(request):
    template = "stopTimes_upload.html"
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
        _, created = StopTimes.objects.update_or_create(
            trip_id=column[0],
            arrival_time=column[1].replace('"', ""),
            departure_time=column[2].replace('"', ""),
            stop_id=column[3],
            stop_sequence=column[4].replace('"', ""),
            stop_headsign=column[5].replace('"', ""),
            pickup_type=column[6].replace('"', ""),
            drop_off_type=column[7].replace('"', ""),
            shape_dist_traveled=column[8].replace('"', ""),
            timepoint=column[9].replace('"', ""),
            stop_note=column[10].replace('"', ""),         
        )
    context = {}
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def calendarDates_upload(request):
    template = "calendarDates_upload.html"
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
    for column in csv.reader(io_string, delimiter=',', quotechar='"'):
        _, created = CalendarDates.objects.update_or_create(
            service_id=column[0].replace("'", ""),
            date=column[1].replace('"', ""),
            exception_type=column[2].replace('"', ""),     
        )
    context = {}
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def notes_upload(request):
    template = "notes_upload.html"
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
    for column in csv.reader(io_string, delimiter=',', quotechar='"'):
        _, created = Notes.objects.update_or_create(
            note_text=column[1].replace("'", "")     
        )
    context = {}
    return render(request, template, context)