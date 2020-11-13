from django.db import models

class TbVoluntariado (models.Model):
    objects = models.Manager() #evitar erro no vscode
    voluntariado_id = models.AutoField(primary_key=True)
    desc_voluntariado = models.TextField(blank=False)

    pessoa = models.ForeignKey(
        'pessoas.TbPessoa',
        related_name='voluntariado',
        on_delete = models.CASCADE 
    )

    # servico = models.ManyToManyField (
    #     'servicos.TbServico',
    #     related_name='voluntariado'
    # )
    