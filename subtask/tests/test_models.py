

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from subtask import models


class ModelTests(TestCase):
    """Test models."""

    def test_create_subtask(self):
        """Test creating a subtask is successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )

        task = models.Task.objects.create(
            title='Title',
            description='Description',
            dueTo=timezone.now(),
            created=timezone.now(),
            updated=timezone.now(),
            priority='LOW',
            category='USER_STORY',
            status='DONE',
        )
        task.users.add(user)

        subtask = models.Subtask.objects.create(
            description='Sample Subtask',
            is_done=True,
            task=task,
        )

        self.assertEqual(str(subtask), subtask.description)
