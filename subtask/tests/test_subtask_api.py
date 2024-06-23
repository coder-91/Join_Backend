"""
Tests for subtask APIs.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APIClient

from task.models import Task
from subtask.models import Subtask
from subtask.serializers import SubtaskSerializer

SUBTASKS_URL = reverse('subtask:subtask-list')


def detail_url(subtask_id):
    """Create and return a subtask detail URL."""
    return reverse('subtask:subtask-detail', args=[subtask_id])


def create_task(users=None, **params):
    """Create and return a sample task."""
    defaults = {
        'title': 'Title',
        'description': 'Description',
        'due_to': timezone.now(),
        'created': timezone.now(),
        'updated': timezone.now(),
        'priority': 'LOW',
        'category': 'USER_STORY',
        'status': 'DONE',
    }
    defaults.update(params)
    task = Task.objects.create(**defaults)
    if users:
        task.users.add(*users)
    return task


def create_subtask(task, **params):
    """Create and return a sample subtask."""

    defaults = {
        'description': 'Sample Subtask description',
        'is_done': True,
        'task_id': task.id,
    }
    defaults.update(params)

    subtask = Subtask.objects.create(**defaults)
    return subtask


class PublicSubtaskAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(SUBTASKS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateSubtaskApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            name='User',
            password='testpass123',
        )
        self.client.force_authenticate(self.user)

        self.another_user = get_user_model().objects.create_user(
            email='otheruser@otheruser.com',
            name='OtherUser',
            password='password',
        )

        self.task = create_task(users=[self.user, self.another_user])

    def test_retrieve_subtasks(self):
        """Test retrieving a list of subtasks."""
        create_subtask(self.task)
        create_subtask(self.task)

        res = self.client.get(SUBTASKS_URL)

        subtasks = Subtask.objects.all().order_by('id')
        serializer = SubtaskSerializer(subtasks, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_subtask_detail(self):
        """Test get subtask detail."""
        subtask = create_subtask(self.task)

        url = detail_url(subtask.id)
        res = self.client.get(url)

        serializer = SubtaskSerializer(subtask)
        self.assertEqual(res.data, serializer.data)

    def test_create_subtask(self):
        """Test creating a subtask."""
        payload = {
            'description': 'Sample Subtask description',
            'is_done': True,
            'task_id': self.task.id,
        }
        res = self.client.post(SUBTASKS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        subtask = Subtask.objects.get(id=res.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(subtask, k), v)

    def test_partial_update(self):
        """Test partial update of a subtask."""
        subtask = create_subtask(self.task)

        payload = {'description': 'New subtask description'}
        url = detail_url(subtask.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        subtask.refresh_from_db()
        self.assertEqual(subtask.description, payload['description'])

    def test_full_update(self):
        """Test full update of subtask."""
        subtask = create_subtask(self.task)

        payload = {
            'description': 'Sample Subtask description',
            'is_done': True,
            'task_id': self.task.id,
        }
        url = detail_url(subtask.id)
        res = self.client.put(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        subtask.refresh_from_db()
        for k, v in payload.items():
            self.assertEqual(getattr(subtask, k), v)

    def test_delete_subtask(self):
        """Test deleting a subtask successful."""
        subtask = create_subtask(self.task)

        url = detail_url(subtask.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Subtask.objects.filter(id=subtask.id).exists())
