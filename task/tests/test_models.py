from unittest import TestCase

from django.contrib.auth import get_user_model
from django.utils import timezone

from task import models


class ModelTests(TestCase):
    """Test models."""

    def test_create_task(self):
        """Test creating a task is successful."""
        user = get_user_model().objects.create_user(
            email='test@example.com',
            name='User',
            password='testpass123'
        )

        task = models.Task.objects.create(
            title='Title',
            description='Description',
            due_to=timezone.now(),
            priority='LOW',
            category='USER_STORY',
            status='DONE',
        )
        task.users.add(user)

        self.assertEqual(str(task), task.title)
