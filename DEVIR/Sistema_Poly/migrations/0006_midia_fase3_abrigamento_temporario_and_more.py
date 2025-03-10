# Generated by Django 5.1.5 on 2025-01-19 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_Poly', '0005_fase3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Midia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='midias/')),
                ('tipo', models.CharField(blank=True, choices=[('imagem', 'Imagem'), ('video', 'Vídeo')], max_length=10, null=True)),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='fase3',
            name='abrigamento_temporario',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='Não Sei', help_text='Você quer e aceita abrigamento temporário?', max_length=10),
        ),
        migrations.AddField(
            model_name='fase3',
            name='advogado_ou_defensor',
            field=models.CharField(blank=True, help_text='Advogado ou Defensor (Detalhes, número de telefone...)', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='agressao_controle',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], help_text='O(A) agressor(a) persegue você, demonstra ciúme excessivo, tenta controlar sua vida e as coisas que você faz?', max_length=10),
        ),
        migrations.AddField(
            model_name='fase3',
            name='agressao_fisica',
            field=models.TextField(blank=True, choices=[('Queimadura', 'Queimadura'), ('Enforcamento', 'Enforcamento'), ('Sufocamento', 'Sufocamento'), ('Estrangulamento', 'Estrangulamento'), ('Tiro', 'Tiro'), ('Afogamento', 'Afogamento'), ('Facada', 'Facada'), ('Paulada', 'Paulada'), ('Soco', 'Soco'), ('Chute', 'Chute'), ('Tapa', 'Tapa'), ('Empurrão', 'Empurrão'), ('Puxão de cabelo', 'Puxão de cabelo'), ('Outra', 'Outra'), ('Nenhuma agressão física', 'Nenhuma agressão física')], null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='agressao_frequente',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='Não Sei', max_length=7),
        ),
        migrations.AddField(
            model_name='fase3',
            name='agressao_outros',
            field=models.CharField(blank=True, choices=[('Sim, filhos', 'Sim, filhos'), ('Sim, outros familiares', 'Sim, outros familiares'), ('Sim, amigos', 'Sim, amigos'), ('Sim, colegas de trabalho', 'Sim, colegas de trabalho'), ('Sim, outras pessoas', 'Sim, outras pessoas'), ('Sim, animais', 'Sim, animais'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], help_text='Escolha as pessoas ou grupos que foram ameaçados ou agredidos.', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='agressao_relacionamento',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=3),
        ),
        migrations.AddField(
            model_name='fase3',
            name='agressao_sexual',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], help_text='O(A) agressor(a) já obrigou você a ter relações sexuais ou praticar atos sexuais contra a sua vontade?', max_length=10),
        ),
        migrations.AddField(
            model_name='fase3',
            name='ajuda_registro',
            field=models.CharField(blank=True, choices=[('Sim, no formulário de risco', 'Sim, no formulário de risco'), ('Sim, na MPU', 'Sim, na MPU'), ('Sim, em ambos (Formulário e MPU)', 'Sim, em ambos (Formulário e MPU)'), ('Não', 'Não')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='alteracao_informacoes',
            field=models.CharField(choices=[('Sim - na DEVIR', 'Sim - na DEVIR'), ('Sim - apenas no FORMULÁRIO DE RISCO', 'Sim - apenas no FORMULÁRIO DE RISCO'), ('Sim - apenas MPU', 'Sim - apenas MPU'), ('Sim - em ambos (FORMULÁRIO E MPU)', 'Sim - em ambos (FORMULÁRIO E MPU)'), ('Não', 'Não')], default='Não', max_length=50),
        ),
        migrations.AddField(
            model_name='fase3',
            name='ameaca',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim - utilizando arma de fogo', 'Sim - utilizando arma de fogo'), ('Sim - utilizando faca', 'Sim - utilizando faca'), ('Sim - de outra forma', 'Sim - de outra forma')], default='Não', max_length=50),
        ),
        migrations.AddField(
            model_name='fase3',
            name='ameacas_novo_relacionamento',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='Não Sei', max_length=10),
        ),
        migrations.AddField(
            model_name='fase3',
            name='arma_fogo',
            field=models.CharField(choices=[('Sim, usou', 'Sim, usou'), ('Sim, ameaçou usar', 'Sim, ameaçou usar'), ('Tem fácil acesso', 'Tem fácil acesso'), ('Não Sei', 'Não Sei'), ('Não', 'Não')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='fase3',
            name='atendimento_medico',
            field=models.CharField(blank=True, choices=[('SIM - a vítima gostaria de encaminhamento para atendimento médico/hospitalar', 'SIM - a vítima gostaria de encaminhamento para atendimento médico/hospitalar'), ('NÃO - preciso de encaminhamento médico', 'NÃO - preciso de encaminhamento médico')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='atendimento_psicologico',
            field=models.CharField(blank=True, choices=[('SIM - a vítima gostaria de encaminhamento para atendimento psicológico', 'SIM - a vítima gostaria de encaminhamento para atendimento psicológico'), ('SIM - a vítima faz uso de medicamentos para depressão, ansiedade ou tratamentos psíquicos', 'SIM - a vítima faz uso de medicamentos para depressão, ansiedade ou tratamentos psíquicos'), ('Não Quero', 'Não Quero')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='bairro_comunidade_rural',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='Não Sei', help_text='Você considera que mora em bairro, comunidade, área rural ou local de risco de violência?', max_length=10),
        ),
        migrations.AddField(
            model_name='fase3',
            name='como_soube',
            field=models.CharField(blank=True, choices=[('TV', 'TV'), ('Internet', 'Internet'), ('Rádio', 'Rádio'), ('Amigos', 'Amigos'), ('Familiares', 'Familiares'), ('Um Policial de Outra Delegacia', 'Um Policial de Outra Delegacia'), ('CRAS', 'CRAS'), ('CREAS', 'CREAS'), ('CRAMS', 'CRAMS'), ('Não Houve Sucesso no Contato com a Requerente', 'Não Houve Sucesso no Contato com a Requerente')], help_text='Como você soube desse serviço da Delegacia Virtual e da Medida Protetiva?', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='comportamentos',
            field=models.CharField(blank=True, choices=[('Se não for minha, não será de mais ninguém', 'Se não for minha, não será de mais ninguém'), ('Perturbou, perseguiu ou vigiou você nos locais que frequenta', 'Perturbou, perseguiu ou vigiou você nos locais que frequenta'), ('Proibiu você de visitar familiares ou amigos', 'Proibiu você de visitar familiares ou amigos'), ('Proibiu você de trabalhar ou estudar', 'Proibiu você de trabalhar ou estudar'), ('Fez telefonemas, enviou mensagens ou e-mails de forma insistente', 'Fez telefonemas, enviou mensagens ou e-mails de forma insistente'), ('Impediu você de ter acesso a dinheiro, conta bancária ou outros bens', 'Impediu você de ter acesso a dinheiro, conta bancária ou outros bens'), ('Teve outros comportamentos de ciúme excessivo e de controle sobre você', 'Teve outros comportamentos de ciúme excessivo e de controle sobre você'), ('Nenhum dos comportamentos acima listados', 'Nenhum dos comportamentos acima listados')], help_text='Selecione os comportamentos do agressor', max_length=255),
        ),
        migrations.AddField(
            model_name='fase3',
            name='conflito_guarda',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='Não Sei', max_length=10),
        ),
        migrations.AddField(
            model_name='fase3',
            name='consequencias_lesao',
            field=models.CharField(blank=True, choices=[('Passei por atendimento em hospital ou posto', 'Passei por atendimento em hospital ou posto'), ('Não passei por atendimento', 'Não passei por atendimento'), ('Não houve lesão física aparente', 'Não houve lesão física aparente'), ('Sofri apenas violência psicológica', 'Sofri apenas violência psicológica'), ('Não', 'Não'), ('Outro', 'Outro')], help_text='O que houve com a vítima após essas lesões (FÍSICAS ou SEXUAIS anteriores por esse agressor)?', max_length=100),
        ),
        migrations.AddField(
            model_name='fase3',
            name='cor_raca',
            field=models.CharField(choices=[('Branca', 'Branca'), ('Preta', 'Preta'), ('Parda', 'Parda'), ('Amarela', 'Amarela'), ('Oriental', 'Oriental'), ('Indígena', 'Indígena')], default='Branca', help_text='Com qual cor/raça você se identifica?', max_length=10),
        ),
        migrations.AddField(
            model_name='fase3',
            name='data_hora_fase3',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='fase3',
            name='deficiencia_ou_doenca',
            field=models.CharField(blank=True, help_text="Caso tenha respondido sim à pergunta anterior, especifique a deficiência ou doença degenerativa. Em caso de não, preenche com 'Não se Aplica'", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='delegacia_busca_informacao',
            field=models.CharField(blank=True, choices=[('Sim, da minha cidade', 'Sim, da minha cidade'), ('Sim, outra delegacia e me encaminharam', 'Sim, outra delegacia e me encaminharam'), ('Não', 'Não')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='dependente_financeiramente',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='Não Sei', help_text='Você se considera dependente financeiramente do(a) agressor(a)?', max_length=10),
        ),
        migrations.AddField(
            model_name='fase3',
            name='dependentes_nome_idade',
            field=models.CharField(blank=True, help_text='Informe abaixo o nome e a idade dos dependentes que estarão neste termo juntamente com a Requerente.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='descumprimento_medida',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='Não Sei', max_length=7),
        ),
        migrations.AddField(
            model_name='fase3',
            name='dificuldade_financeira',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='', max_length=7),
        ),
        migrations.AddField(
            model_name='fase3',
            name='doenca_mental',
            field=models.CharField(choices=[('Sim, com uso de medicação', 'Sim, com uso de medicação'), ('Sim, sem uso de medicação', 'Sim, sem uso de medicação'), ('Não', 'Não'), ('Não sei', 'Não sei')], default='Não sei', max_length=30),
        ),
        migrations.AddField(
            model_name='fase3',
            name='especificar_delegacia',
            field=models.TextField(blank=True, help_text="Em caso de 'Sim, outra delegacia e me encaminharam', especifique qual a Delegacia. Caso contrário, preencha com 'Não se Aplica'.", null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='filho_com_deficiencia',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Se Aplica', 'Não Se Aplica')], default='Não', max_length=20),
        ),
        migrations.AddField(
            model_name='fase3',
            name='filhos_com_agressor',
            field=models.CharField(choices=[('Sim, 1 filho(a)', 'Sim, 1 filho(a)'), ('Sim, 2 filhos(as)', 'Sim, 2 filhos(as)'), ('Sim, 3 filhos(as)', 'Sim, 3 filhos(as)'), ('Sim, mais de 3 filhos(as)', 'Sim, mais de 3 filhos(as)'), ('Não', 'Não')], default='Não', max_length=30),
        ),
        migrations.AddField(
            model_name='fase3',
            name='filhos_presenciaram',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='Não Sei', max_length=10),
        ),
        migrations.AddField(
            model_name='fase3',
            name='gravida_ou_bebe',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='Não Sei', max_length=10),
        ),
        migrations.AddField(
            model_name='fase3',
            name='informacoes_beneficios',
            field=models.CharField(choices=[('Sim, totalmente', 'Sim, totalmente'), ('Sim, parcialmente. Tem emprego mas não se autosustenta', 'Sim, parcialmente. Tem emprego mas não se autosustenta'), ('Não. Tenho emprego e consigo me sustentar', 'Não. Tenho emprego e consigo me sustentar'), ('Não se Aplica', 'Não se Aplica')], default='Não se Aplica', help_text='Deseja receber informações sobre benefícios sociais?', max_length=54),
        ),
        migrations.AddField(
            model_name='fase3',
            name='medidas_protetivas',
            field=models.TextField(blank=True, help_text='Escolha as medidas protetivas que foram aplicadas'),
        ),
        migrations.AddField(
            model_name='fase3',
            name='moradia_cedida',
            field=models.CharField(blank=True, help_text="Em caso de moradia cedida, especificar a seguir por quem. Caso contrário, preencher com 'Não se Aplica'.", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='motivos_retorno',
            field=models.JSONField(blank=True, default=list, help_text='Escolha os motivos do retorno (se aplicável).', null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='natureza_dos_crimes',
            field=models.CharField(blank=True, help_text='Natureza dos Crimes (Ameaça; Agressão... Quando possível (por agendamento ou telefone) fazer a certidão para a vítima no cartório da DP)', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='numero_processo_mpu',
            field=models.CharField(blank=True, help_text='Informe o número do processo de MPU anterior.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='policial_responsavel',
            field=models.CharField(choices=[('MARIA NAZARÉ', 'MARIA NAZARÉ'), ('DANIELLA PORTO', 'DANIELLA PORTO'), ('PAULA TIMBÓ', 'PAULA TIMBÓ'), ('THAYSA ALBUQUERQUE', 'THAYSA ALBUQUERQUE'), ('YASMIM CRISTINA', 'YASMIM CRISTINA'), ('AMANDA NASCIMENTO', 'AMANDA NASCIMENTO'), ('PAULA WILTSHIRE', 'PAULA WILTSHIRE'), ('CARINA QUEIROZ', 'CARINA QUEIROZ')], default='MARIA NAZARÉ', max_length=50),
        ),
        migrations.AddField(
            model_name='fase3',
            name='qtd_filhos',
            field=models.CharField(choices=[('1 filho(a)', '1 filho(a)'), ('2 filhos(as)', '2 filhos(as)'), ('3 filhos(as)', '3 filhos(as)'), ('Mais de 3 filhos(as)', 'Mais de 3 filhos(as)'), ('Não possuo filhos', 'Não possuo filhos')], default='Não possuo filhos', max_length=20),
        ),
        migrations.AddField(
            model_name='fase3',
            name='reataram_relacionamento',
            field=models.CharField(blank=True, choices=[('Sim - uma vez', 'Sim - uma vez'), ('Sim - duas vezes', 'Sim - duas vezes'), ('Sim - várias vezes', 'Sim - várias vezes'), ('Não - essa foi a primeira vez que terminamos por esse motivo', 'Não - essa foi a primeira vez que terminamos por esse motivo'), ('Nunca houve separação', 'Nunca houve separação'), ('Não Houve Retorno', 'Não Houve Retorno')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='registro_ocorrencia',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=3),
        ),
        migrations.AddField(
            model_name='fase3',
            name='separacao_recente',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=3),
        ),
        migrations.AddField(
            model_name='fase3',
            name='situacao_moradia',
            field=models.CharField(choices=[('Própria', 'Própria'), ('Alugada', 'Alugada'), ('Cedida', 'Cedida')], default='Própria', help_text='Qual sua situação de moradia?', max_length=10),
        ),
        migrations.AddField(
            model_name='fase3',
            name='status_fase_3',
            field=models.CharField(choices=[('Em Andamento', 'Em Andamento'), ('Concluída', 'Concluída'), ('Desistência na Fase 3', 'Desistência na Fase 3')], default='Em Andamento', max_length=21),
        ),
        migrations.AddField(
            model_name='fase3',
            name='suicidio',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='', max_length=7),
        ),
        migrations.AddField(
            model_name='fase3',
            name='telefone_endereco_whatsapp',
            field=models.TextField(blank=True, help_text="Em caso de Não, preencher com 'Não se Aplica'.", null=True),
        ),
        migrations.AddField(
            model_name='fase3',
            name='uso_abusivo',
            field=models.CharField(choices=[('Sim, de álcool', 'Sim, de álcool'), ('Sim, de drogas', 'Sim, de drogas'), ('Sim, de medicamentos', 'Sim, de medicamentos'), ('Não', 'Não'), ('Não sei', 'Não sei')], default='Não', max_length=20),
        ),
        migrations.AddField(
            model_name='fase3',
            name='videoconferencia',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Sim, mas não quis mostrar a imagem dela (sem câmera ligada)', 'Sim, mas não quis mostrar a imagem dela (sem câmera ligada)'), ('Não - o atendimento foi realizado por mensagem', 'Não - o atendimento foi realizado por mensagem'), ('Não - o atendimento foi realizado por ligação', 'Não - o atendimento foi realizado por ligação'), ('Não houve gravação do vídeo', 'Não houve gravação do vídeo')], default='Sim', max_length=100),
        ),
        migrations.AddField(
            model_name='fase3',
            name='violencia_gravidez',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não Sei', 'Não Sei')], default='Não Sei', max_length=10),
        ),
    ]
