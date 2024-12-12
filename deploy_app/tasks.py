from celery import shared_task
import time
from .models import Deployment
from .services import check_resources, allocate_resources

@shared_task
def process_deployments():
    while True:
        pending_deployments = Deployment.objects.filter(status='queued').order_by('-priority')
        for deployment in pending_deployments:
            if check_resources(deployment):
                allocate_resources(deployment)
                deployment.status = 'running'
                deployment.save()
        time.sleep(10)