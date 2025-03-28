from app import app, db, Exercise

# Exercícios de PANTURRILHA (25 exercícios)
exercicios_panturrilha = [
    {
        'name': 'Elevação de Panturrilha em Pé',
        'description': 'Em pé, com as pontas dos pés sobre um degrau ou plataforma e os calcanhares no ar, eleve-se na ponta dos pés, contraindo as panturrilhas. Abaixe os calcanhares abaixo do nível da plataforma e repita.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=wxwY7GXxL4k'
    },
    {
        'name': 'Elevação de Panturrilha Sentado',
        'description': 'Sentado na máquina de panturrilha, posicione as pontas dos pés na plataforma e os joelhos sob as almofadas. Eleve os calcanhares, contraindo as panturrilhas, e depois abaixe-os controladamente.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=JbyjNymZOt0'
    },
    {
        'name': 'Elevação de Panturrilha no Leg Press',
        'description': 'Sentado na máquina leg press, posicione as pontas dos pés na parte inferior da plataforma. Empurre a plataforma estendendo os tornozelos, e depois flexione-os controladamente.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=UC1oiV7PzXU'
    },
    {
        'name': 'Elevação de Panturrilha com Barra',
        'description': 'Em pé, com uma barra apoiada nos trapézios, eleve-se na ponta dos pés, contraindo as panturrilhas. Abaixe os calcanhares até o chão e repita.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=JbyjNymZOt0'
    },
    {
        'name': 'Elevação de Panturrilha Unilateral',
        'description': 'Em pé, apoiado em uma perna com a ponta do pé sobre um degrau, segure-se em algo para manter o equilíbrio. Eleve-se na ponta do pé, contraindo a panturrilha, e depois abaixe o calcanhar controladamente.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=JH5QvfgMNwQ'
    },
    {
        'name': 'Elevação de Panturrilha com Halteres',
        'description': 'Em pé, segurando halteres ao lado do corpo, com as pontas dos pés sobre um degrau, eleve-se na ponta dos pés. Abaixe os calcanhares abaixo do nível do degrau e repita.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=wxwY7GXxL4k'
    },
    {
        'name': 'Elevação de Panturrilha Sentado com Halteres',
        'description': 'Sentado em um banco, coloque as pontas dos pés no chão e posicione halteres sobre os joelhos. Eleve os calcanhares, contraindo as panturrilhas, e depois abaixe-os controladamente.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=JbyjNymZOt0'
    },
    {
        'name': 'Elevação de Panturrilha Burro',
        'description': 'Utilizando uma máquina específica ou improvisando com um parceiro sentado nas costas, posicione as pontas dos pés em um degrau, com os joelhos levemente flexionados. Eleve-se na ponta dos pés e abaixe controladamente.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=gCXQHvbcb4I'
    },
    {
        'name': 'Elevação de Panturrilha com Smith Machine',
        'description': 'Posicione os ombros sob a barra da máquina Smith, com as pontas dos pés sobre um degrau. Destrave a barra e eleve-se na ponta dos pés, contraindo as panturrilhas. Abaixe os calcanhares e repita.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=DXVGO5hNF8Y'
    },
    {
        'name': 'Pular Corda',
        'description': 'Com uma corda de pular, salte repetidamente, usando principalmente as panturrilhas para impulsionar o corpo. Mantenha um ritmo constante, pulando sobre a ponta dos pés.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=FJmRQ5iTXKE'
    },
    {
        'name': 'Skipping',
        'description': 'Corra no lugar, elevando os joelhos e saltando sobre a ponta dos pés. Mantenha um ritmo rápido, usando as panturrilhas para impulsionar cada salto.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=CYJ3QA9G9oI'
    },
    {
        'name': 'Box Jumps',
        'description': 'Posicione-se em frente a uma caixa ou plataforma. Salte para cima da caixa, aterrissando suavemente na ponta dos pés. Desça e repita.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=52r_Ul5k03g'
    },
    {
        'name': 'Elevação de Panturrilha Isométrica',
        'description': 'Em pé, com as pontas dos pés sobre um degrau, eleve-se na ponta dos pés e mantenha a posição contraída por 10-30 segundos. Retorne à posição inicial e repita.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=wxwY7GXxL4k'
    },
    {
        'name': 'Tibial Anterior',
        'description': 'Sentado ou em pé, eleve a ponta do pé, mantendo o calcanhar no chão. Este exercício trabalha o músculo oposto às panturrilhas, proporcionando equilíbrio muscular.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=JQXkOSY5NP4'
    },
    {
        'name': 'Caminhada na Ponta dos Pés',
        'description': 'Caminhe na ponta dos pés por uma distância determinada ou por um tempo específico. Mantenha os calcanhares elevados durante todo o movimento.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=QYFy8ul5uFU'
    },
    {
        'name': 'Step-Up na Ponta dos Pés',
        'description': 'Suba em um degrau com um pé, terminando o movimento na ponta do pé. Desça e repita com o outro pé.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=dQqApCGd5Ss'
    },
    {
        'name': 'Elevação de Panturrilha Sentado com Barra',
        'description': 'Sentado em um banco, coloque uma barra sobre os joelhos com as pontas dos pés no chão. Eleve os calcanhares, contraindo as panturrilhas, e depois abaixe-os controladamente.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=JbyjNymZOt0'
    },
    {
        'name': 'Elevação Combinada (Agachamento + Panturrilha)',
        'description': 'Realize um agachamento completo e, ao subir, continue o movimento elevando-se na ponta dos pés para trabalhar as panturrilhas. Retorne à posição inicial e repita.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=1l-ZhRMCQHQ'
    },
    {
        'name': 'Tibial com Resistência',
        'description': 'Sentado, prenda uma faixa elástica ou cabo ao pé. Flexione o tornozelo, puxando a ponta do pé em direção à canela contra a resistência. Retorne controladamente.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=JQXkOSY5NP4'
    },
    {
        'name': 'Elevação de Panturrilha em Plataforma Inclinada',
        'description': 'Posicione as pontas dos pés em uma plataforma inclinada, com os calcanhares no ar. Eleve-se na ponta dos pés e abaixe controladamente.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=wxwY7GXxL4k'
    },
    {
        'name': 'Elevação de Panturrilha em Bola Suíça',
        'description': 'Em pé, coloque as pontas dos pés sobre uma bola suíça, mantendo o equilíbrio. Eleve-se na ponta dos pés e abaixe controladamente.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=wxwY7GXxL4k'
    },
    {
        'name': 'Elevação de Panturrilha com Rotação',
        'description': 'Em pé, com as pontas dos pés sobre um degrau, eleve-se na ponta dos pés, girando os calcanhares para fora (pés para dentro). Retorne à posição inicial e repita, alternando com rotação para dentro.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=PxkS0DJ_5Dk'
    },
    {
        'name': 'Elevação de Panturrilha em Prensa 45°',
        'description': 'Sentado na prensa 45°, posicione as pontas dos pés na plataforma. Mantenha as pernas estendidas e pressione a plataforma apenas com os pés, trabalhando somente as panturrilhas.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=UC1oiV7PzXU'
    },
    {
        'name': 'Saltos de Afundo',
        'description': 'Partindo da posição de afundo, salte verticalmente trocando as pernas no ar e aterrisse na ponta dos pés. Continue alternando as pernas em cada salto.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=VrKN08AR1C4'
    },
    {
        'name': 'Elevação de Panturrilha com Base Instável',
        'description': 'Em pé sobre uma superfície instável como um bosu ou almofada de equilíbrio, eleve-se na ponta dos pés e abaixe controladamente.',
        'muscle_group': 'Panturrilha',
        'video_url': 'https://www.youtube.com/watch?v=wxwY7GXxL4k'
    }
]

# Função para adicionar os exercícios ao banco de dados
def adicionar_exercicios_panturrilha():
    with app.app_context():
        # Adicionar cada exercício ao banco de dados
        for exercicio in exercicios_panturrilha:
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
        print(f"Foram adicionados {len(exercicios_panturrilha)} exercícios de panturrilha ao banco de dados!")