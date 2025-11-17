from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Produto, Servico
from .form import ProdutoForm, ServicoForm

# Create your views here.

def index(request):
    produtos = Produto.objects.all()[:6]  
    return render(request, "index.html", {"produtos": produtos})


#Cruds Serviços
def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, "servicos.html", {"servicos": servicos})

@login_required
def cadastrar_servico(request):
    
    if not request.user.is_staff:
        return HttpResponseForbidden("Apenas administradores podem acessar esta página.")
    
    if request.method == 'POST':
        form = ServicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço cadastrado com sucesso!')
            return redirect('servicos')  
    else:
        form = ServicoForm()
    return render(request, 'form_servico.html', {'form': form, 'titulo': 'Cadastrar Serviço'})

@login_required
def editar_servico(request, pk):
    
    if not request.user.is_staff:
        return HttpResponseForbidden("Apenas administradores podem acessar esta página.")
    
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço atualizado com sucesso!')
            return redirect('servicos')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'form_servico.html', {'form': form, 'titulo': 'Editar Serviço'})

@login_required
def deletar_servico(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Apenas administradores podem acessar esta página.")
 
    servico = get_object_or_404(Servico, pk=pk)
    servico.delete()
    messages.success(request, 'Serviço deletado com sucesso!')
    return redirect('servicos')

def detalhar_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    return render(request, 'detalhe_servico.html', {'servico': servico})

#Cruds Produtos
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos.html", {"produtos": produtos})

@login_required
def cadastrar_produto(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Apenas administradores podem acessar esta página.")
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('produtos')  
    else:
        form = ProdutoForm()
    return render(request, 'form_produto.html', {'form': form, 'titulo': 'Cadastrar Produto'})

@login_required
def editar_produto(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Apenas administradores podem acessar esta página.")
    
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'form_produto.html', {'form': form, 'titulo': 'Editar Produto'})

@login_required
def deletar_produto(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Apenas administradores podem acessar esta página.")
    
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    messages.success(request, 'Produto deletado com sucesso!')
    return redirect('produtos')

def detalhar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'detalhe_produto.html', {'produto': produto})

