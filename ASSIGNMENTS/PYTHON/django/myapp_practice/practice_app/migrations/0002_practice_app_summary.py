# Generated by Django 3.2.8 on 2022-02-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice_app',
            name='summary',
            field=models.TextField(default='Type Your Summary!'),
        ),
    ]
