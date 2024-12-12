from django.db import models

class Cluster(models.Model):
    name = models.CharField(max_length=100, unique=True)
    total_ram = models.IntegerField()
    total_cpu = models.IntegerField()
    total_gpu = models.IntegerField()
    available_ram = models.IntegerField()
    available_cpu = models.IntegerField()
    available_gpu = models.IntegerField()
