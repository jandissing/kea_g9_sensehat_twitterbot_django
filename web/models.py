from django.db import models
from datetime import datetime

# Create your models here.

class HatData(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    DateTime = models.DateTimeField(db_column='DateTime', blank=True, null=True)  # Field name made lowercase.
    Temperature = models.DecimalField(db_column='Temperature', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    Humidity = models.IntegerField(db_column='Humidity', blank=True, null=True)  # Field name made lowercase.
    Pressure = models.DecimalField(db_column='Pressure', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'HatData'

    def __str__(self):
        return str(self.Id) + ' - ' + self.DateTime.strftime("%Y-%m-%d %H:%M:%S") + ' : Temp:' + str(self.Temperature) + 'C - Pressure:' + str(self.Pressure) + 'bars - Humidity:' + str(self.Humidity) + '%'


class LastSeenId(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    LastSeenId = models.CharField(db_column='LastSeenId', max_length=19, blank=True, null=True)  # Field name made lowercase.
    User = models.CharField(db_column='User', max_length=150, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    img_link = models.CharField(max_length=512, blank=True, null=True, default=None)
    Tweet = models.CharField(max_length=280, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'LastSeenId'

    def __str__(self):
        return str(self.Id) + ' - ' + self.created_at.strftime("%Y-%m-%d %H:%M:%S") + ' : User:' + self.User + ' with tweet ID ' + str(self.LastSeenId) + ' says:  ' + str(self.Tweet)


class TeamMember(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    Name = models.CharField(max_length=150)
    Picture = models.ImageField()
    Email = models.CharField(max_length=200)

    def __str__(self):
        return self.Name