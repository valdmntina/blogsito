from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

#este lista
def index(response):
    posts = Post.objects.all()
    for obj in posts:
        print(obj.titulo)
    return HttpResponse("lista de posts")

#este guarda
def storage(request, titulo, cuerpo):
    post = Post(titulo=titulo, cuerpo=cuerpo)
    post.save()
    return HttpResponse("guardamos los datos")

#este busca id
def mostrar_id(request, id):
    post = Post.objects.get(id=id)
    return HttpResponse(f"Titulo: {post.titulo}, Cuerpo: {post.cuerpo}, Fecha: {post.fecha}")

#este modifica 
def modificar(request, titulo, id):
    post = Post.objects.get(id=id)
    post.titulo = titulo
    post.save()
    return HttpResponse("post actualizado")


#este elimina id
def eliminar(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponse("eliminao 😂")