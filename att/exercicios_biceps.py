from app import app, db, Exercise

# Exercícios de BÍCEPS (25 exercícios)
exercicios_biceps = [
    {
        'name': 'Rosca Direta com Barra',
        'description': 'Em pé, segure a barra com as palmas das mãos voltadas para cima, na largura dos ombros. Flexione os cotovelos e eleve a barra até a altura dos ombros, mantendo os cotovelos junto ao corpo. Desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=kwG2ipFRgfo'
    },
    {
        'name': 'Rosca Direta com Barra EZ',
        'description': 'Em pé, segure a barra EZ com as palmas das mãos voltadas para cima. Flexione os cotovelos e eleve a barra até a altura dos ombros, mantendo os cotovelos junto ao corpo. Desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=z5bsHp2W8is'
    },
    {
        'name': 'Rosca Alternada com Halteres',
        'description': 'Em pé, segure um halter em cada mão com os braços estendidos. Flexione um cotovelo de cada vez, girando o pulso (supinação) enquanto eleva o halter, e desça controladamente antes de alternar para o outro braço.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=sAq_ocpRh_I'
    },
    {
        'name': 'Rosca Simultânea com Halteres',
        'description': 'Em pé, segure um halter em cada mão com os braços estendidos. Flexione ambos os cotovelos simultaneamente, elevando os halteres até a altura dos ombros, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=hvVt3YzJchw'
    },
    {
        'name': 'Rosca Concentrada',
        'description': 'Sentado em um banco, apoie o cotovelo na parte interna da coxa e segure um halter. Flexione o cotovelo, elevando o halter em direção ao ombro enquanto mantém o braço superior estacionário. Desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=Jvj2wV0vOYU'
    },
    {
        'name': 'Rosca Scott com Barra',
        'description': 'Sente-se no banco Scott, segure a barra com as palmas voltadas para cima. Flexione os cotovelos para elevar a barra até a altura dos ombros, depois abaixe controladamente até quase estender completamente os braços.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=LY0HeQbVkPk'
    },
    {
        'name': 'Rosca Scott com Barra EZ',
        'description': 'Sente-se no banco Scott, segure a barra EZ com as palmas voltadas para cima. Flexione os cotovelos para elevar a barra até a altura dos ombros, depois abaixe controladamente até quase estender completamente os braços.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=mvB-Q-vIeOA'
    },
    {
        'name': 'Rosca Scott com Halteres',
        'description': 'Sente-se no banco Scott, segure um halter com a palma voltada para cima. Flexione o cotovelo para elevar o halter até a altura do ombro, depois abaixe controladamente até quase estender completamente o braço. Alterne os braços ou use um em cada mão.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=Tw6JiOoE9h8'
    },
    {
        'name': 'Rosca Martelo com Halteres',
        'description': 'Em pé, segure um halter em cada mão com as palmas voltadas uma para a outra (pegada neutra). Flexione os cotovelos e eleve os halteres até a altura dos ombros, mantendo as palmas sempre na mesma posição.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=zC3nLlEvin4'
    },
    {
        'name': 'Rosca Martelo Alternada',
        'description': 'Em pé, segure um halter em cada mão com as palmas voltadas uma para a outra. Flexione um cotovelo de cada vez, elevando o halter até a altura do ombro, mantendo a pegada neutra, e desça controladamente antes de alternar para o outro braço.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=8ISbmQTbjDk'
    },
    {
        'name': 'Rosca Inversa com Barra',
        'description': 'Em pé, segure a barra com as palmas das mãos voltadas para baixo (pegada pronada), na largura dos ombros. Flexione os cotovelos e eleve a barra até a altura dos ombros, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=nRgxYX2Ve9w'
    },
    {
        'name': 'Rosca na Polia Baixa',
        'description': 'Em pé, de frente para a polia baixa, segure a barra ou alça com as palmas voltadas para cima. Flexione os cotovelos e eleve a barra até a altura dos ombros, mantendo os cotovelos junto ao corpo, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=AsAVbj7puKo'
    },
    {
        'name': 'Rosca na Polia Alta',
        'description': 'Em pé, de costas para a polia alta, segure a barra ou alça com as palmas voltadas para cima. Flexione os cotovelos e eleve a barra até a altura dos ombros, mantendo os cotovelos junto ao corpo, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=rk9DVWIfnD4'
    },
    {
        'name': 'Rosca 21',
        'description': 'Em pé, segure a barra com as palmas voltadas para cima. Faça 7 repetições da metade inferior do movimento (da extensão completa até metade do caminho), 7 repetições da metade superior (da metade do caminho até a contração completa) e 7 repetições completas.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=QZEqB6wUPxQ'
    },
    {
        'name': 'Rosca Inclinada com Halteres',
        'description': 'Sente-se em um banco inclinado, segure um halter em cada mão com os braços estendidos. Flexione os cotovelos, elevando os halteres até a altura dos ombros, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=soxrZlIl35U'
    },
    {
        'name': 'Rosca Spider com Halteres',
        'description': 'Sente-se em um banco inclinado de frente (peito apoiado no encosto), segure um halter em cada mão com os braços estendidos. Flexione os cotovelos, elevando os halteres até a altura dos ombros, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=nvufDW-2vD0'
    },
    {
        'name': 'Rosca Zottman',
        'description': 'Em pé, segure um halter em cada mão com as palmas voltadas para cima. Flexione os cotovelos e eleve os halteres até a altura dos ombros. No topo, gire os pulsos para que as palmas fiquem voltadas para baixo, e desça com essa pegada. Gire novamente para a posição inicial.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=ZI31kP6k0_Y'
    },
    {
        'name': 'Rosca Bayesiana',
        'description': 'Sente-se em um banco inclinado e apoie as costas. Deixe os braços pendurados em direção ao chão, segurando os halteres com as palmas voltadas para fora. Flexione os cotovelos, elevando os halteres, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=DWHThH0jKxM'
    },
    {
        'name': 'Rosca Cross-Body com Halter',
        'description': 'Em pé, segure um halter em cada mão. Flexione um cotovelo, elevando o halter diagonalmente em direção ao ombro oposto. Desça controladamente e repita com o outro braço.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=WJm9zA2NY8E'
    },
    {
        'name': 'Rosca com Cabo Unilateral',
        'description': 'Em pé, ao lado de uma polia baixa, segure a alça com uma mão, palma voltada para cima. Flexione o cotovelo, elevando a alça até a altura do ombro, mantendo o cotovelo junto ao corpo, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=1QdZEBggrW8'
    },
    {
        'name': 'Rosca com Corda na Polia Baixa',
        'description': 'Em pé, de frente para a polia baixa, segure a corda com as palmas voltadas uma para a outra. Flexione os cotovelos, elevando a corda até a altura dos ombros, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=bG3K67w3Z3k'
    },
    {
        'name': 'Rosca com Barra W',
        'description': 'Em pé, segure a barra W com as palmas voltadas para cima. Flexione os cotovelos, elevando a barra até a altura dos ombros, mantendo os cotovelos junto ao corpo, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=fIWP-FRFNU0'
    },
    {
        'name': 'Rosca com Halteres na Polia',
        'description': 'Em pé, segure um halter em cada mão, conectados a polias baixas. Flexione os cotovelos, elevando os halteres até a altura dos ombros, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=Rx5pFnzrh0E'
    },
    {
        'name': 'Rosca Martelo na Polia',
        'description': 'Em pé, de frente para a polia baixa, segure a alça com a pegada neutra (polegar para cima). Flexione o cotovelo, elevando a alça até a altura do ombro, mantendo o cotovelo junto ao corpo, e desça controladamente.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=crOSHnQUUzE'
    },
    {
        'name': 'Rosca com TRX',
        'description': 'Segure as alças do TRX com as palmas voltadas para cima, incline-se para trás com os braços estendidos. Flexione os cotovelos, puxando o corpo para frente, e retorne controladamente à posição inicial.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=hoNnQoA0PnU'
    }
]

# Função para adicionar os exercícios ao banco de dados
def adicionar_exercicios_biceps():
    with app.app_context():
        # Adicionar cada exercício ao banco de dados
        for exercicio in exercicios_biceps:
            # Verificar se o exercício já existe (pelo nome)
            existente = Exercise.query.filter_by(name=exercicio['name']).first()
            if not existente:
                novo_exercicio = Exercise(
                    name=exercicio['name'],
                    description=exercicio['description'],
                    muscle_group=exercicio['muscle_group'],
                    video_url=exercicio['video_url']
                )
                db.session.add(novo_exercicio)
        
        # Commit das alterações
        db.session.commit()
        print(f"Foram adicionados {len(exercicios_biceps)} exercícios de bíceps ao banco de dados!")