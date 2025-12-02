from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("produtos/", views.lista_produtos, name="produtos"),
    path("produtos/novo/", views.criar_produto, name="criar_produto"),
    path("produtos/<int:id>/editar/", views.editar_produto, name="editar_produto"),
    path("produtos/<int:id>/deletar/", views.deletar_produto, name="deletar_produto"),
    path("servicos/novo/", views.criar_servico, name="criar_servico"),
    path("servicos/<int:id>/editar/", views.editar_servico, name="editar_servico"),
    path("servicos/<int:id>/deletar/", views.deletar_servico, name="deletar_servico"),
    path("designs/", views.listar_designs, name="designs"),
]
