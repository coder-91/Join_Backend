from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authentication.views import UserProfileViewSet
from contact.views import ContactViewSet
from subtask.views import SubtaskViewSet

router = routers.DefaultRouter()
router.register(r'authentication', UserProfileViewSet)
#router.register(r'tasks', TaskViewSet)
router.register(r'subtasks', SubtaskViewSet)
router.register(r'contacts', ContactViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('authentication.urls')),
    path('', include('task.urls')),
]
