"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from lightrail.views import agency_upload, route_upload, stops_upload, calendar_upload, shapes_upload, trips_upload, stopTimes_upload, calendarDates_upload, notes_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lightrail/', include('lightrail.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('upload-agency-csv/', agency_upload, name="agency_upload"),
    path('upload-routes-csv/', route_upload, name="route_upload"),
    path('upload-stops-csv/', stops_upload, name="stops_upload"),
    path('upload-calendar-csv/', calendar_upload, name="calendar_upload"),
    path('upload-shapes-csv/', shapes_upload, name="shapes_upload"),
    path('upload-trips-csv/', trips_upload, name="trips_upload"),
    path('upload-stoptimes-csv/', stopTimes_upload, name="stoptimes_upload"),
    path('upload-calendardates-csv/', calendarDates_upload, name="calendardates_upload"),
    path('upload-notes-csv/', notes_upload, name="notes_upload"),
]

urlpatterns += static(settings.MEDIA_URL)
