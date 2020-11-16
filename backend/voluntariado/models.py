from django.db import models

class TbVoluntariado (models.Model):
    objects = models.Manager() #evitar erro no vscode
    voluntariado_id = models.AutoField(primary_key=True)
    titulo_voluntariado = models.CharField(max_length=100, blank=False)
    desc_voluntariado = models.TextField(blank=False)

    pessoa = models.ForeignKey(
        'pessoas.TbPessoa',
        related_name='voluntariados',
        on_delete = models.CASCADE 
    )
    
    def __str__(self):
        return self.titulo_voluntariado

    class Meta:
        verbose_name = 'Voluntariado'
        verbose_name_plural = 'Voluntariados'
