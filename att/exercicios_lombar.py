from app import app, db, Exercise

# Exercícios de LOMBAR (25 exercícios)
exercicios_lombar = [
    {
        'name': 'Extensão Lombar',
        'description': 'Deite-se de bruços na máquina de extensão lombar, com o quadril apoiado na almofada e os pés presos. Abaixe o tronco e depois estenda-o até ficar alinhado com as pernas, contraindo os músculos lombares. Retorne controladamente.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=ph3pddpKzzw'
    },
    {
        'name': 'Levantamento Terra',
        'description': 'Em pé, posicione-se com os pés na largura dos ombros e a barra próxima aos tornozelos. Flexione os joelhos e quadris, mantendo as costas retas, segure a barra e estenda o corpo levantando a barra, mantendo-a próxima às pernas.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=op9kVnSso6Q'
    },
    {
        'name': 'Boa Dia (Good Morning)',
        'description': 'Em pé, coloque uma barra nas costas, apoiada nos trapézios. Mantendo as pernas quase estendidas e as costas retas, incline o tronco à frente, abaixando a barra até a altura das canelas, e retorne à posição inicial.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=Xh-gmFLNdvI'
    },
    {
        'name': 'Superman',
        'description': 'Deite-se de bruços, com os braços estendidos à frente e as pernas estendidas. Eleve simultaneamente os braços, o peito e as pernas, contraindo os músculos lombares. Mantenha a posição por alguns segundos e retorne controladamente.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=cc6UVRS7PW4'
    },
    {
        'name': 'Hiperextensão em Banco Romano',
        'description': 'Posicione-se no banco romano, com o quadril apoiado na almofada e os pés presos. Comece com o tronco flexionado para baixo, e estenda-o até que o corpo esteja em linha reta, contraindo as costas. Retorne controladamente.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=ph3pddpKzzw'
    },
    {
        'name': 'Levantamento Terra Sumo',
        'description': 'Em pé, posicione-se com os pés bem afastados e rotacionados para fora, com a barra entre eles. Flexione os joelhos e quadris, segure a barra e estenda o corpo levantando a barra, mantendo-a próxima às pernas.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=XsrD5y8EIKU'
    },
    {
        'name': 'Remada Curvada com Barra',
        'description': 'Em pé, segure a barra com as mãos na largura dos ombros, dobre os joelhos levemente e incline o tronco à frente mantendo as costas retas. Puxe a barra em direção ao abdômen, contraindo as costas, e desça controladamente.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=kBWAon7ItDw'
    },
    {
        'name': 'Levantamento Terra com Pernas Estendidas',
        'description': 'Em pé, segure a barra com as mãos na largura dos ombros. Mantendo as pernas quase estendidas e as costas retas, incline o tronco à frente, abaixando a barra até a altura das canelas, e retorne à posição inicial.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=1ZXobu7JvvE'
    },
    {
        'name': 'Ponte de Quadril',
        'description': 'Deite-se de costas no chão, com os joelhos flexionados e os pés apoiados no chão. Eleve o quadril, contraindo os glúteos e os músculos lombares, até que o corpo forme uma linha reta do joelho ao ombro. Retorne controladamente.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=wPM8icPu6H8'
    },
    {
        'name': 'Bird Dog',
        'description': 'Posicione-se de quatro apoios, com mãos alinhadas sob os ombros e joelhos sob os quadris. Estenda simultaneamente o braço direito para frente e a perna esquerda para trás, mantendo o equilíbrio. Retorne à posição inicial e alterne.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=wS8QvxP2PwU'
    },
    {
        'name': 'Prancha',
        'description': 'Apoie-se nos antebraços e nas pontas dos pés, mantendo o corpo em linha reta da cabeça aos calcanhares. Contraia o abdômen e os glúteos para manter a posição. Segure pelo tempo desejado.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=ASdvN_XEl_c'
    },
    {
        'name': 'Remada em T com Halteres',
        'description': 'Segure um halter em cada mão, incline o tronco para frente a partir do quadril, mantendo as costas retas. Os braços devem estar estendidos em direção ao chão. Eleve os halteres para os lados, formando um "T" com o corpo. Retorne controladamente.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=ZG7RcJx_q6o'
    },
    {
        'name': 'Nadador',
        'description': 'Deite-se de bruços, com os braços estendidos à frente e as pernas estendidas. Eleve alternadamente o braço direito/perna esquerda e depois o braço esquerdo/perna direita, simulando o movimento de natação. Continue alternando.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=Dbxw9lvIKqE'
    },
    {
        'name': 'Extensão Lombar com Braços em Y',
        'description': 'Deite-se de bruços, com os braços estendidos acima da cabeça em forma de "Y". Eleve simultaneamente os braços, o peito e as pernas, contraindo os músculos lombares. Mantenha a posição por alguns segundos e retorne controladamente.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=cc6UVRS7PW4'
    },
    {
        'name': 'Levantamento Terra com Trap Bar',
        'description': 'Posicione-se dentro da trap bar (barra hexagonal), com os pés na largura dos ombros. Flexione os joelhos e quadris, mantendo as costas retas, segure as alças e estenda o corpo levantando a barra.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=1jBc5jM3VrI'
    },
    {
        'name': 'Cat-Cow',
        'description': 'Posicione-se de quatro apoios. Inspire enquanto arqueia as costas para baixo (cow), levantando a cabeça e o cóccix. Expire enquanto arredonda as costas para cima (cat), abaixando a cabeça e o cóccix. Alterne os movimentos de forma fluida.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=kqnua4rHVVA'
    },
    {
        'name': 'Elevação de Arco',
        'description': 'Deite-se de bruços, com os braços estendidos à frente. Eleve o peito e as pernas simultaneamente, formando um arco com o corpo. Mantenha a posição por alguns segundos e retorne controladamente.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=cc6UVRS7PW4'
    },
    {
        'name': 'Agachamento',
        'description': 'Em pé, com os pés na largura dos ombros, flexione os joelhos e quadris, abaixando o corpo como se fosse sentar em uma cadeira. Mantenha o peito erguido e as costas retas. Retorne à posição inicial empurrando através dos calcanhares.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=SW_C1A-rejs'
    },
    {
        'name': 'Pull-Through com Corda',
        'description': 'Posicione-se de costas para a polia baixa, afastado, segurando uma corda entre as pernas. Mantendo as costas retas, flexione o quadril, inclinando o tronco para frente. Estenda o quadril até ficar ereto, contraindo os glúteos e lombares.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=lht3YD3JQ2s'
    },
    {
        'name': 'Back Extension Isométrica',
        'description': 'Posicione-se no banco romano, com o quadril apoiado na almofada e os pés presos. Estenda o tronco até que o corpo esteja em linha reta e mantenha a posição isometricamente por 30-60 segundos.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=ph3pddpKzzw'
    },
    {
        'name': 'Side Plank',
        'description': 'Deite-se de lado, apoiando-se sobre o antebraço, com o cotovelo alinhado abaixo do ombro. Eleve o quadril, formando uma linha reta com o corpo. Mantenha a posição por 30-60 segundos e repita do outro lado.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=xOhBnFMpOeU'
    },
    {
        'name': 'Jefferson Curl',
        'description': 'Em pé sobre uma plataforma elevada, segure um peso à frente do corpo. Flexione a cabeça, seguida do tronco, vértebra por vértebra, até onde for confortável. Retorne à posição inicial, desdobrando o corpo vértebra por vértebra.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=nYS0R4c3Ojw'
    },
    {
        'name': 'Remada Unilateral com Rotação',
        'description': 'Em posição de prancha lateral, apoiado sobre um braço estendido, segure um halter na mão livre. Puxe o halter em direção ao peito e, ao chegar ao topo, rotacione o tronco, estendendo o braço para cima. Retorne controladamente.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=QtDVX8ebB8s'
    },
    {
        'name': 'Ponte em Fitball',
        'description': 'Deite-se de costas no chão, com as pernas estendidas e os calcanhares apoiados em uma bola de estabilidade. Eleve o quadril, contraindo os glúteos e os músculos lombares, até que o corpo forme uma linha reta. Retorne controladamente.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=HfpRhNxLqJA'
    },
    {
        'name': 'Romanian Deadlift Unilateral',
        'description': 'Em pé, apoiado em uma perna, segure um peso na mão do mesmo lado. Incline o tronco para frente, estendendo a outra perna para trás, mantendo-a alinhada com o tronco. Retorne à posição inicial e repita com o outro lado.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=1V53Z3V_7_A'
    }
]

# Função para adicionar os exercícios ao banco de dados
def adicionar_exercicios_lombar():
    with app.app_context():
        # Adicionar cada exercício ao banco de dados
        for exercicio in exercicios_lombar:
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
        print(f"Foram adicionados {len(exercicios_lombar)} exercícios de lombar ao banco de dados!")