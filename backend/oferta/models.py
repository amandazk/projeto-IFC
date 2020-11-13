from django.db import models

class TbOferta(models.Model):
    objects = models.Manager() #evitar erro no vscode
    oferta_id =  models.AutoField(primary_key=True)
    dt_oferta = models.DateField(blank=False)
    titulo_oferta = models.CharField(max_length=100, blank=False)
    rua_oferta = models.CharField(max_length=100)
    numero_endereco_oferta = models.CharField(max_length=10)
    bairro_oferta = models.CharField(max_length=100)
    cidade_oferta = models.CharField(max_length=100)

    pessoas = models.ForeignKey(
        'pessoas.TbPessoa',
        related_name='oferta',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.titulo_oferta

    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'

