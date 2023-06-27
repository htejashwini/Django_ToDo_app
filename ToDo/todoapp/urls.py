# from django.urls import path
# from . import views
# from .views import CustomLoginView, TaskList, TaskDetail

# urlpatterns = [
    
#     path('tasks/', TaskList.as_view(), name='tasks'),
#     path('task/<int:pk>/', TaskDetail.as_view(), name='tasks'),
#     path('', views.alltodos, name = 'alltodos'),
#     path('delete_item/<int:pk>', views.deleteItem, name='deleteItem'),
#     path('update_item/<int:pk>', views.updateItem, name='updateItem'),
   
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.alltodos, name='alltodos'),
    path('todo/<int:pk>/', views.TaskDetail.as_view(), name='taskDetail'),
    path('todo/update/<int:pk>/', views.updateItem, name='updateItem'),
    path('todo/delete/<int:pk>/', views.deleteItem, name='deleteItem'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]
