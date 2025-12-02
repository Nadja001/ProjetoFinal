from django import forms

from .models import Produto, Servico


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['titulo', 'preco_base', 'descricao', 'imagem', 'is_design']


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'descricao', 'estoque', 'imagem']
