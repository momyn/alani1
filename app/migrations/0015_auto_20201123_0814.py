# Generated by Django 3.1.3 on 2020-11-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_info_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='product/%Y/%m/%d', verbose_name='Картинка'),
        ),
    ]
