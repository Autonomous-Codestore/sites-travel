# Generated by Django 3.2.9 on 2021-12-16 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomadation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('budget', models.CharField(choices=[('budget', 'budget'), ('mid range', 'mid range'), ('up market', 'up market')], max_length=100)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='cars')),
                ('category', models.CharField(choices=[('executive', 'executive'), ('4x4', '4x4'), ('safari', 'safari'), ('vans', 'vans'), ('salon', 'salon'), ('buses', 'buses'), ('pickups', 'pickups'), ('trucks', 'trucks')], max_length=50)),
                ('capacity', models.PositiveIntegerField(default=3)),
                ('available', models.BooleanField(default=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('telephone', models.CharField(max_length=20, null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', django_countries.fields.CountryField(max_length=2)),
                ('destination', django_countries.fields.CountryField(max_length=2)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='flights')),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='gallery')),
                ('category', models.CharField(choices=[('gallery', 'gallery'), ('partner', 'partner')], default='gallery', max_length=50)),
                ('caption', models.CharField(max_length=100, null=True)),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='trips')),
                ('slots', models.PositiveIntegerField(default=0)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('details', models.TextField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('arrival_accomodation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arrival_accom', to='myapp.accomadation')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
                ('trip_accomodation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trip_accom', to='myapp.accomadation')),
            ],
            options={
                'ordering': ['-destination'],
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('permit_class', models.CharField(default='DL', max_length=100)),
                ('permit', models.FileField(upload_to='permits')),
                ('photo', models.ImageField(upload_to='cars')),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('trip', 'trip'), ('flight', 'flight'), ('car hire', 'car hire')], default='trip', max_length=50)),
                ('pickup', models.CharField(max_length=100)),
                ('dropoff', models.CharField(max_length=100)),
                ('start', models.DateField(null=True)),
                ('end', models.DateField(null=True)),
                ('slots', models.PositiveIntegerField(default=0)),
                ('adults', models.PositiveIntegerField(default=0)),
                ('children', models.PositiveIntegerField(default=0)),
                ('driven_by', models.CharField(choices=[('driver', 'our driver'), ('self', 'self')], default='driver', max_length=40, null=True)),
                ('carhire_trip', models.CharField(choices=[('up country', 'up country'), ('town', 'town')], default='up country', max_length=100)),
                ('booked_on', models.DateTimeField(auto_now_add=True)),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_by', to=settings.AUTH_USER_MODEL)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_booking', to='myapp.car')),
                ('flight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.flight')),
                ('trip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.trip')),
            ],
            options={
                'ordering': ['-booked_on'],
            },
        ),
    ]
