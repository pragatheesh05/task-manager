from django.urls import path
from .views import TaskListCreate, profile, TaskDetail


urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('profile/', profile.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),

    
    
    #path('tasks/<int:pk>/', task_detail, name='task-detail'),
]