# Generated by Django 4.1.2 on 2022-10-16 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lightrail', '0012_alter_agency_agency_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='agency_email',
            field=models.EmailField(max_length=254),
        ),
    ]
