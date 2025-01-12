from django import forms
from .models import Contato,Usuario, Produto


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']


class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'senha'] 
  
    email = forms.EmailField(
        label='Email', 
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email', 'class':'inputlogin'})
    )
    senha = forms.CharField(
        label='Senha', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha', 'class':'inputlogin'})
    )



class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'preco', 'marca', 'imagem']
