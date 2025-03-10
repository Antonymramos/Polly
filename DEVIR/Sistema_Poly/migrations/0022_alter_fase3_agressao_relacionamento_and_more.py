# Generated by Django 5.1.4 on 2025-01-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_Poly', '0021_alter_fase3_abrigamento_temporario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fase3',
            name='agressao_relacionamento',
            field=models.CharField(default='Não', max_length=3),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='ajuda_registro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='alteracao_informacoes',
            field=models.CharField(default='Não', max_length=50),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='atendimento_medico_vitima',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='atendimento_psicologico',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='como_soube',
            field=models.CharField(blank=True, help_text='Como você soube desse serviço da Delegacia Virtual e da Medida Protetiva?', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='delegacia_busca_informacao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='motivos_retorno',
            field=models.TextField(blank=True, help_text='Escolha os motivos do retorno (se aplicável).', null=True),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='policial_responsavel',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='reataram_relacionamento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='status_fase',
            field=models.CharField(default='Em Andamento', max_length=21),
        ),
    ]
