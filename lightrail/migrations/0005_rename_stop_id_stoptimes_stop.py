# Generated by Django 4.1.2 on 2022-10-13 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lightrail', '0004_rename_trip_id_trips_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stoptimes',
            old_name='stop_id',
            new_name='stop',
        ),
    ]