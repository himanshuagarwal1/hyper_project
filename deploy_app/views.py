from rest_framework import viewsets
from .models import Deployment
from .services import single_deployment
from .serializers import DeploymentSerializer

class DeploymentViewSet(viewsets.ModelViewSet):
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def cluster_deployment(request):
    """
    API endpoint to trigger the deployment of a cluster.
    """


    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cluster_id = data.get('cluster_id')
            docker_image = data.get('docker_image')
            ram = data.get('ram')
            cpu = data.get('cpu')
            gpu = data.get('gpu')
            priority = data.get('priority', 1)  # Default priority 1

            deployment  = Deployment.objects.create(
            cluster=cluster_id,
            docker_image=docker_image,
            required_ram=ram,
            required_cpu=cpu,
            required_gpu=gpu,
            status='queued',
            priority=priority
        )
            


            response = single_deployment(deployment)
            
            if isinstance(response, str):  # Error message
                return JsonResponse({'message': response}, status=400)
            
            return JsonResponse({
                'message': 'Deployment started successfully',
                'deployment_id': response.id
            }, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
