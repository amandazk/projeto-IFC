# Generated by Django 3.1.3 on 2020-12-07 21:42

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbFone',
            fields=[
                ('fone_id', models.AutoField(primary_key=True, serialize=False)),
                ('nr_fone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
            options={
                'verbose_name': 'Fone',
                'verbose_name_plural': 'Fones',
            },
        ),
        migrations.CreateModel(
            name='TbPessoa',
            fields=[
                ('pessoa_id', models.AutoField(primary_key=True, serialize=False)),
                ('cpf_pessoa', models.CharField(max_length=11, unique=True)),
                ('nome_pessoa', models.CharField(max_length=200)),
                ('nasc_pessoa', models.DateField()),
                ('email_pessoa', models.EmailField(max_length=254)),
                ('fone', models.ManyToManyField(related_name='pessoas', to='pessoas.TbFone')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
    ]
