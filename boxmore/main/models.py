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
    nome_produto = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome_produto



