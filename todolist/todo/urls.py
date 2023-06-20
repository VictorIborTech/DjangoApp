from django.urls import path
from .views import home,TasksList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete


urlpatterns =[
    path('', home, name = 'home'),
    path('tasks/', TasksList.as_view(),name ='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(),name ='task'),
    path('task/create/', TaskCreate.as_view(),name ='create_task'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(),name ='update_task'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(),name ='delete_task'),
]