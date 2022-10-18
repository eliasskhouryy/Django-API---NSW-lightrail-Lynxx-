# Generated by Django 4.1.2 on 2022-10-18 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('agency_id', models.CharField(default=0, max_length=100, primary_key=True, serialize=False)),
                ('agency_name', models.CharField(max_length=255)),
                ('agency_url', models.URLField()),
                ('agency_timezone', models.CharField(max_length=255)),
                ('agency_lang', models.CharField(max_length=255)),
                ('agency_phone', models.CharField(max_length=255)),
                ('agency_fare_url', models.URLField()),
                ('agency_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField()),
                ('monday', models.BooleanField()),
                ('tuesday', models.BooleanField()),
                ('wednesday', models.BooleanField()),
                ('thursday', models.BooleanField()),
                ('friday', models.BooleanField()),
                ('saturday', models.BooleanField()),
                ('sunday', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CalendarDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField()),
                ('date', models.DateField()),
                ('exception_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('route_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('route_short_name', models.CharField(max_length=255)),
                ('route_long_name', models.CharField(max_length=255)),
                ('route_desc', models.TextField()),
                ('route_type', models.CharField(max_length=255)),
                ('route_color', models.CharField(max_length=255)),
                ('route_url', models.URLField(blank=True, null=True)),
                ('agency', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lightrail.agency')),
            ],
        ),
        migrations.CreateModel(
            name='Shapes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shape_identifier', models.CharField(default=0, max_length=255)),
                ('shape_pt_lat', models.DecimalField(decimal_places=6, max_digits=30)),
                ('shape_pt_long', models.DecimalField(decimal_places=6, max_digits=30)),
                ('shape_pt_sequence', models.IntegerField()),
                ('shape_dist_traveled', models.DecimalField(decimal_places=2, max_digits=30)),
            ],
        ),
        migrations.CreateModel(
            name='Stops',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('stop_code', models.CharField(max_length=255, null=True)),
                ('stop_name', models.CharField(max_length=255)),
                ('stop_desc', models.TextField()),
                ('stop_lat', models.DecimalField(decimal_places=6, max_digits=30)),
                ('stop_lon', models.DecimalField(decimal_places=6, max_digits=30)),
                ('zone_id', models.CharField(max_length=255)),
                ('stop_url', models.URLField()),
                ('location_type', models.CharField(max_length=255)),
                ('parent_station', models.CharField(max_length=255)),
                ('stop_timezone', models.CharField(max_length=255)),
                ('wheelchair_boarding', models.IntegerField()),
                ('platform_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.CharField(default=0, max_length=100, primary_key=True, serialize=False)),
                ('service_id', models.BigIntegerField()),
                ('trip_headsign', models.CharField(max_length=255)),
                ('trip_short_name', models.CharField(max_length=255, null=True)),
                ('direction_id', models.BooleanField()),
                ('block_id', models.BigIntegerField()),
                ('shape_name', models.CharField(max_length=255, null=True)),
                ('wheelchair_accessible', models.BooleanField()),
                ('bikes_allowed', models.BooleanField()),
                ('trip_note', models.CharField(max_length=255)),
                ('route_direction', models.CharField(max_length=255)),
                ('route', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='lightrail.routes')),
            ],
        ),
        migrations.CreateModel(
            name='StopTimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('stop_sequence', models.IntegerField()),
                ('stop_headsign', models.CharField(max_length=255)),
                ('pickup_type', models.BooleanField()),
                ('drop_off_type', models.BooleanField()),
                ('shape_dist_traveled', models.DecimalField(decimal_places=2, max_digits=30)),
                ('timepoint', models.BooleanField()),
                ('stop_note', models.CharField(default='empty note', max_length=255, null=True)),
                ('stop', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='lightrail.stops')),
                ('trip', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='lightrail.trips')),
            ],
        ),
    ]
