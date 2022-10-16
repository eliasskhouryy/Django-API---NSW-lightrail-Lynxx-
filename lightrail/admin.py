from django.contrib import admin
from .models import Routes
# Register your models here.
class RoutesAdmin(admin.ModelAdmin):
    readonly_fields = ('id')
