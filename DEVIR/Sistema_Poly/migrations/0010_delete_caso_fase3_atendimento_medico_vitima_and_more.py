# Generated by Django 5.1.5 on 2025-01-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_Poly', '0009_alter_fase2_protocolo_fase2_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Caso',
        ),
        migrations.AddField(
            model_name='fase3',
            name='atendimento_medico_vitima',
            field=models.CharField(blank=True, choices=[('SIM - a vítima gostaria de encaminhamento para atendimento médico/hospitalar', 'SIM - a vítima gostaria de encaminhamento para atendimento médico/hospitalar'), ('NÃO - preciso de encaminhamento médico', 'NÃO - preciso de encaminhamento médico')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='deficiencia_vitima',
            field=models.CharField(blank=True, help_text="Caso tenha respondido sim à pergunta anterior, especifique a deficiência ou doença degenerativa. Em caso de não, preenche com 'Não se Aplica'", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='atendimento_medico',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], help_text='Você necessitou de atendimento médico e/ou internação após algumas dessas agressões?', max_length=10),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='deficiencia_ou_doenca',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=3),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='policial_responsavel',
            field=models.CharField(choices=[('MARIA NAZARÉ', 'MARIA NAZARÉ'), ('DANIELLA PORTO', 'DANIELLA PORTO'), ('PAULA TIMBÓ', 'PAULA TIMBÓ'), ('THAYSA ALBUQUERQUE', 'THAYSA ALBUQUERQUE'), ('YASMIM CRISTINA', 'YASMIM CRISTINA'), ('AMANDA NASCIMENTO', 'AMANDA NASCIMENTO'), ('PAULA WILTSHIRE', 'PAULA WILTSHIRE'), ('CARINA QUEIROZ', 'CARINA QUEIROZ')], max_length=50),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='protocolo_devir',
            field=models.CharField(max_length=17, unique=True),
        ),
    ]
