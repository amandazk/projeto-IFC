from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Fone(models.Model):
    objects = models.Manager()
    fone_id = models.AutoField(primary_key=True)
    nr_fone = PhoneNumberField(blank = False)

    def __unicode__(self):
        return self.fone_id

    class Meta:
        verbose_name = 'Fone'
        verbose_name_plural = 'Fones'