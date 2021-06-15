# Generated by Django 3.2.4 on 2021-06-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='Num')),
                ('symbol', models.CharField(max_length=10, verbose_name='Symbol')),
                ('date', models.DateField(auto_now=True, verbose_name='Date')),
                ('opening', models.FloatField(verbose_name='Open')),
                ('high', models.FloatField(verbose_name='High')),
                ('low', models.FloatField(verbose_name='Low')),
                ('volume', models.BigIntegerField(verbose_name='Volume')),
                ('adjclose', models.FloatField(verbose_name='adjclose')),
            ],
        ),
    ]
