# Generated by Django 5.1.4 on 2025-02-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_Poly', '0029_alter_fase3_abrigamento_temporario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fase3',
            name='advogado_ou_defensor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='deficiencia_vitima',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='especificar_delegacia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fase3',
            name='telefone_endereco_whatsapp',
            field=models.TextField(blank=True, null=True),
        ),
    ]
