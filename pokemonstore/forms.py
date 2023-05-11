from django import forms

from pokemonstore.models import Pokemon, Pokeball


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name', 'poke_type', 'weight', 'height']

class PokeballForm(forms.ModelForm):
    class Meta:
        model = Pokeball
        fields = ['name', 'catch_rate']


###########################
# class EditoraForm(forms.ModelForm):
#     class Meta:
#         model = Editora
#         fields = ['nome', 'endereco', 'telefone']

# class AutorForm(forms.ModelForm):
#     class Meta:
#         model = Autor
#         fields = ['nome', 'email', 'bio', 'telefone']

# class LivroForm(forms.ModelForm):
#     class Meta:
#         model = Livro
#         fields = ['titulo', 'isbn', 'codigo', 'paginas', 'ano', 'resumo', 'categoria', 'editora', 'autor']
