from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.get_route, name='route'),
    path('todo', views.get_todo, name='todo'),
    path('todoid/<str:pk>', views.get_todo_id, name='todoid'),
    path('update/<str:pk>', views.update_todo, name='todoupdate'),
    path('delete/<str:pk>', views.delete, name='tododelete'),
    path('add', views.add_todo, name="addtodo")
]
