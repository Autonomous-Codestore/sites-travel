# Generated by Django 3.2.9 on 2021-12-11 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_packagecategory_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='country',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='telephone',
        ),
    ]
