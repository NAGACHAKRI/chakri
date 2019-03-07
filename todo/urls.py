
from django.urls import path,include
from . import views
from todo.views import addtodo,deletetodo,updatetodo


urlpatterns = [
    path("show/",views.show),
    path("add/",views.add),
    path("home/",views.home),
    path("delete/",views.delete),
    path("todo/",views.todo),
    path("addtodo/",views.addtodo),
    path("updatetodo/<int:uptodo_id>/",views.updatetodo),
    path("deletetodo/<int:todo_id>/",views.deletetodo),
]