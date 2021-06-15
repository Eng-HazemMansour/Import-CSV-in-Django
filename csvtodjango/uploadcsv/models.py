from django.db import models

# Create your models here.
class Data(models.Model):
    num = models.IntegerField("Num")
    symbol = models.CharField("Symbol", max_length = 10)
    date = models.DateField("Date", auto_now = True)
    opening = models.FloatField("Open")
    high = models.FloatField("High")
    low = models.FloatField("Low")
    close = models.FloatField("Close", null = True)
    volume = models.BigIntegerField("Volume")
    adjclose = models.FloatField("Adj Close")


    def  __str__(self):
        return self.symbol