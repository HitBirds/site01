# Generated by Django 2.0.3 on 2018-08-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0002_auto_20180805_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cite',
            name='header',
            field=models.CharField(max_length=30, verbose_name='logo'),
        ),
    ]