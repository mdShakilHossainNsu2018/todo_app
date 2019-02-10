from django.urls import path

from . import views
from todo.views import IndexView

app_name = 'todo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('addtodo/', views.addTodo, name='addTodo'),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name='deleteTodo' )
]




