
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ="index"),
    #vistas del modulo
    path("post/", include('post.urls'))
]
