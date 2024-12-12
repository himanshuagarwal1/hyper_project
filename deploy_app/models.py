from django.db import models

class Deployment(models.Model):
    cluster = models.ForeignKey('cluster_app.Cluster', on_delete=models.CASCADE)
    user = models.ForeignKey('auth_app.User', on_delete=models.CASCADE)
    docker_image_path = models.CharField(max_length=200)
    required_ram = models.IntegerField()
    required_cpu = models.IntegerField()
    required_gpu = models.IntegerField()
    priority = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('queued', 'queued'), ('running', 'running'), ('completed', 'completed')])


