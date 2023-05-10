from django import forms

from livraria.models import Categoria, Editora, Autor, Livro


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome', 'endereco', 'telefone']


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'email', 'bio', 'telefone']


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'isbn', 'codigo', 'paginas', 'ano', 'resumo', 'categoria', 'editora', 'autor']
