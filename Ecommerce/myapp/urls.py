from django.urls import path
from myapp.views import *

# Create your views here.

urlpatterns = [
    path("", inicio, name="inicio"),
    path("about/", about, name="about"),
    path("shop/", shop, name="shop"),
    path("itens/", index, name="itens"),
    path("itens/cadastrar/", create, name="criar_item"),
    path("itens/editar/<int:id>", edit, name="editar_item"),
    path("itens/atualizar/<int:id>", update, name="atualizar_item"),
    path("itens/visualizar/<int:id>", read, name="visualizar_item"),
    path("itens/deletar/<int:id>", delete, name="deletar_item"),
    path("cart/<int:id>", add_cart, name="add_cart"),
]