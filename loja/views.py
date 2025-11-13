from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProdutoForm, ServicoForm
from .models import Produto, Servico


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos.html", {"produtos": produtos})

def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("produtos")
    else:
        form = ProdutoForm()
    return render(request, "produtos_form.html", {"form": form})

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("produtos")
    else:
        form = ProdutoForm(instance=produto)
    return render(request, "produtos_form.html", {"form": form})

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect("produtos")


def index(request):
    servicos = Servico.objects.all()
    return render(request, "index.html", {"servicos": servicos})

def criar_servico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ServicoForm()
    return render(request, "servicos_form.html", {"form": form})

def editar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    if request.method == "POST":
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ServicoForm(instance=servico)
    return render(request, "servicos_form.html", {"form": form})

def deletar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    if request.method == "POST":
        servico.delete()
        return redirect("index")
