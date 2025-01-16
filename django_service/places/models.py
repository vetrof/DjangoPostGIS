from django.contrib.gis.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField(geography=True, null=True, blank=True)

    def __str__(self):
        return self.name
