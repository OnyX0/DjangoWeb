from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('detail/<int:pk>', views.TaskDetailView.as_view(), name='detail'),
    path('edit-page', views.TaskCreateView.as_view(), name='edit'),
    path('update-page/<int:pk>', views.TaskUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', views.TaskDeleteView.as_view(), name='delete_page'),
]