# Generated by Django 3.2.8 on 2021-11-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReaderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RName', models.CharField(max_length=30)),
                ('RNumber', models.IntegerField(unique=True)),
                ('Gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], default='Male', max_length=10)),
                ('City', models.CharField(max_length=40)),
                ('ContactNumber', models.BigIntegerField()),
                ('Subscription', models.CharField(choices=[('Month', 'Monthly'), ('Annual', 'Annually')], default='Month', max_length=10)),
                ('Charges', models.IntegerField(choices=[(100, '100'), (1000, '1000')], default=100)),
            ],
            options={
                'db_table': 'reader',
                'ordering': ('-Charges',),
            },
        ),
    ]
