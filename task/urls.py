from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task import views

router = DefaultRouter()
router.register('', views.TaskViewSet)

app_name = 'task'

urlpatterns = [
    path('', include(router.urls)),
]