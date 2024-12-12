
from django.test import TestCase
from .models import Cluster

class ClusterResourceTestCase(TestCase):
    def setUp(self):
        print("enter")
        self.cluster = Cluster.objects.create(
            name='Test Cluster',
            total_ram=32, 
            total_cpu=16, 
            total_gpu=4, 
            available_ram=32, 
            available_cpu=16, 
            available_gpu=4
        )

    def test_check_resources_sufficient(self):
        """Test that resources are sufficient."""
        result = self.cluster.check_resources(8, 4, 1)
        self.assertTrue(result)

    def test_check_resources_insufficient(self):
        """Test that resources are insufficient."""
        result = self.cluster.check_resources(40, 4, 1)
        self.assertFalse(result)

    def test_allocate_resources(self):
        """Test that resources are allocated properly."""
        self.cluster.allocate_resources(8, 4, 1)
        self.assertEqual(self.cluster.available_ram, 24)
        self.assertEqual(self.cluster.available_cpu, 12)
        self.assertEqual(self.cluster.available_gpu, 3)
