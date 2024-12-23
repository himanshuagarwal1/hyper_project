from rest_framework import viewsets
from .models import Cluster
from .serializers import ClusterSerializer
from rest_framework.permissions import IsAuthenticated

class ClusterViewSet(viewsets.ModelViewSet):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer
    permission_classes = [IsAuthenticated]
