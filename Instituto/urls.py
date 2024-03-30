from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    path("ver_alumnos", views.ver_alumnos , name="alumnos"),
    path("ver_profesores", views.ver_profesores , name="profesores"),
    path("alta_curso", views.alta_curso),
    path("alta_alumno", views.alta_alumno),
    path("alta_profesor", views.alta_profesor),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar)
 

]
