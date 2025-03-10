# Generated by Django 5.1.4 on 2025-02-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_Poly', '0034_alter_fase1_data_fato_alter_fase1_idade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fase4',
            name='agressao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fase4',
            name='data_atendimento_fase4',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fase4',
            name='mpu_enviado_ao_tj',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fase4',
            name='numero_processo_protecao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fase4',
            name='policial_finalizacao_fase4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fase4',
            name='protocolo',
            field=models.CharField(blank=True, max_length=17, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='fase4',
            name='representou_crime',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fase4',
            name='situacao_mpu',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fase4',
            name='status_fase',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
