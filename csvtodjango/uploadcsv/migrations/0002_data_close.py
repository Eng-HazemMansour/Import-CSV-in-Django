# Generated by Django 3.2.4 on 2021-06-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadcsv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='close',
            field=models.FloatField(null=True, verbose_name='Close'),
        ),
    ]