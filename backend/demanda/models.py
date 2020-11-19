from django.db import models
# from django.contrib.gis.db import models


class TbDemanda(models.Model):
    objects = models.Manager()  # evitar erro no vscode
    demanda_id = models.AutoField(primary_key=True)
    titulo_demanda = models.CharField(max_length=100, blank=False)
    data_demanda = models.DateField()
    # local = models.PointField(null=True)
    rua_servico = models.CharField(max_length=100)
    numero_endereco_servico = models.CharField(max_length=10)
    bairro_servico = models.CharField(max_length=100)
    cidade_servico = models.CharField(max_length=100)
    desc_demanda = models.TextField(max_length=1400, blank=False)

    pessoas = models.ForeignKey(
        'pessoas.TbPessoa',
        related_name='demanda',
        on_delete=models.CASCADE,
    )

    servico = models.ManyToManyField(
        'servico.TbServico',
        related_name='demanda'
    )

    def __unicode__(self):
        return self.demanda_id

    class Meta:
        verbose_name = 'Demanda'
        verbose_name_plural = 'Demandas'
