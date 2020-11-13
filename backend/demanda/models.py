from django.db import models

class TbDemanda(models.Model):
    objects = models.Manager() #evitar erro no vscode
    demanda_id =  models.AutoField(primary_key=True)
    titulo_demanda = models.CharField(max_length=100, blank=False)
    data_demanda = models.DateField()
    rua_servico = models.CharField(max_length=100)
    numero_endereco_servico = models.CharField(max_length=10)
    bairro_servico = models.CharField(max_length=100)
    cidade_servico = models.CharField(max_length=100)
    desc_demanda = models.TextField(max_length=1400, blank=False)

    # servico = models.ForeignKey(
    #     'servico.TbServico',
    #     related_name='demanda',
    #     on_delete=models.CASCADE,
    # )

    pessoas = models.ForeignKey(
        'pessoas.TbPessoa',
        related_name='demanda',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.titulo_demanda

    class Meta:
        verbose_name = 'Demanda'
        verbose_name_plural = 'Demandas'
