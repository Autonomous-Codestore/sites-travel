# Generated by Django 3.2.9 on 2022-03-26 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220112_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trip',
            options={'ordering': ['destination']},
        ),
    ]