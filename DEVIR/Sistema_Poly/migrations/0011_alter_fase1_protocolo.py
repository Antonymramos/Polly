# Generated by Django 5.1.5 on 2025-01-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_Poly', '0010_delete_caso_fase3_atendimento_medico_vitima_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fase1',
            name='protocolo',
            field=models.CharField(max_length=17),
        ),
    ]
