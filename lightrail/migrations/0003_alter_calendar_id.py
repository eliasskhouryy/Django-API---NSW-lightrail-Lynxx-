# Generated by Django 4.1.2 on 2022-10-13 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lightrail', '0002_rename_wedesday_calendar_wednesday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]