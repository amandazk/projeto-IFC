from django.db import models

class Noticia(models.Model):
    objects = models.Manager() #evitar erro no vscode
    noticia_id =  models.AutoField(primary_key=True)
    titulo_noticia = models.CharField(max_length=300, blank=False)
    subtitulo_noticia = models.CharField(max_length=300, blank=False)
    desc_noticia = models.TextField(max_length=10000, blank=False)

    pessoas = models.ForeignKey(
        'pessoas.Pessoa',
        related_name='noticia',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.titulo_noticia

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
