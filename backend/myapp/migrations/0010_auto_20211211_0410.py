# Generated by Django 3.2.9 on 2021-12-11 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20211211_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start',
            field=models.DateField(null=True),
        ),
    ]
