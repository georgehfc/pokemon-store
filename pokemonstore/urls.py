from django.urls import path

from pokemonstore import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemons/', views.PokemonListView.as_view(), name='pokemon-list'),
    path('pokemon/<int:pk>', views.PokemonDetailView.as_view(), name='pokemon-details'),
    path('pokeballs/', views.PokeballListView.as_view(), name='pokeball-list'),
    path('pokeball/<int:pk>', views.PokeballDetailView.as_view(), name='pokeball-details'),
    # path('', views.IndexTemplateView.as_view(), name='index'),
    # path('categorias', views.CategoriaListView.as_view(), name='categorias'),
    # path('categoria/<int:pk>', views.CategoriaDetailView.as_view(), name='detalhe-categoria'),
    # path('autores', views.AutoresListView.as_view(), name='autores'),
    # path('autor/<int:pk>', views.AutoresDetailView.as_view(), name='detalhe-autor'),
    # path('livro/<int:pk>', views.LivrosDetailView.as_view(), name='livros'),
]
