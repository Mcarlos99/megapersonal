from app import app, db, Exercise

# Exercícios de OMBROS (25 exercícios)
exercicios_ombros = [
    {
        'name': 'Desenvolvimento com Barra',
        'description': 'Sentado ou em pé, segure a barra na altura dos ombros com as mãos um pouco mais afastadas que a largura dos ombros. Empurre a barra para cima até estender os braços, e abaixe-a controladamente de volta à posição inicial.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=2yjwXTZQDDI'
    },
    {
        'name': 'Desenvolvimento com Halteres',
        'description': 'Sentado ou em pé, segure um halter em cada mão na altura dos ombros, com as palmas voltadas para frente. Empurre os halteres para cima até estender os braços, e abaixe-os controladamente de volta à posição inicial.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=qEwKCR5JCog'
    },
    {
        'name': 'Desenvolvimento Arnold',
        'description': 'Sentado, segure os halteres na altura dos ombros com as palmas voltadas para você. Enquanto eleva os halteres, gire as palmas para fora, terminando com os braços estendidos e as palmas voltadas para frente. Inverta o movimento ao descer.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=3ml7BH7mNwQ'
    },
    {
        'name': 'Desenvolvimento com Barra Smith',
        'description': 'Sentado ou em pé, posicione-se na máquina Smith com a barra na altura dos ombros. Desengate a barra e empurre-a para cima até estender os braços, e abaixe-a controladamente.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=hAb-AYdulfo'
    },
    {
        'name': 'Desenvolvimento na Máquina',
        'description': 'Sente-se na máquina de desenvolvimento, ajuste o banco e segure as alças. Empurre para cima até estender os braços, contraindo os ombros no topo, e retorne controladamente à posição inicial.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=Wqq43dKW1TU'
    },
    {
        'name': 'Elevação Lateral com Halteres',
        'description': 'Em pé, segure um halter em cada mão ao lado do corpo. Mantendo os cotovelos levemente flexionados, eleve os braços lateralmente até a altura dos ombros, e abaixe controladamente de volta à posição inicial.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=3VcKaXpzqRo'
    },
    {
        'name': 'Elevação Lateral na Polia',
        'description': 'Em pé, ao lado de uma polia baixa, segure a alça com a mão oposta ao aparelho. Mantenha o cotovelo levemente flexionado e eleve o braço lateralmente até a altura do ombro, e retorne controladamente.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=FxnxfIoEZOA'
    },
    {
        'name': 'Elevação Lateral na Máquina',
        'description': 'Sente-se na máquina de elevação lateral, posicionando os braços nas almofadas. Eleve os braços lateralmente, contraindo os ombros, e retorne controladamente à posição inicial.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=U-BC9CibQZM'
    },
    {
        'name': 'Elevação Frontal com Halteres',
        'description': 'Em pé, segure um halter em cada mão à frente do corpo. Mantendo os cotovelos levemente flexionados, eleve os braços à frente até a altura dos ombros, e abaixe controladamente de volta à posição inicial.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=sOcYlBI85hc'
    },
    {
        'name': 'Elevação Frontal com Barra',
        'description': 'Em pé, segure uma barra com as duas mãos à frente do corpo. Mantendo os cotovelos levemente flexionados, eleve a barra à frente até a altura dos ombros, e abaixe controladamente de volta à posição inicial.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=ALa-u1JYuLw'
    },
    {
        'name': 'Elevação Frontal com Polia',
        'description': 'Em pé, de costas para uma polia baixa, segure a alça com as duas mãos à frente do corpo. Eleve a alça à frente até a altura dos ombros, e abaixe controladamente.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=UihlAF2PwF8'
    },
    {
        'name': 'Crucifixo Invertido com Halteres',
        'description': 'Incline o tronco para frente, mantenha as costas retas e os joelhos levemente flexionados. Segure os halteres com os cotovelos levemente dobrados e eleve-os lateralmente até a altura dos ombros, contraindo as costas.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=wZnsZsMywrY'
    },
    {
        'name': 'Crucifixo Invertido no Cabo',
        'description': 'Em pé, de frente para polias altas cruzadas, segure a alça da direita com a mão esquerda e vice-versa. Puxe os cabos para fora e para baixo em um movimento diagonal, contraindo os ombros posteriores, e retorne controladamente.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=JZLHIBRW0Jk'
    },
    {
        'name': 'Crucifixo Invertido na Máquina',
        'description': 'Sente-se na máquina de peck deck ao contrário, posicionando os antebraços nas almofadas. Puxe as almofadas para trás, contraindo os ombros posteriores, e retorne lentamente à posição inicial.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=lVCEeGy7hIs'
    },
    {
        'name': 'Encolhimento de Ombros com Barra',
        'description': 'Em pé, segure a barra com as mãos na largura dos ombros e os braços estendidos. Eleve os ombros o máximo possível em direção às orelhas, segure brevemente e abaixe controladamente.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=cJRVVxmytaM'
    },
    {
        'name': 'Encolhimento de Ombros com Halteres',
        'description': 'Em pé, segure um halter em cada mão ao lado do corpo, com os braços estendidos. Eleve os ombros o máximo possível em direção às orelhas, segure brevemente e abaixe controladamente.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=g6qbq4Lf1FI'
    },
    {
        'name': 'Encolhimento de Ombros na Máquina Smith',
        'description': 'Em pé dentro da máquina Smith, posicione a barra atrás de você e segure-a com as mãos. Eleve os ombros o máximo possível em direção às orelhas, segure brevemente e abaixe controladamente.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=7HMzEMZM8XU'
    },
    {
        'name': 'Remada Alta com Barra',
        'description': 'Em pé, segure a barra com as mãos próximas, um pouco menos que a largura dos ombros. Puxe a barra verticalmente, mantendo-a próxima ao corpo, até que chegue à altura dos ombros, com os cotovelos apontando para cima.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=MVMNk0HiTMg'
    },
    {
        'name': 'Remada Alta com Halteres',
        'description': 'Em pé, segure um halter em cada mão à frente do corpo. Puxe os halteres verticalmente até a altura dos ombros, mantendo-os próximos ao corpo, com os cotovelos apontando para cima.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=GUKBBGnuqV8'
    },
    {
        'name': 'Remada Alta no Cabo',
        'description': 'Em pé, de frente para uma polia baixa, segure a alça com as duas mãos. Puxe a alça verticalmente até a altura dos ombros, mantendo-a próxima ao corpo, com os cotovelos apontando para cima.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=NFzTWp2qpiE'
    },
    {
        'name': 'Desenvolvimento com Kettlebell',
        'description': 'Em pé, segure um kettlebell na posição de rack (junto ao ombro). Empurre o kettlebell para cima até estender o braço, e abaixe-o controladamente de volta à posição inicial. Alterne os braços ou use um em cada mão.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=fe9Uw4P56GI'
    },
    {
        'name': 'Face Pull',
        'description': 'Em pé, de frente para a polia alta, segure a corda com as mãos. Puxe a corda em direção ao rosto, afastando os cotovelos para os lados, e retorne controladamente. Foque em contrair os ombros posteriores.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=V8dZ3pyiCBo'
    },
    {
        'name': 'Elevação Lateral Inclinada',
        'description': 'Incline-se lateralmente segurando um halter na mão do lado oposto à inclinação. Eleve o halter lateralmente até a altura do ombro, contraindo a região lateral do ombro, e retorne controladamente.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=v_ZkxWzYnMc'
    },
    {
        'name': 'W Press (Desenvolvimento com Cotovelos para Frente)',
        'description': 'Em pé, segure dois halteres na altura dos ombros com os cotovelos apontando para frente, criando uma forma de "W". Empurre os halteres para cima até estender os braços, e retorne à posição inicial.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=ZrXE9Cy0IsI'
    },
    {
        'name': 'Elevação de Ombros 6 Direções',
        'description': 'Em pé, segure um par de halteres leves. Realize elevações laterais em 6 posições diferentes: frontal, 45 graus, lateral, 135 graus, posterior e elevando diretamente para cima. Cada posição é uma repetição.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=hXkP4DCvD0A'
    },
    {
        'name': 'Desenvolvimento com Halteres Sentado na Bola',
        'description': 'Sente-se em uma bola de estabilidade, segure um halter em cada mão na altura dos ombros. Empurre os halteres para cima até estender os braços, e abaixe-os controladamente. A instabilidade da bola intensifica o trabalho muscular.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=G0rL1uv6-hI'
    }
]

# Função para adicionar os exercícios ao banco de dados
def adicionar_exercicios_ombros():
    with app.app_context():
        # Adicionar cada exercício ao banco de dados
        for exercicio in exercicios_ombros:
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
        print(f"Foram adicionados {len(exercicios_ombros)} exercícios de ombros ao banco de dados!")