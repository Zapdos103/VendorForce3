# Generated by Django 5.0.3 on 2024-07-31 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios2', '0005_alter_formulario_funcionarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='texto',
        ),
        migrations.AddField(
            model_name='formulario',
            name='textoteste',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]