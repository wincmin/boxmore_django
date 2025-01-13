from django.http import HttpResponseRedirect  # Usado para redirecionar o usuário para uma nova URL
from django.shortcuts import render, redirect  # 'render' para renderizar templates e 'redirect' para redirecionar o usuário
from main.bd_config import conecta_no_banco_de_dados  # Função personalizada para conectar-se ao banco de dados
from .forms import ContatoForm, LoginForm  # Importa o formulário personalizado 'ContatoForm' para manipulação de dados do usuário
from django.shortcuts import render  # Usado para renderizar templates HTML com dados contextuais
from django.contrib.auth import authenticate, login, logout  # Funções de autenticação para autenticar, logar e deslogar usuários
from django.contrib.auth.models import User  # Modelo de usuário padrão do Django, para criação e manipulação de usuários
#from django.contrib.auth.decorators import login_required  # Para proteger views que exigem um usuário autenticado (comentado)
from django.views.decorators.csrf import csrf_protect  # Ativa a proteção CSRF para uma view específica
from django.contrib.auth.decorators import login_required  # Decorator que exige que o usuário esteja autenticado para acessar a view
from django.contrib.auth.mixins import LoginRequiredMixin  # Mixin para garantir que apenas usuários autenticados acessem views baseadas em classe
from django.shortcuts import render, redirect  # 'render' para templates e 'redirect' para redirecionamentos de URL
from django.http import HttpResponseBadRequest  # Retorna uma resposta HTTP com erro 400 (Bad Request)
from django.db import transaction  # Usado para controlar transações de banco de dados (commit/rollback)
from django.http import HttpResponse, JsonResponse  # 'HttpResponse' para resposta genérica e 'JsonResponse' para respostas JSON
from django.contrib import messages  # Usado para mostrar mensagens de feedback ao usuário, como sucesso ou erro

def login(request):
    request.session['usuario_id'] = None
    request.session['perfil'] = None
    

    # Se for uma solicitação POST, valida o login
    if request.method == 'POST':
        form = LoginForm(request.POST)

        # Verifique se o formulário foi validado corretamente
        if form.is_valid():
            # Extrair as credenciais do formulário
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            # Conectar ao banco de dados
            bd = conecta_no_banco_de_dados()

            # Verificar as credenciais no banco de dados
            cursor = bd.cursor()
            cursor.execute("""
                        SELECT *
                        FROM usuarios
                        WHERE email = %s AND senha = %s;
                    """, (email, senha))
            usuario = cursor.fetchone()
            cursor.close()
            bd.close()

            # Se o usuário for encontrado
            if usuario:
                request.session['usuario_id'] = usuario[0]  # Salva o ID do usuário na sessão
                request.session['perfil'] = usuario[4]
                return redirect('index')  # Redireciona para a página inicial

            else:
                # Se não encontrar o usuário, exibe uma mensagem de erro
                mensagem_erro = 'Email ou senha inválidos.'
                return render(request, 'login.html', {'form': form, 'mensagem_erro': mensagem_erro})

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def excluirususario(request,id):
    if not request.session.get('usuario_id'):
            return redirect('/')
    else:
        try:
            # Estabelecer conexão com o banco de dados (substitua 'seu_banco_de_dados' pelo nome real)
            bd =conecta_no_banco_de_dados()
            cursor = bd.cursor()

            # Evitar SQL injection usando parâmetros nomeados
            sql = 'DELETE FROM usuarios WHERE id = %(user_id)s;'
            params = {'user_id': id}

            cursor.execute(sql, params)
            bd.commit()
            cursor.close()

            messages.success(request, 'Usuário excluído com sucesso!')
            return redirect('index')

        except Exception as e:
            print(f"Erro ao excluir usuário: {e}")
            messages.error(request, 'Falha ao excluir usuário. Tente novamente mais tarde.')
            return redirect('index')
        
