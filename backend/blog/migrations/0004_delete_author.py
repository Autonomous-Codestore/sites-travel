# Generated by Django 3.2.9 on 2021-12-15 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]