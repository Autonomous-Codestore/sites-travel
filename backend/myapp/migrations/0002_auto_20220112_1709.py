# Generated by Django 3.2.9 on 2022-01-12 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['category']},
        ),
        migrations.RemoveField(
            model_name='trip',
            name='category',
        ),
    ]