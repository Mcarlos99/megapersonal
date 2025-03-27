from app import app, db, Exercise

# Exercícios de ABDÔMEN (25 exercícios)
exercicios_abdomen = [
    {
        'name': 'Abdominal Tradicional',
        'description': 'Deite-se de costas no chão, com os joelhos flexionados e os pés apoiados no chão. Coloque as mãos atrás da cabeça ou cruzadas sobre o peito. Contraia o abdômen, elevando os ombros do chão, e retorne à posição inicial controladamente.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=Xyd_fa5zoEU'
    },
    {
        'name': 'Abdominal Infra (Elevação de Pernas)',
        'description': 'Deite-se de costas no chão, com as mãos ao lado do corpo ou sob os glúteos. Mantenha as pernas estendidas ou levemente flexionadas e eleve-as em direção ao teto, contraindo o abdômen inferior. Abaixe as pernas controladamente, sem tocar o chão.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=JB2oyawG9KI'
    },
    {
        'name': 'Abdominal Oblíquo (Bicicleta)',
        'description': 'Deite-se de costas no chão, com as mãos atrás da cabeça e as pernas elevadas com os joelhos flexionados. Alterne levando o cotovelo direito em direção ao joelho esquerdo e vice-versa, simulando o movimento de pedalar uma bicicleta.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=Iwyvozckjak'
    },
    {
        'name': 'Prancha',
        'description': 'Posicione-se com os antebraços apoiados no chão, cotovelos alinhados abaixo dos ombros, e as pontas dos pés apoiadas no chão. Mantenha o corpo em linha reta da cabeça aos calcanhares, contraindo o abdômen e os glúteos. Segure esta posição pelo tempo desejado.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=ASdvN_XEl_c'
    },
    {
        'name': 'Prancha Lateral',
        'description': 'Posicione-se de lado, com o antebraço apoiado no chão, cotovelo alinhado abaixo do ombro, e os pés um sobre o outro. Eleve o quadril, formando uma linha reta do tornozelo à cabeça. Segure esta posição pelo tempo desejado e repita do outro lado.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=xOhBnFMpOeU'
    },
    {
        'name': 'Abdominal na Máquina',
        'description': 'Sente-se na máquina de abdominal, ajustando o encosto e as almofadas. Segure as alças, contraia o abdômen e flexione o tronco à frente. Retorne controladamente à posição inicial.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=JRj5m9hsoY0'
    },
    {
        'name': 'Abdominal Declinado',
        'description': 'Deite-se em um banco declinado, prenda os pés nos suportes, e coloque as mãos atrás da cabeça ou cruzadas sobre o peito. Contraia o abdômen, elevando o tronco em direção às coxas, e retorne à posição inicial controladamente.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=_M2Etme-tfE'
    },
    {
        'name': 'Russian Twist',
        'description': 'Sente-se no chão com os joelhos flexionados e os pés ligeiramente elevados. Incline o tronco para trás, mantendo as costas retas. Segure um peso com as mãos e gire o tronco de um lado para o outro, tocando o peso no chão a cada lado.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=wkD8rjkodUI'
    },
    {
        'name': 'Mountain Climbers',
        'description': 'Posicione-se em quatro apoios, com as mãos alinhadas abaixo dos ombros e o corpo em linha reta. Alterne trazendo os joelhos em direção ao peito, como se estivesse escalando, mantendo o core contraído durante todo o movimento.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=nmwgirgXLYM'
    },
    {
        'name': 'Abdominal Infra na Barra',
        'description': 'Pendure-se em uma barra fixa, com os braços estendidos e as mãos na largura dos ombros. Contraia o abdômen, elevando os joelhos em direção ao peito, e abaixe controladamente.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=JB2oyawG9KI'
    },
    {
        'name': 'Abdominal Inverso',
        'description': 'Deite-se de costas no chão, com as mãos ao lado do corpo e as pernas elevadas com os joelhos flexionados a 90 graus. Contraia o abdômen, elevando o quadril do chão e empurrando as pernas ligeiramente para cima. Retorne controladamente à posição inicial.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=29hQpFCP_zs'
    },
    {
        'name': 'V-Ups',
        'description': 'Deite-se de costas no chão, com os braços estendidos acima da cabeça e as pernas estendidas. Simultaneamente, eleve o tronco e as pernas, tentando tocar as mãos nos pés, formando um "V" com o corpo. Retorne controladamente à posição inicial.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=iP2fjvG0g3w'
    },
    {
        'name': 'Prancha com Apoios',
        'description': 'Posicione-se em quatro apoios, com as mãos alinhadas abaixo dos ombros e os joelhos alinhados abaixo dos quadris. Estenda um braço à frente e a perna oposta para trás, mantendo o core contraído e o corpo estável. Alterne os lados.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=QOVaHwm-Q6U'
    },
    {
        'name': 'Prancha com Toque no Ombro',
        'description': 'Posicione-se em posição de prancha alta, com as mãos alinhadas abaixo dos ombros e o corpo em linha reta. Alternadamente, toque o ombro oposto com cada mão, mantendo o quadril estável e o core contraído.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=fbTLg1Hvr8M'
    },
    {
        'name': 'Abdominal Canivete',
        'description': 'Deite-se de costas no chão, com os braços estendidos acima da cabeça e as pernas estendidas. Simultaneamente, eleve o tronco e as pernas, contraindo o abdômen e tentando tocar os pés. Retorne controladamente à posição inicial.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=j2RJ9CqIgfI'
    },
    {
        'name': 'Dragon Flag',
        'description': 'Deite-se de costas em um banco, segurando a parte de trás do banco com as mãos acima da cabeça. Eleve as pernas e o quadril, mantendo o corpo reto, apoiando apenas os ombros no banco. Abaixe o corpo controladamente, mantendo-o reto, sem tocar as costas no banco.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=kICxJien7xM'
    },
    {
        'name': 'Hollow Hold',
        'description': 'Deite-se de costas no chão, pressione a região lombar contra o chão, estenda os braços acima da cabeça e eleve as pernas a aproximadamente 30 graus do chão. Mantenha o corpo nessa posição, contraindo o abdômen. Segure esta posição pelo tempo desejado.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=ztmMjFA1PuY'
    },
    {
        'name': 'Abdominal Rollout com Roda',
        'description': 'Ajoelhe-se no chão, segurando uma roda de abdominal com as duas mãos à frente dos joelhos. Role a roda para frente, estendendo o corpo, mantendo o core contraído, e depois puxe de volta à posição inicial usando a força do abdômen.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=3sy6iLhgl5o'
    },
    {
        'name': 'Abdominal Pêndulo',
        'description': 'Deite-se de costas no chão, com os braços estendidos ao lado do corpo e as pernas elevadas a 90 graus. Mantenha as pernas juntas e abaixe-as para um lado até quase tocar o chão, depois eleve-as de volta e abaixe para o outro lado.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=0CFILIy_YrI'
    },
    {
        'name': 'Abdominal com Torção',
        'description': 'Deite-se de costas no chão, com os joelhos flexionados e os pés apoiados no chão. Coloque as mãos atrás da cabeça. Eleve o tronco e gire-o, levando o cotovelo direito em direção ao joelho esquerdo. Retorne à posição inicial e repita para o outro lado.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=OMJ2OkjB8Tc'
    },
    {
        'name': 'Tesoura',
        'description': 'Deite-se de costas no chão, eleve ligeiramente os ombros do chão e as pernas estendidas a aproximadamente 15 cm do chão. Cruze as pernas, alternando a perna de cima, mantendo o core contraído durante todo o movimento.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=dkQdlndLFGE'
    },
    {
        'name': 'Toe Touches',
        'description': 'Deite-se de costas no chão, eleve as pernas para cima com os joelhos ligeiramente flexionados. Eleve os ombros do chão, estendendo os braços para tocar os dedos dos pés. Retorne controladamente à posição inicial.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=H-7AZusMeKo'
    },
    {
        'name': 'Prancha com Elevação de Perna',
        'description': 'Posicione-se em posição de prancha, com os antebraços apoiados no chão e o corpo em linha reta. Alterne elevando cada perna, mantendo o quadril estável e o core contraído.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=x6ZmRs4C66I'
    },
    {
        'name': 'Windshield Wipers',
        'description': 'Deite-se de costas no chão, estenda os braços para os lados e eleve as pernas estendidas a 90 graus do chão. Gire o quadril, levando as pernas para um lado e depois para o outro, mantendo o core contraído.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=Xyd_fa5zoEU'
    },
    {
        'name': 'Abdominal com Resistência',
        'description': 'Deite-se de costas no chão, com os joelhos flexionados e os pés apoiados no chão. Segure um peso ou disco no peito. Contraia o abdômen, elevando os ombros do chão, e retorne à posição inicial controladamente.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=vyHO60Dw8zU'
    },
    {
        'name': 'Abdominal na Fitball',
        'description': 'Sente-se em uma bola de estabilidade, com os pés apoiados no chão. Cruze os braços sobre o peito ou coloque-os atrás da cabeça. Abaixe o tronco para trás, contraindo o abdômen, e retorne à posição inicial.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=_fcTG8SMxJs'
    },
    {
        'name': 'Prancha com Fitball',
        'description': 'Posicione-se em posição de prancha, com os antebraços apoiados em uma bola de estabilidade e as pontas dos pés apoiadas no chão. Mantenha o corpo em linha reta, contraindo o core para manter a estabilidade.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=iIDN0_RXUOE'
    },
    {
        'name': 'Dead Bug',
        'description': 'Deite-se de costas no chão, eleve os braços em direção ao teto e as pernas com os joelhos flexionados a 90 graus. Mantendo a região lombar pressionada contra o chão, estenda simultaneamente o braço direito e a perna esquerda. Retorne à posição inicial e repita com o lado oposto.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=g_BYB0R-4Ws'
    },
    {
        'name': 'Cable Crunch',
        'description': 'Ajoelhe-se de frente para uma polia alta, segure a corda com as mãos próximas à cabeça. Contraia o abdômen, flexionando o tronco em direção aos joelhos, e retorne controladamente à posição inicial.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=sDtYQZptIAQ'
    },
    {
        'name': 'Medicine Ball Slam',
        'description': 'Em pé, segure uma medicine ball acima da cabeça com os braços estendidos. Contraia o abdômen e use a força do core para lançar a bola ao chão com força. Pegue a bola após o quique e repita o movimento.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=2IWLB6xZkhs'
    },
    {
        'name': 'Side Jackknife',
        'description': 'Deite-se de lado, com o corpo estendido e a mão da cabeça apoiando-a. Simultaneamente, eleve as pernas e o tronco, contraindo os oblíquos e tentando aproximar o cotovelo da ilíaca. Retorne controladamente à posição inicial.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=Xyd_fa5zoEU'
    },
    {
        'name': 'L-Sit',
        'description': 'Sente-se no chão, coloque as mãos ao lado do quadril e empurre o corpo para cima, elevando o quadril do chão. Mantenha as pernas estendidas à frente, paralelas ao chão, formando um "L" com o corpo. Segure esta posição pelo tempo desejado.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=shL_6XNQz-k'
    },
    {
        'name': 'Prancha com Kickthrough',
        'description': 'Posicione-se em quatro apoios, com as mãos alinhadas abaixo dos ombros e os joelhos alinhados abaixo dos quadris. Eleve os joelhos ligeiramente do chão, depois gire o corpo, estendendo uma perna por baixo do corpo e elevando o braço oposto. Retorne à posição inicial e repita do outro lado.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=3vHqXTG9RMw'
    },
    {
        'name': 'Abdominal Suspenso',
        'description': 'Pendure-se em uma barra ou suporte para abdominais, com os braços flexionados e o corpo suspenso. Contraia o abdômen, elevando os joelhos em direção ao peito, e abaixe controladamente.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=BGOfGQ0A50c'
    },
    {
        'name': 'Abdominal Grupado',
        'description': 'Deite-se de costas no chão, com os braços estendidos ao lado do corpo e as pernas estendidas. Simultaneamente, flexione os joelhos e eleve o tronco, contraindo o abdômen e tentando tocar as mãos nos tornozelos. Retorne controladamente à posição inicial.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=gWGnJVn3Dco'
    }
]

# Função para adicionar os exercícios ao banco de dados
def adicionar_exercicios_abdomen():
    with app.app_context():
        # Adicionar cada exercício ao banco de dados
        for exercicio in exercicios_abdomen:
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
        print(f"Foram adicionados {len(exercicios_abdomen)} exercícios adicionais de abdômen ao banco de dados!")