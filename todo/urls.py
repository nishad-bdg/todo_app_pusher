from django.urls import path
from todo import views

urlpatterns = [
    path('',views.ToDoList.as_view()),
    path('<int:pk>/',views.ToDoDetail.as_view()),
]