def editarusuario(request,id):
    if not request.session.get('usuario_id'):
        return redirect('/')
    else:
        id_usuario = id
        bd = conecta_no_banco_de_dados()
        cursor = bd.cursor()
        cursor.execute("""
            SELECT id, nome, email
            FROM usuarios
            WHERE id = %s;
        """, (id,))
        dados_usuario = cursor.fetchone()
        cursor.close()
        bd.close()
        if request.method == 'POST':
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')    
            if not all([nome, email, senha]):
                return render(request, 'usuarios.html')
            bd = conecta_no_banco_de_dados()
            cursor = bd.cursor()
            sql = (
                """
                UPDATE usuarios
                SET nome = %s, email = %s, senha = %s
                WHERE id = %s;
                """
            )
            values = (nome, email, senha, id)
            cursor.execute(sql, values)
            bd.commit() 
            cursor.close()
            bd.close()

            return redirect('index')     
        return render(request, 'editarusuario.html',{'id': id_usuario})
    
def cadastro(request):
    if request.session.get('usuario_id'):
        return redirect('index')
    else:
        if request.method == 'POST':
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            perfil = request.POST.get('perfil') 
          


            if not all([nome, email, senha, perfil]):
                return render(request, 'cadastro.html', {'erro': 'Todos os campos são obrigatórios!'})
                
            bd = conecta_no_banco_de_dados()
            cursor = bd.cursor()
            sql = (
                """
                INSERT INTO usuarios
                SET nome = %s, email = %s, senha = %s, perfil=%s;
                """
            )
            values = (nome, email, senha,perfil)
            cursor.execute(sql, values)
            bd.commit() 
            cursor.close()
            bd.close()


            return redirect('index')    
        return render(request, 'cadastro.html')            



def carrinho(request):
    return render(request, 'carrinho.html')


def logout(request):
    request.session.flush()
    return redirect('index') 

def index(request):
    usuario_logado = None 

   
    if request.session.get('usuario_id'):
        usuario_id = request.session['usuario_id']
        bd = conecta_no_banco_de_dados()
        cursor = bd.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = %s;", (usuario_id,))
        usuario = cursor.fetchone()
        cursor.close()
        bd.close()

        if usuario:
            usuario_logado = usuario[1]  
    return render(request, 'index.html', {'usuario_logado': usuario_logado})


def sobre(request):
    if not request.session.get('usuario_id'):
         return redirect('/')
    else:
        return render(request, 'Sobre/sobre.html')

def pagamento(request):
    return render(request, 'pagamento.html')

from .models import Produto  

def busca_produtos(request):
    query = request.GET.get('query', '') 
    produtos = Produto.objects.all()  

    if query:

        produtos = produtos.filter(nome_produto__icontains=query)

    return render(request, 'index.html', {'produtos': produtos, 'query': query})

def suporte(request):
    return render(request, 'suporte.html')

def sobrenos(request):
    return render(request, 'sobrenos.html')

def carrossel(request):
    return render(request, 'carrossel.html')


def usuarios(request):

    if request.session.get('perfil') != 'administrador': 
        return redirect('index')  
  
    bd = conecta_no_banco_de_dados()
    cursor = bd.cursor()
    cursor.execute('SELECT * FROM usuarios;')
    usuarios = cursor.fetchall()
    cursor.close()
    bd.close()

    return render(request, 'usuarios.html', {"usuarios": usuarios})

        

def excluirproduto(request, id):
    if not request.session.get('usuario_id'):
        return redirect('/')
    else:
        try:
            bd = conecta_no_banco_de_dados()
            cursor = bd.cursor()

            sql = 'DELETE FROM produtos WHERE id = %(produto_id)s;'
            params = {'produto_id': id}

            cursor.execute(sql, params)
            bd.commit()
            cursor.close()

            messages.success(request, 'Produto excluído com sucesso!')
            return redirect('carrinho') 

        except Exception as e:
            print(f"Erro ao excluir produto: {e}")
            messages.error(request, 'Falha ao excluir produto. Tente novamente mais tarde.')
            return redirect('carrinho')
