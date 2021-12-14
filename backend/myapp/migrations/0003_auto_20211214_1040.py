# Generated by Django 3.2.9 on 2021-12-14 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20211214_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='category',
        ),
        migrations.AddField(
            model_name='trip',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.category'),
            preserve_default=False,
        ),
    ]