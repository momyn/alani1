# Generated by Django 3.1.3 on 2020-11-23 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20201122_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='footer',
        ),
    ]
