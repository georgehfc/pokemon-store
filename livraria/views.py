from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from livraria.models import Livro, Autor, Categoria


def index(request):
    quantidade_livros = Livro.objects.all().count()
    quantidade_autores = Autor.objects.all().count()

    context = {
        'quantidade_livros': quantidade_livros,
        'quantidade_autores': quantidade_autores,
    }

    return render(request, 'index.html', context=context)


# class IndexTemplateView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['quantidade_livros'] = Livro.objects.all().count()
#         context['quantidade_autores'] = Autor.objects.all().count()
#         return context


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias.html'


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        livros = Livro.objects.filter(categoria=context.get('categoria').id)
        context["livros_list"] = livros
        return context


class AutoresListView(ListView):
    model = Autor
    template_name = 'autores.html'


class AutoresDetailView(DetailView):
    model = Autor
    template_name = 'autor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        livros = Livro.objects.filter(autor_id=context.get('autor').id)
        context["livros_list"] = livros
        return context
