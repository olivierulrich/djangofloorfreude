from __future__ import unicode_literals

import uuid as uuid
from django.db import models


class Event(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=200)
    description = models.TextField()
    lineup = models.TextField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    price = models.IntegerField()
    private = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
