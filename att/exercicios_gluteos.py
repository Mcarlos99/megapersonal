from app import app, db, Exercise

# Exercícios de GLÚTEOS (25 exercícios)
exercicios_gluteos = [
    {
        'name': 'Agachamento Livre',
        'description': 'Em pé, com os pés na largura dos ombros, coloque a barra nas costas. Flexione os joelhos e quadris, abaixando o corpo como se fosse sentar em uma cadeira, mantendo as costas retas e o peito erguido. Retorne à posição inicial empurrando através dos calcanhares.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=SW_C1A-rejs'
    },
    {
        'name': 'Hip Thrust',
        'description': 'Sente-se no chão com as escápulas apoiadas em um banco, joelhos flexionados e pés apoiados no chão. Coloque uma barra sobre o quadril. Eleve o quadril, estendendo-o até que o corpo forme uma linha reta do joelho ao ombro, contraindo os glúteos no topo.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=Zp26q4BY5HE'
    },
    {
        'name': 'Elevação Pélvica',
        'description': 'Deite-se de costas no chão, com os joelhos flexionados e os pés apoiados no chão. Eleve o quadril, contraindo os glúteos, até que o corpo forme uma linha reta do joelho ao ombro. Retorne controladamente à posição inicial.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=wPM8icPu6H8'
    },
    {
        'name': 'Agachamento Sumô',
        'description': 'Em pé, com os pés bem afastados e voltados para fora, segure um halter ou kettlebell entre as pernas. Flexione os joelhos e quadris, abaixando o corpo, mantendo as costas retas e o peito erguido. Retorne à posição inicial empurrando através dos calcanhares.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=qQZEcJpRWUA'
    },
    {
        'name': 'Avanço (Lunges)',
        'description': 'Em pé, dê um passo à frente com uma perna. Flexione ambos os joelhos até que a coxa da frente fique paralela ao chão e o joelho de trás quase toque o chão. Empurre o pé da frente para retornar à posição inicial. Alterne as pernas.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=QOVaHwm-Q6U'
    },
    {
        'name': 'Agachamento Búlgaro',
        'description': 'Em pé, posicione uma perna para trás sobre um banco, com o peito do pé apoiado. A perna da frente deve estar à frente do corpo. Flexione o joelho da frente, abaixando o corpo até que a coxa fique paralela ao chão. Retorne à posição inicial.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=hPlKPjohFS0'
    },
    {
        'name': 'Extensão de Quadril na Polia',
        'description': 'Em pé, de frente para uma polia baixa, prenda a correia no tornozelo. Mantendo a perna de apoio levemente flexionada e o tronco ligeiramente inclinado para frente, estenda a perna com a correia para trás, contraindo o glúteo. Retorne controladamente.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=cUi3CgBTbkY'
    },
    {
        'name': 'Abdução de Quadril de Lado',
        'description': 'Deite-se de lado no chão, com as pernas estendidas. Eleve a perna de cima, mantendo-a alinhada com o corpo, e abaixe-a controladamente. Repita o movimento e então troque de lado.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=jgh6sGwtTwk'
    },
    {
        'name': 'Elevação de Quadril Unilateral',
        'description': 'Deite-se de costas no chão, com um pé apoiado e a outra perna estendida. Eleve o quadril, contraindo os glúteos, mantendo a perna estendida alinhada com o corpo. Retorne controladamente à posição inicial.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=mQf7UgIPT-s'
    },
    {
        'name': 'Step Up',
        'description': 'Em pé, de frente para um banco ou plataforma, coloque um pé sobre ele. Empurre através do calcanhar para elevar o corpo, trazendo a outra perna até a posição em pé sobre o banco. Retorne controladamente à posição inicial.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=dQqApCGd5Ss'
    },
    {
        'name': 'Passada Lateral',
        'description': 'Em pé, dê um passo lateral amplo com uma perna. Flexione a perna que deu o passo, mantendo a outra estendida, abaixando o quadril. Empurre através do calcanhar para retornar à posição inicial. Repita com a outra perna.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=fPuUa9NcfBU'
    },
    {
        'name': 'Good Morning',
        'description': 'Em pé, com a barra apoiada nas costas, pés na largura dos ombros. Mantendo as costas retas e joelhos levemente flexionados, incline o tronco para frente a partir do quadril. Retorne à posição inicial contraindo os glúteos.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=Xh-gmFLNdvI'
    },
    {
        'name': 'Agachamento com Banda Elástica',
        'description': 'Coloque uma banda elástica acima dos joelhos. Em pé, pés na largura dos ombros, realize um agachamento, mantendo pressão externa contra a banda. Retorne à posição inicial contraindo os glúteos.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=NW3QshKYblw'
    },
    {
        'name': 'Fire Hydrant',
        'description': 'Posicione-se de quatro, com mãos alinhadas abaixo dos ombros e joelhos abaixo dos quadris. Mantendo o joelho flexionado a 90 graus, eleve uma perna lateralmente, como um cachorro em um hidrante. Retorne à posição inicial.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=V1jYIZ_v2yU'
    },
    {
        'name': 'Donkey Kicks',
        'description': 'Posicione-se de quatro, com mãos alinhadas abaixo dos ombros e joelhos abaixo dos quadris. Mantendo o joelho flexionado, eleve uma perna para trás e para cima, contraindo o glúteo. Retorne à posição inicial.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=SJ1Xuz9D-ZQ'
    },
    {
        'name': 'Glute Bridge com Banda Elástica',
        'description': 'Coloque uma banda elástica acima dos joelhos. Deite-se de costas no chão, com os joelhos flexionados e os pés apoiados. Eleve o quadril, contraindo os glúteos e empurrando os joelhos contra a banda. Retorne controladamente.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=Fk3Q4X1wbJs'
    },
    {
        'name': 'Clam Shell',
        'description': 'Deite-se de lado, com joelhos flexionados e pés alinhados com o quadril. Mantendo os pés unidos, abra o joelho de cima, rodando externamente o quadril. Retorne à posição inicial.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=7j9BjK48c0E'
    },
    {
        'name': 'Romanian Deadlift',
        'description': 'Em pé, segure uma barra ou halteres à frente do corpo, pés na largura dos ombros. Mantendo as costas retas e joelhos levemente flexionados, incline o tronco para frente, empurrando o quadril para trás. Retorne à posição inicial.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=JCXUYuzwNrM'
    },
    {
        'name': 'Curtsy Lunge',
        'description': 'Em pé, dê um passo para trás e diagonalmente, cruzando atrás da perna de apoio, como em uma reverência. Flexione ambos os joelhos, abaixando o corpo. Retorne à posição inicial e alterne as pernas.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=Q2SGeKjCHMk'
    },
    {
        'name': 'Agachamento Pliê',
        'description': 'Em pé, pés bem afastados e rotacionados para fora, segure um peso à frente do corpo. Flexione os joelhos, abaixando o corpo verticalmente. Retorne à posição inicial empurrando através dos calcanhares.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=mFTtl3CU3O8'
    },
    {
        'name': 'Single-Leg Romanian Deadlift',
        'description': 'Em pé, apoiado em uma perna, segure um peso na mão do mesmo lado. Incline o tronco para frente, estendendo a outra perna para trás, mantendo-a alinhada com o tronco. Retorne à posição inicial.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=1V53Z3V_7_A'
    },
    {
        'name': 'Frog Pumps',
        'description': 'Deite-se de costas, una as solas dos pés, permitindo que os joelhos se afastem. Eleve o quadril, contraindo os glúteos. Retorne controladamente à posição inicial.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=2t42gvr0S-Y'
    },
    {
        'name': 'Cable Pull Through',
        'description': 'De costas para a polia baixa, segure a corda entre as pernas. Incline o tronco para frente, mantendo as costas retas. Estenda os quadris, contraindo os glúteos, até ficar ereto. Retorne controladamente.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=lht3YD3JQ2s'
    },
    {
        'name': 'Banded Lateral Walk',
        'description': 'Coloque uma banda elástica ao redor dos tornozelos ou acima dos joelhos. Em leve agachamento, dê passos laterais, mantendo tensão na banda e os joelhos afastados. Após vários passos, repita na direção oposta.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=kv-tBQZ8RYg'
    },
    {
        'name': 'Reverse Hyperextension',
        'description': 'Deite-se de bruços sobre um banco, com os quadris na borda e as pernas pendentes. Eleve as pernas até ficarem alinhadas com o tronco, contraindo os glúteos. Abaixe controladamente.',
        'muscle_group': 'Glúteos',
        'video_url': 'https://www.youtube.com/watch?v=py6EpF91dc0'
    }
]

# Função para adicionar os exercícios ao banco de dados
def adicionar_exercicios_gluteos():
    with app.app_context():
        # Adicionar cada exercício ao banco de dados
        for exercicio in exercicios_gluteos:
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
        print(f"Foram adicionados {len(exercicios_gluteos)} exercícios de glúteos ao banco de dados!")