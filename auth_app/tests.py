from django.test import TestCase
from django.contrib.auth import get_user_model
from auth_app.models import Organization

User = get_user_model

class UserModelTest(TestCase):

    def setUp(self):
        """Set up data for tests."""
        self.organization = Organization.objects.create(name='Test Org')
        self.user = User.objects.create(username='testuser', email='test@example.com', password='password123')

    def test_user_creation(self):
        """Test that a user can be created successfully."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('password123'))

    def test_user_can_join_organization(self):
        """Test that a user can join an organization using an invite code."""
        self.user.join_organization(self.organization.invite_code)
        self.assertEqual(self.user.organization, self.organization)
