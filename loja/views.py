from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .forms import ProdutoForm, ServicoForm
from .models import Produto, Servico
from django.db.models import Q
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.decorators import login_required

def lista_produtos(request):
    search = request.GET.get("search", "")

    produtos_list = Produto.objects.all()

    if search:
        produtos_list = produtos_list.filter(
            Q(nome__icontains=search)
        )

    produtos_list = produtos_list.order_by('-id')

    paginator = Paginator(produtos_list, 10)
    page_number = request.GET.get('page')
    produtos = paginator.get_page(page_number)

    context = {
        "produtos": produtos,
        "search": search,
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
    search = request.GET.get("search", "")

    servicos_list = Servico.objects.filter(is_design=False)

    if search:
        servicos_list = servicos_list.filter(
            Q(titulo__icontains=search)
        )

    servicos_list = servicos_list.order_by('-id')

    paginator = Paginator(servicos_list, 10)
    page_number = request.GET.get('page')
    servicos = paginator.get_page(page_number)

    context = {
        "servicos": servicos,
        "search": search,
    }

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
    search = request.GET.get("search", "")

    servicos_list = Servico.objects.filter(is_design=True)

    if search:
        servicos_list = servicos_list.filter(
            Q(titulo__icontains=search)
        )

    servicos_list = servicos_list.order_by('-id')

    paginator = Paginator(servicos_list, 10)
    page_number = request.GET.get('page')
    servicos = paginator.get_page(page_number)

    context = {
        "servicos": servicos,
        "search": search,
    }
    return render(request, "designs.html", context)