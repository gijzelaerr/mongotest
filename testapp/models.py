from django.db import models


class Something(models.Model):
    name = models.CharField(max_length=100)
    some_field = models.FileField(blank=True, null=True)
