# Generated by Django 4.1.2 on 2022-10-13 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lightrail', '0003_alter_calendar_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trips',
            old_name='trip_id',
            new_name='id',
        ),
    ]
