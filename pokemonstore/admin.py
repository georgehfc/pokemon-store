from django.contrib import admin

from pokemonstore.forms import PokemonForm, PokeballForm
from pokemonstore.models import Pokemon, Pokeball


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    form = PokemonForm
    list_display = ('id', 'name', 'poke_type', 'weight', 'height',)
    list_display_links = ('id', 'name', 'poke_type', 'weight', 'height',)
    search_fields = ('name',)
    list_per_page = 15
    ordering = ['id']

@admin.register(Pokeball)
class PokeballAdmin(admin.ModelAdmin):
    form = PokeballForm
    list_display = ('id', 'name', 'catch_rate',)
    list_display_links = ('id', 'name', 'catch_rate',)
    search_fields = ('name',)
    list_per_page = 15
    ordering = ['id']



###################################
# @admin.register(Editora)
# class EditoraAdmin(admin.ModelAdmin):
#     form = EditoraForm
#     list_display = ('id', 'nome', 'telefone')
#     list_display_links = ('id', 'nome')
#     search_fields = ('nome',)
#     list_per_page = 15
#     ordering = ['id']

# @admin.register(Autor)
# class AutorAdmin(admin.ModelAdmin):
#     form = AutorForm
#     list_display = ('id', 'nome', 'email', 'telefone')
#     list_display_links = ('id', 'nome', 'email')
#     search_fields = ('nome', 'email',)
#     list_per_page = 15
#     ordering = ['id']

# @admin.register(Livro)
# class LivroAdmin(admin.ModelAdmin):
#     form = LivroForm
#     list_display = ('id', 'titulo', 'categoria', 'editora', 'autor')
#     list_display_links = ('id', 'titulo', 'autor')
#     search_fields = ('titulo', 'autor',)
#     list_filter = ('ano', )
#     list_per_page = 15
#     ordering = ['id']
