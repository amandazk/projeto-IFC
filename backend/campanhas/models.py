from django.db import models

class TbCampanha(models.Model):
    objects = models.Manager() #evitar erro no vscode
    campanha_id = models.AutoField(primary_key=True)
    ativo = models.BooleanField(default=False)
    titulo_campanha = models.CharField(max_length=100, blank=False)
    desc_campanha = models.TextField(max_length=1400, blank=False)
    dt_inicio_campanha = models.DateField(blank=False)
    dt_fim_campanha = models.DateField()
    rua_campanha = models.CharField(max_length=100)
    numero_endereco_campanha = models.CharField(max_length=10)
    bairro_campanha = models.CharField(max_length=100)
    cidade_campanha = models.CharField(max_length=100)
    link_campanha = models.URLField()

    pessoa = models.ForeignKey(
        'pessoas.TbPessoa',
        related_name='campanhas',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.titulo_campanha

    class Meta:
        verbose_name = 'Campanha'
        verbose_name_plural = 'Campanhas'




