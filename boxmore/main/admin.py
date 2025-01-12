from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'preco', 'marca', 'imagem')

admin.site.register(Produto, ProdutoAdmin)
