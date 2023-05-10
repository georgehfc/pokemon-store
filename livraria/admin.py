from django.contrib import admin

from livraria.forms import CategoriaForm, EditoraForm, AutorForm, LivroForm
from livraria.models import Categoria, Editora, Autor, Livro


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    form = CategoriaForm
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 15
    ordering = ['id']


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    form = EditoraForm
    list_display = ('id', 'nome', 'telefone')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 15
    ordering = ['id']


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    form = AutorForm
    list_display = ('id', 'nome', 'email', 'telefone')
    list_display_links = ('id', 'nome', 'email')
    search_fields = ('nome', 'email',)
    list_per_page = 15
    ordering = ['id']

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    form = LivroForm
    list_display = ('id', 'titulo', 'categoria', 'editora', 'autor')
    list_display_links = ('id', 'titulo', 'autor')
    search_fields = ('titulo', 'autor',)
    list_filter = ('ano', )
    list_per_page = 15
    ordering = ['id']
