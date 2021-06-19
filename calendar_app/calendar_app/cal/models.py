from django.db import models

# Create your models here.

#import datetime
#from django.db import models
#from django.utils import timezone

class DateInfo(models.Model):
    date_month = models.IntegerField()
    date_day = models.IntegerField()
    date_year = models.IntegerField()
    date_content = models.CharField(max_length=1000)
    def __str__(self):
        return "%d %d, %d \n %s" %(self.date_month, self.date_day, self.date_year, self.date_content)
    def day_and_text(self):
        return "%d \n %s " %(self.date_day, self.date_content)