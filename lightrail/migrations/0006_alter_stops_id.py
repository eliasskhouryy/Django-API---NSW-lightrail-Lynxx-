# Generated by Django 4.1.2 on 2022-10-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lightrail', '0005_rename_stop_id_stoptimes_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stops',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]