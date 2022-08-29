# Generated by Django 3.1.6 on 2021-02-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructionapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('landsq', models.IntegerField(max_length=20)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='landproperty',
            field=models.CharField(max_length=15),
        ),
    ]