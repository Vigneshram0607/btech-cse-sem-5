# Generated by Django 3.2.8 on 2021-11-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sec_app',
            name='summary',
            field=models.TextField(default='this is cool!'),
        ),
    ]