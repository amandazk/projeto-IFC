# Generated by Django 3.1.3 on 2021-01-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oferta', '0001_initial'),
        ('voluntariado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id_servico', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_servico', models.CharField(max_length=100)),
                ('desc_servico', models.TextField(max_length=1400)),
                ('oferta', models.ManyToManyField(related_name='servicos', to='oferta.Oferta')),
                ('voluntariado', models.ManyToManyField(related_name='voluntariados', to='voluntariado.Voluntariado')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
    ]
