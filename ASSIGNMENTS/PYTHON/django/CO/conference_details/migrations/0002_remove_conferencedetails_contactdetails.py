# Generated by Django 3.0.5 on 2022-02-14 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference_details', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conferencedetails',
            name='ContactDetails',
        ),
    ]