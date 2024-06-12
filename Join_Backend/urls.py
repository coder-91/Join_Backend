from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from contact.views import ContactViewSet
from subtask.views import SubtaskViewSet
from task.views import TaskViewSet
from user.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'subtasks', SubtaskViewSet)
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
