from django.urls import path
from .views import DeploymentViewSet , cluster_deployment
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'deployment', DeploymentViewSet)


urlpatterns = [
    # Endpoint to deploy a cluster (single deployment)
    path('deploy/', cluster_deployment, name='deploy_cluster'),
]
urlpatterns+= router.urls