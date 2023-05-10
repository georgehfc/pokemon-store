from django.urls import path

from livraria import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.IndexTemplateView.as_view(), name='index'),
    path('categorias', views.CategoriaListView.as_view(), name='categorias'),
    path('categoria/<int:pk>', views.CategoriaDetailView.as_view(), name='detalhe-categoria'),
    path('autores', views.AutoresListView.as_view(), name='autores'),
    path('autor/<int:pk>', views.AutoresDetailView.as_view(), name='detalhe-autor'),
    # path('livro/<int:pk>', views.LivrosDetailView.as_view(), name='livros'),
]
