from django.urls import path
from task import views

urlpatterns = [
    path('tasks/', views.TaskView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetailsView.as_view(), name='task-details'),

    #path('tasks/', views.TaskList.as_view(), name='task-list'),
    #path('tasks/<int:pk>/', views.TaskDetails.as_view(), name='task-details'),
    #path('tasks/', views.task_list, name='task-list'),
    #path('tasks/<int:pk>/', views.task_details, name='task-details'),
]