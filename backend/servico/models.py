from django.db import models

class TbServico(models.Model):
    objects = models.Manager() #evitar erro no vscode
    id_servico = models.AutoField(primary_key=True)
    titulo_servico = models.CharField(max_length=100, blank=False)
    desc_servico = models.TextField(max_length=1400, blank=False)

    oferta = models.ManyToManyField(
        'oferta.TbOferta',
        related_name='servicos'
    )
    
    demanda = models.ManyToManyField(
        'demanda.TbDemanda',
        related_name='demandas'
    )
    
    voluntariado = models.ManyToManyField(
        'voluntariado.TbVoluntariado',
        related_name='voluntariados'
    )
    
    
    def _str_(self):
        return self.titulo_servico
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
