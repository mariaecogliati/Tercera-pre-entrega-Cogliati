from django.shortcuts import render
from Instituto.models import Curso , Alumno , Profesor
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def inicio(request):
    return render( request , "padre.html")

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def ver_alumnos (request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)   

def ver_profesores (request):
    profesores = Profesor.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)   

def alta_curso(request):
    if request.method == "POST":
        curso = Curso( Nombre = request.POST["Nombre"] , Comision = request.POST["Comision"])
        curso.save()
        return render(request , "formcurso.html")
    return render(request , "formcurso.html")

def alta_alumno(request):
    if request.method == "POST":
        alumno = Alumno( Nombre = request.POST["Nombre"] , Apellido = request.POST["Apellido"] , Documento = request.POST["Documento"])
        alumno.save()
        return render(request , "formalumno.html")
    return render(request , "formalumno.html")

def alta_profesor(request):
    if request.method == "POST":
        profesor = Profesor( Nombre = request.POST["Nombre"] , Apellido = request.POST["Apellido"] , Documento = request.POST["Documento"])
        profesor.save()
        return render(request , "formprofe.html")
    return render(request , "formprofe.html")
    
def buscar_curso(request):

    return render(request, "buscar_curso.html")

def buscar(request):

    if request.GET["Nombre"]:
        Nombre = request.GET["Nombre"]
        cursos = Curso.objects.filter(Nombre__icontains= Nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    
