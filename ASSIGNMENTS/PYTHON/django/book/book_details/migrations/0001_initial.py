# Generated by Django 3.2.8 on 2022-02-12 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'authot',
                'ordering': ('-first_name',),
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=15)),
                ('website', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'publisher',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('publication_date', models.DateField()),
                ('authors', models.ManyToManyField(to='book_details.Author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_details.publisher')),
            ],
            options={
                'db_table': 'book',
                'ordering': ('-title',),
            },
        ),
    ]
