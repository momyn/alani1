# Generated by Django 3.1.3 on 2020-11-21 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201120_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textproduct',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produkt', to='app.category'),
        ),
    ]
