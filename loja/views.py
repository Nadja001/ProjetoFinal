from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .forms import ProdutoForm, ServicoForm
from .models import Produto, Servico
from django.db.models import Q
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.decorators import login_required

def lista_produtos(request):
    nome = request.GET.get("nome", "")
    preco_min = request.GET.get("preco_min", "")
    preco_max = request.GET.get("preco_max", "")
    ativo = request.GET.get("ativo", "")

    produtos_list = Produto.objects.all()

    # Filtro por nome
    if nome:
        produtos_list = produtos_list.filter(
            Q(nome__icontains=nome)
        )

    # Filtro por preço mínimo
    if preco_min:
        produtos_list = produtos_list.filter(preco__gte=preco_min)

    # Filtro por preço máximo
    if preco_max:
        produtos_list = produtos_list.filter(preco__lte=preco_max)

    # Filtro por ativo
    if ativo:
        produtos_list = produtos_list.filter(ativo=ativo)

    produtos_list = produtos_list.order_by('-id')

    paginator = Paginator(produtos_list, 10)
    page_number = request.GET.get('page')
    produtos = paginator.get_page(page_number)

    context = {
        "produtos": produtos,
        "request_get": request.GET,  # preserva valores no formulário
    }
    return render(request, "produtos.html", context)


@has_role_decorator('Admin')
@login_required(login_url='/usuarios/login/')
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("produtos")
    else:
        form = ProdutoForm()
    return render(request, "produtos_form.html", {"form": form})

@has_role_decorator('Admin')
@login_required(login_url='/usuarios/login/')
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

@has_role_decorator('Admin')
@login_required(login_url='/usuarios/login/')
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect("produtos")


def index(request):
    titulo = request.GET.get("titulo", "")
    preco_min = request.GET.get("preco_min", "")
    preco_max = request.GET.get("preco_max", "")
    ativo = request.GET.get("ativo", "")

    servicos_list = Servico.objects.filter(is_design=False)

    if titulo:
        servicos_list = servicos_list.filter(titulo__icontains=titulo)

    if preco_min:
        servicos_list = servicos_list.filter(preco_base__gte=preco_min)

    if preco_max:
        servicos_list = servicos_list.filter(preco_base__lte=preco_max)

    if ativo:
        servicos_list = servicos_list.filter(ativo=ativo)

    servicos_list = servicos_list.order_by('-id')

    paginator = Paginator(servicos_list, 10)
    page_number = request.GET.get('page')
    servicos = paginator.get_page(page_number)

    context = {
        "servicos": servicos,
        "request_get": request.GET,}
    return render(request, "index.html", context)


@has_role_decorator('Admin')
@login_required(login_url='/usuarios/login/')
def criar_servico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if form.cleaned_data.get("is_design"):
                return redirect("designs")
            return redirect("index")
    else:
        form = ServicoForm()
    return render(request, "servicos_form.html", {"form": form})

@has_role_decorator('Admin')
@login_required(login_url='/usuarios/login/')
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

@has_role_decorator('Admin')
@login_required(login_url='/usuarios/login/')
def deletar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    if request.method == "POST":
        servico.delete()
        return redirect("index")

def listar_designs(request):
    servicos_list = Servico.objects.filter(is_design=True)

    servicos_list = servicos_list.order_by('-id')

    paginator = Paginator(servicos_list, 10)
    page_number = request.GET.get('page')
    servicos = paginator.get_page(page_number)

    context = {
        "servicos": servicos,
    }
    return render(request, "designs.html", context)