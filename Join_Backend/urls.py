from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authentication.views import CustomUserViewSet
from contact.views import ContactViewSet
from subtask.views import SubtaskViewSet
from task.views import TaskViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'subtasks', SubtaskViewSet, basename='subtasks')
router.register(r'contacts', ContactViewSet, basename='contacts')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('authentication.urls')),
    # path('', include('task.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    )
]
