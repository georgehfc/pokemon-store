from django.db import models
from django.urls import reverse


class Pokemon(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    poke_type = models.CharField(max_length=50, unique=True, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)

    def __str__(self):
        return self.name

    # def __str__(self) -> str:
    #     return super().__str__()

    def get_absolute_url(self):
        return reverse('pokemon-details', kwargs={'pk': self.pk})

    objects = models.Manager()

class Pokeball(models.Model):
    name = models.CharField(max_length=50, null=False)
    catch_rate = models.IntegerField(null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pokeball-details', kwargs={'pk': self.pk})

    objects = models.Manager()



####################
# class Editora(models.Model):
#     nome = models.CharField(max_length=255, unique=True, null=False)
#     endereco = models.TextField(null=False)
#     telefone = models.CharField(max_length=20)

#     def __str__(self):
#         return self.nome

#     def get_absolute_url(self):
#         return reverse('editora-detail', kwargs={'pk': self.pk})

#     objects = models.Manager()

# class Livro(models.Model):
#     titulo = models.CharField(null=False)
#     isbn = models.CharField(max_length=20, unique=True, null=False)
#     codigo = models.CharField(max_length=10, unique=True, null=False)
#     paginas = models.IntegerField(null=False)
#     ano = models.IntegerField(null=False)
#     resumo = models.TextField(null=False)
#     categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
#     editora = models.ForeignKey(Editora, on_delete=models.RESTRICT)
#     # edicao = models.IntegerField()
#     # idioma = models.CharField(max_length=20)
#     autor = models.ForeignKey(Autor, on_delete=models.RESTRICT)

#     def __str__(self):
#         return self.titulo

#     def get_absolute_url(self):
#         return reverse('detalhe-livro', kwargs={'pk': self.pk})

#     objects = models.Manager()
