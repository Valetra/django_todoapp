from django.urls import path
from .views import (
    todoappView,
    addTodoView,
    deleteTodoView,
    completeTodoItemView,
)

urlpatterns = [
    path('', todoappView),
    path('addTodoItem/', addTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
    path('completeTodoItemView/<int:i>/', completeTodoItemView)
]
