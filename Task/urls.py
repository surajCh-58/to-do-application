from django.urls import path
from . import views
app_name="Task"
urlpatterns = [
     path('addtask',views.AddTask, name="addtask"),
     path('edittask/<int:pk>',views.AddTask,name="edit"),
     path('delete/<int:pk>',views.DeleteTask,name="delete"),
     path('alltask',views.AllTask,name="alltask")
]
