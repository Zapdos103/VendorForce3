# Generated by Django 5.0.3 on 2024-07-31 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('formularios2', '0004_rename_formularios_formulario_funcionarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='funcionarios',
            field=models.ManyToManyField(blank=True, to='empresas.funcionario'),
        ),
    ]