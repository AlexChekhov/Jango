from django.db import models

# Create your models here.

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    room_number = models.IntegerField

    def __str__(self):
        return self.name