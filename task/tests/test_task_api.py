"""
Tests for task APIs.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APIClient

from task.models import Task
from task.serializers import TaskSerializer

TASKS_URL = reverse('task:task-list')


def detail_url(task_id):
    """Create and return a task detail URL."""
    return reverse('task:task-detail', args=[task_id])


def create_task(users=None, **params):
    """Create and return a sample task."""
    defaults = {
        'title': 'Sample Task',
        'description': 'Sample Description',
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


class PublicTaskAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(TASKS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTaskApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='user@user.com',
            name='User',
            password='password',
        )
        self.client.force_authenticate(self.user)

        self.another_user = get_user_model().objects.create_user(
            email='otheruser@otheruser.com',
            name='OtherUser',
            password='password',
        )

    def test_retrieve_tasks(self):
        """Test retrieving a list of tasks."""
        create_task(users=[self.user, self.another_user])
        create_task(users=[self.user])

        res = self.client.get(TASKS_URL)

        tasks = Task.objects.all().order_by('id')
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_task_detail(self):
        """Test get task detail."""
        task = create_task(users=[self.user])

        url = detail_url(task.id)
        res = self.client.get(url)

        serializer = TaskSerializer(task)
        self.assertEqual(res.data, serializer.data)

    def test_create_task(self):
        """Test creating a task."""
        payload = {
            'title': 'Title',
            'description': 'Description',
            'due_to': timezone.now(),
            'created': timezone.now(),
            'updated': timezone.now(),
            'priority': 'LOW',
            'category': 'USER_STORY',
            'status': 'DONE',
            'users': [self.user.id]
        }
        res = self.client.post(TASKS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        task = Task.objects.get(id=res.data['id'])
        for k, v in payload.items():
            if k == 'users':
                self.assertEqual(list(task.users.values_list('id', flat=True)), v)
            else:
                self.assertEqual(getattr(task, k), v)

    def test_partial_update(self):
        """Test partial update of a task."""
        task = create_task()

        payload = {'title': 'New task title'}
        url = detail_url(task.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, payload['title'])

    def test_full_update(self):
        """Test full update of task."""
        task = create_task()

        payload = {
            'title': 'Title',
            'description': 'Description',
            'due_to': timezone.now(),
            'created': timezone.now(),
            'updated': timezone.now(),
            'priority': 'LOW',
            'category': 'USER_STORY',
            'status': 'DONE',
            'users': [self.user.id]
        }
        url = detail_url(task.id)
        res = self.client.put(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        for k, v in payload.items():
            if k == 'users':
                self.assertEqual(list(task.users.values_list('id', flat=True)), v)
            else:
                self.assertEqual(getattr(task, k), v)

    def test_delete_task(self):
        """Test deleting a task successful."""
        task = create_task()

        url = detail_url(task.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
