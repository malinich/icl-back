from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField


class PointSet(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    points = JSONField(null=True, blank=True, default=list())

    class Meta:
        ordering = ('date',)
