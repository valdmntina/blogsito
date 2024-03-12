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


def consultas(request):
#obtener todos los elementos de post
    posts = Post.objects.all()
#filtrar la consulta por una condicion
    filtro = Post.objects.filter(titulo='valentina')
#obtener un unico registro
    post = Post.objects.get(id=12)
#obtener 20 primeros elementos
    limit = Post.objects.all()[:20]
#obtener 6 resultados partiendo del 15
    limit2 = Post.objects.all()[15:21]
#obtener los registros ordenados por el titulo
    orden = Post.objects.all().order_by('cuerpo')[:10]
#obtener elementos que su id sea menor o igual que 20
    menor = Post.objects.filter(id__lte=20)
    return render (request, 'index.html', {
        'posts': posts,
        'filtro': filtro,
        'post': post,
        'limit': limit,
        'limit2': limit2,
        'orden': orden,
        'menor': menor
        })