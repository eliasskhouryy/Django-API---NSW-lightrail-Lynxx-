from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('routes', views.RoutesViewSet)
router.register('agency', views.AgencyViewSet)
router.register('stops', views.StopsViewSet)
router.register('calendar', views.CalendarViewSet)
router.register('shapes', views.ShapesViewSet)
router.register('trips', views.TripsViewSet)
router.register('stoptimes', views.StopTimesViewSet)
router.register('calendardates', views.CalendarDatesViewSet)
router.register('notes', views.NotesViewSet)

urlpatterns = router.urls
