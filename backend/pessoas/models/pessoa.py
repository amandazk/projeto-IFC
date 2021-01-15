from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    objects = models.Manager() #evitar erro no vscode
    pessoa_id = models.AutoField(primary_key=True)
    cpf_pessoa = models.CharField(max_length=11, unique=True, blank=False)
    nome_pessoa = models.CharField(max_length=200, blank=False)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=30, blank=False)
    nasc_pessoa = models.DateField()
    email_pessoa = models.EmailField(blank=False)

    fone = models.ManyToManyField(
        'pessoas.Fone',
        related_name='pessoas'
    )

    user = models.OneToOneField(
    User,
    on_delete = models.CASCADE
    )


    def __str__(self):
        return self.nome_pessoa

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


