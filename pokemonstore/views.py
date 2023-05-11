from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from pokemonstore.models import Pokemon, Pokeball

def index(request):
    all_pokemon = Pokemon.objects.all().count()
    all_pokeball = Pokeball.objects.all().count()

    context = {
        'all_pokemon': all_pokemon,
        'all_pokeball': all_pokeball,
    }

    return render(request, 'index.html', context=context)

class PokemonListView(ListView):
    model = Pokemon
    template_name = 'pokemons.html'

class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = 'pokemon.html'

class PokeballListView(ListView):
    model = Pokeball
    template_name = 'pokeballs.html'

class PokeballDetailView(DetailView):
    model = Pokeball
    template_name = 'pokeball.html'




####################################
# class IndexTemplateView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['quantidade_livros'] = Livro.objects.all().count()
#         context['quantidade_autores'] = Autor.objects.all().count()
#         return context

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         livros = Livro.objects.filter(categoria=context.get('categoria').id)
#         context["livros_list"] = livros
#         return context

# class AutoresListView(ListView):
#     model = Autor
#     template_name = 'autores.html'

# class AutoresDetailView(DetailView):
#     model = Autor
#     template_name = 'autor.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         livros = Livro.objects.filter(autor_id=context.get('autor').id)
#         context["livros_list"] = livros
#         return context
