from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("produtos/", views.lista_produtos, name="produtos"),
    path("servicos/", views.lista_servicos, name="servicos"),
    path('produto/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produto/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('produto/deletar/<int:pk>/', views.deletar_produto, name='deletar_produto'),
    path('produto/detalhar/<int:pk>/', views.detalhar_produto, name='detalhar_produto'),
    path('servico/cadastrar/', views.cadastrar_servico, name='cadastrar_servico'),
    path('servico/editar/<int:pk>/', views.editar_servico, name='editar_servico'),
    path('servico/deletar/<int:pk>/', views.deletar_servico, name='deletar_servico'),
    path('servico/detalhar/<int:pk>/', views.detalhar_servico, name='detalhar_servico'),
]
