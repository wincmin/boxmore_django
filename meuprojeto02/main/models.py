from django.db import models
class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mensagem = models.TextField()

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome_produto = models.CharField(max_length=200, verbose_name="Nome do Produto")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    marca = models.CharField(max_length=100, blank=True, null=True, verbose_name="Marca")
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, verbose_name="Imagem do Produto")

    def __str__(self):
        return self.nome_produto
