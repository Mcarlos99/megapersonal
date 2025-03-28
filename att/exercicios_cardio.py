from app import app, db, Exercise

# Exercícios de CARDIO (25 exercícios)
exercicios_cardio = [
    {
        'name': 'Corrida em Esteira',
        'description': 'Corra na esteira em um ritmo constante ou variando entre alta e baixa intensidade. Ajuste a velocidade e inclinação conforme seu nível de condicionamento físico.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=9L2b2khySLE'
    },
    {
        'name': 'Ciclismo Indoor',
        'description': 'Pedale em uma bicicleta estacionária ou de spinning, ajustando a resistência e velocidade para atingir diferentes níveis de intensidade. Pode-se alternar entre sentar e ficar de pé.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=fAlCvVJtYGE'
    },
    {
        'name': 'Elíptico',
        'description': 'Use o elíptico com movimentos fluidos, empurrando e puxando os braços enquanto pedala. Ajuste a resistência e inclinação para variar a intensidade.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=mfJhAFGQKW4'
    },
    {
        'name': 'Pular Corda',
        'description': 'Segure as extremidades da corda e gire-a, saltando quando ela passar sob seus pés. Mantenha um ritmo constante e salte apenas o necessário para deixar a corda passar.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=FJmRQ5iTXKE'
    },
    {
        'name': 'Remo',
        'description': 'No ergômetro de remo, inicie o movimento empurrando com as pernas, depois incline o tronco para trás e puxe a alça em direção ao abdômen. Retorne à posição inicial na ordem inversa.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=H0r_ZPXJLtg'
    },
    {
        'name': 'Burpees',
        'description': 'Partindo em pé, agache-se, coloque as mãos no chão, estenda as pernas para trás em posição de prancha, faça uma flexão, volte à posição agachada e salte verticalmente. Repita em sequência.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=TU8QYVW0gDU'
    },
    {
        'name': 'Mountain Climbers',
        'description': 'Em posição de prancha alta, alterne trazendo os joelhos em direção ao peito em um movimento rápido, como se estivesse escalando. Mantenha o core estabilizado durante todo o exercício.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=nmwgirgXLYM'
    },
    {
        'name': 'Jumping Jacks',
        'description': 'Em pé, com os braços ao lado do corpo e pés juntos, salte abrindo as pernas e elevando os braços acima da cabeça. Volte à posição inicial com outro salto e repita em ritmo constante.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=c4DAnQ6DtF8'
    },
    {
        'name': 'Box Jumps',
        'description': 'Posicione-se em frente a uma caixa ou plataforma. Flexione levemente os joelhos e salte sobre a caixa, aterrissando com os joelhos levemente flexionados. Desça e repita.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=52r_Ul5k03g'
    },
    {
        'name': 'High Knees',
        'description': 'Corra no lugar, elevando os joelhos até a altura do quadril alternadamente em um ritmo rápido. Mantenha o tronco ereto e balance os braços naturalmente.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=tx5rgpd5p_A'
    },
    {
        'name': 'Skater Jumps',
        'description': 'Salte lateralmente de um pé para outro, como um patinador. Ao aterrissar, cruze a perna livre atrás do corpo e toque o chão com a mão, se possível. Continue alternando os lados.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=xbABGepKT2o'
    },
    {
        'name': 'Saltos Alternados',
        'description': 'Partindo da posição de afundo, salte verticalmente trocando as pernas no ar. Aterrisse suavemente e continue alternando as pernas em cada salto.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=VrKN08AR1C4'
    },
    {
        'name': 'Escada Coordenativa',
        'description': 'Realize diferentes padrões de passos através de uma escada de agilidade colocada no chão. Mantenha um ritmo rápido e consistente, focando na coordenação e velocidade dos pés.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=67XXkpjQcfA'
    },
    {
        'name': 'Polichinelo com Salto',
        'description': 'Realize um jumping jack tradicional, mas adicione um salto extra no meio, quando os pés se juntam. Este movimento adiciona intensidade e trabalha a potência.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=iSSAk4XCsRA'
    },
    {
        'name': 'Shuttle Run (Corrida de Vai e Vem)',
        'description': 'Coloque dois marcadores separados por uma distância específica. Corra de um marcador ao outro, toque no chão, mude de direção e volte. Continue por um número determinado de repetições.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=MdOCt_6dS3E'
    },
    {
        'name': 'Pular Corda Duplo',
        'description': 'Salte mais alto enquanto pula corda, permitindo que a corda passe duas vezes sob seus pés em um único salto. Este movimento avançado aumenta significativamente a intensidade.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=xN-lqgvf1yc'
    },
    {
        'name': 'Battle Ropes',
        'description': 'Segure as extremidades de cordas grossas ancoradas em um ponto fixo. Crie ondas alternadas ou simultâneas movendo os braços rapidamente para cima e para baixo ou para os lados.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=r2-JZPhLm6E'
    },
    {
        'name': 'Speed Skater',
        'description': 'Salte de um pé para o outro lateralmente, como um patinador de velocidade. Ao aterrissar, cruze a perna livre atrás e estenda o braço oposto à frente para equilíbrio.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=xbABGepKT2o'
    },
    {
        'name': 'Escada (StairMaster)',
        'description': 'Use a máquina StairMaster, subindo degraus continuamente. Ajuste a velocidade para controlar a intensidade do exercício. Mantenha a postura ereta, evitando se apoiar muito no corrimão.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=g2YS1d7_Ld8'
    },
    {
        'name': 'Sprints (Tiros)',
        'description': 'Alterne entre períodos curtos de corrida em alta intensidade (sprint) e períodos de recuperação ativa (caminhada ou trote leve). Por exemplo, 30 segundos de sprint seguidos por 60 segundos de recuperação.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=QcDnUdrpP_s'
    },
    {
        'name': 'Natação',
        'description': 'Nade utilizando diferentes estilos como crawl, costas, peito ou borboleta. Alterne entre séries de intensidade mais alta e períodos de recuperação.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=M5KVJb-bJ2k'
    },
    {
        'name': 'Kettlebell Swing',
        'description': 'Com os pés afastados, segure um kettlebell com as duas mãos. Flexione levemente os joelhos, incline o tronco à frente e balance o kettlebell entre as pernas. Impulsione os quadris para frente para balançar o kettlebell até a altura dos ombros.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=mKDIuUbH94Q'
    },
    {
        'name': 'Circuito de Exercícios',
        'description': 'Realize uma série de exercícios diferentes em sequência, com pouco ou nenhum tempo de descanso entre eles. Por exemplo: agachamentos, flexões, abdominais, burpees, jumping jacks, em ciclos de 30-45 segundos cada.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=CBJBxcGkvH4'
    },
    {
        'name': 'Squat Jumps',
        'description': 'Partindo da posição de agachamento, salte explosivamente para cima, estendendo completamente o corpo. Aterrisse suavemente voltando à posição de agachamento e repita em movimento contínuo.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=Azl5tkCzDcc'
    },
    {
        'name': 'HIIT (Treino Intervalado de Alta Intensidade)',
        'description': 'Alterne entre períodos curtos de exercício em máxima intensidade (como sprint, burpees ou mountain climbers) e períodos curtos de recuperação. Por exemplo, 20 segundos de esforço máximo seguidos por 10 segundos de descanso.',
        'muscle_group': 'Cardio',
        'video_url': 'https://www.youtube.com/watch?v=ml6cT4AZdqI'
    }
]

# Função para adicionar os exercícios ao banco de dados
def adicionar_exercicios_cardio():
    with app.app_context():
        # Adicionar cada exercício ao banco de dados
        for exercicio in exercicios_cardio:
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
        print(f"Foram adicionados {len(exercicios_cardio)} exercícios de cardio ao banco de dados!")