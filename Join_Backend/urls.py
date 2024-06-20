from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from subtask.views import SubtaskViewSet
from task.views import TaskViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'subtasks', SubtaskViewSet, basename='subtasks')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('user.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs',)
]
