from django.db import models


class GetCounter(models.Model):
    parameter = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
