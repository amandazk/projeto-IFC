from django.db import models

class TbPessoa(models.Model):
    objects = models.Manager() #evitar erro no vscode
    pessoa_id = models.AutoField(primary_key=True)
    cpf_pessoa = models.CharField(max_length=11, unique=True, blank=False)
    nome_pessoa = models.CharField(max_length=200, blank=False)
    nasc_pessoa = models.DateField()
    email_pessoa = models.EmailField(blank=False)

    fone = models.ForeignKey(
        'pessoas.TbFone',
        related_name='pessoas',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nome_pessoa

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


