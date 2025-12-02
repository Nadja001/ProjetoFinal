from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    preco_base = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='images/', blank=True)
    is_design = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
