# Generated by Django 5.1.4 on 2025-01-24 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_Poly', '0013_alter_fase4_agressao_alter_fase4_mpu_enviado_ao_tj_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fase',
        ),
        migrations.DeleteModel(
            name='Protocolo',
        ),
    ]
