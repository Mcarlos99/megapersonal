from app import app, db, Exercise

# Exercícios de PERNAS (25 exercícios)
exercicios_pernas = [
    {
        'name': 'Agachamento Livre',
        'description': 'Em pé, com os pés na largura dos ombros, coloque a barra nas costas, apoiada nos trapézios. Flexione os joelhos e quadris, abaixando o corpo como se fosse sentar em uma cadeira, mantendo as costas retas e o peito erguido, até que as coxas fiquem paralelas ao chão. Retorne à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=SW_C1A-rejs'
    },
    {
        'name': 'Leg Press',
        'description': 'Sente-se na máquina Leg Press, posicione os pés na plataforma na largura dos ombros. Destrave a plataforma, flexione os joelhos, trazendo-os em direção ao peito, e depois estenda as pernas sem travar os joelhos no topo.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=txBS_pn8xIo'
    },
    {
        'name': 'Cadeira Extensora',
        'description': 'Sente-se na máquina, ajuste o encosto para que os joelhos fiquem alinhados com o eixo de rotação. Posicione os tornozelos atrás da almofada e estenda os joelhos completamente, contraindo o quadríceps no topo. Retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=YyvSfVjQeL0'
    },
    {
        'name': 'Cadeira Flexora',
        'description': 'Deite-se na máquina de curl de pernas, posicionando os tornozelos sob a almofada e os joelhos alinhados com o eixo da máquina. Flexione os joelhos, levando os calcanhares em direção aos glúteos, contraindo os isquiotibiais. Retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=1Tq3QdYUuHs'
    },
    {
        'name': 'Stiff',
        'description': 'Em pé, segure a barra à frente do corpo com os braços estendidos. Mantendo as pernas quase estendidas e as costas retas, incline o tronco à frente, empurrando o quadril para trás, abaixando a barra até a altura das canelas. Retorne à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=VA0_lg0LLPk'
    },
    {
        'name': 'Agachamento Hack',
        'description': 'Posicione-se na máquina Hack, com os pés na largura dos ombros. Destrave a plataforma, flexione os joelhos e quadris, abaixando o corpo, e depois estenda as pernas para retornar à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=0tn5K9NlCfo'
    },
    {
        'name': 'Agachamento Frontal',
        'description': 'Em pé, com os pés na largura dos ombros, coloque a barra na frente do corpo, apoiada nos deltoides anteriores e clavículas. Flexione os joelhos e quadris, abaixando o corpo como se fosse sentar em uma cadeira, mantendo as costas retas e o peito erguido. Retorne à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=m4ytaCJZpl0'
    },
    {
        'name': 'Agachamento Sumô',
        'description': 'Em pé, com os pés mais afastados que a largura dos ombros e os dedos apontando para fora, segure um halter ou kettlebell entre as pernas. Flexione os joelhos e quadris, abaixando o corpo, mantendo as costas retas e o peito erguido. Retorne à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=qQZEcJpRWUA'
    },
    {
        'name': 'Avanço (Lunges)',
        'description': 'Em pé, segurando halteres ao lado do corpo ou uma barra nas costas, dê um passo à frente com uma perna. Flexione ambos os joelhos até que a coxa da frente fique paralela ao chão e o joelho de trás quase toque o chão. Empurre o pé da frente para retornar à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=QOVaHwm-Q6U'
    },
    {
        'name': 'Avanço Reverso',
        'description': 'Em pé, segurando halteres ao lado do corpo ou uma barra nas costas, dê um passo para trás com uma perna. Flexione ambos os joelhos até que a coxa da frente fique paralela ao chão e o joelho de trás quase toque o chão. Empurre o pé da frente para retornar à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=0oaXtE3-tvo'
    },
    {
        'name': 'Agachamento Búlgaro',
        'description': 'Em pé, posicione uma perna para trás sobre um banco, com o peito do pé apoiado. A perna da frente deve estar à frente do corpo, na largura dos ombros. Flexione o joelho da frente, abaixando o corpo até que a coxa fique paralela ao chão. Retorne à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=hPlKPjohFS0'
    },
    {
        'name': 'Abdução de Quadril na Máquina',
        'description': 'Sente-se na máquina de abdução de quadril, posicionando as almofadas laterais contra a parte externa das coxas. Afaste as pernas, abrindo os joelhos, e depois retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=Gt9a4fu_mmQ'
    },
    {
        'name': 'Adução de Quadril na Máquina',
        'description': 'Sente-se na máquina de adução de quadril, posicionando as almofadas laterais contra a parte interna das coxas. Aproxime as pernas, fechando os joelhos, e depois retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=ykfbYVU6-_E'
    },
    {
        'name': 'Leg Press 45°',
        'description': 'Sente-se na máquina Leg Press 45°, posicione os pés na plataforma na largura dos ombros. Destrave a plataforma, flexione os joelhos, trazendo-os em direção ao peito, e depois estenda as pernas sem travar os joelhos no topo.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=JLVy8BpsOD8'
    },
    {
        'name': 'Flexora em Pé',
        'description': 'Posicione-se na máquina flexora em pé, ajustando a almofada sobre o tendão de Aquiles. Flexione o joelho, levando o calcanhar em direção ao glúteo, contraindo os isquiotibiais. Retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=9wvO_2u-1yU'
    },
    {
        'name': 'Flexora Sentada',
        'description': 'Sente-se na máquina flexora sentada, ajustando a almofada sobre os calcanhares. Flexione os joelhos, puxando as pernas para trás, contraindo os isquiotibiais. Retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=F_y1Faf9SOU'
    },
    {
        'name': 'Elevação Pélvica (Hip Thrust)',
        'description': 'Sente-se no chão com as escápulas apoiadas em um banco, joelhos flexionados e pés apoiados no chão. Coloque uma barra ou peso sobre o quadril. Eleve o quadril, estendendo-o até que o corpo forme uma linha reta do joelho ao ombro. Retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=Zp26q4BY5HE'
    },
    {
        'name': 'Elevação Pélvica Unilateral',
        'description': 'Sente-se no chão com as escápulas apoiadas em um banco, um joelho flexionado e pé apoiado no chão, e a outra perna estendida. Eleve o quadril, estendendo-o até que o corpo forme uma linha reta do joelho ao ombro. Retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=hUboSbJdvvU'
    },
    {
        'name': 'Step Up',
        'description': 'Em pé, de frente para um banco ou plataforma, segure halteres ao lado do corpo. Coloque um pé sobre o banco e empurre-se para cima, estendendo a perna de apoio, até que ambos os pés estejam sobre o banco. Retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=dQqApCGd5Ss'
    },
    {
        'name': 'Extensão de Quadril na Polia',
        'description': 'Em pé, de frente para uma polia baixa, prenda a correia no tornozelo. Mantendo a perna de apoio levemente flexionada e o tronco ligeiramente inclinado para frente, estenda a perna com a correia para trás, contraindo o glúteo. Retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=cUi3CgBTbkY'
    },
    {
        'name': 'Abdução de Quadril com Caneleira',
        'description': 'Deite-se de lado no chão, com a cabeça apoiada no braço. Coloque uma caneleira no tornozelo da perna que ficará por cima. Mantendo a perna de baixo levemente flexionada, eleve a perna de cima, abrindo o quadril, e depois abaixe-a controladamente.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=jgh6sGwtTwk'
    },
    {
        'name': 'Agachamento com Salto',
        'description': 'Em pé, com os pés na largura dos ombros, realize um agachamento normal. Ao retornar à posição inicial, impulsione-se para cima em um salto explosivo. Aterrisse suavemente, amortecendo o impacto ao flexionar levemente os joelhos, e repita o movimento.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=TVDuUYA_8n4'
    },
    {
        'name': 'Agachamento Sissy',
        'description': 'Em pé, com os pés juntos e as mãos estendidas à frente ou segurando um apoio, desça em um agachamento profundo, mantendo os calcanhares no chão e as costas o mais retas possível. Retorne à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=c8L8LYBRU6w'
    },
    {
        'name': 'Bom Dia',
        'description': 'Em pé, coloque uma barra nas costas, apoiada nos trapézios. Mantendo as pernas quase estendidas e as costas retas, incline o tronco à frente, empurrando o quadril para trás, até que o tronco esteja quase paralelo ao chão. Retorne à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=Xh-gmFLNdvI'
    },
    {
        'name': 'Passada Lateral',
        'description': 'Em pé, com os pés juntos, dê um passo lateral com uma perna, flexionando o joelho e quadril e mantendo a outra perna estendida. Empurre o pé em movimento para retornar à posição inicial. Pode ser realizado com ou sem peso adicional.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=fPuUa9NcfBU'
    },
        {
        'name': 'Agachamento Pistol',
        'description': 'Em pé, sobre uma perna, estenda a outra perna à frente. Mantendo a perna estendida elevada, abaixe o corpo em um agachamento unilateral até que a coxa da perna de apoio fique quase paralela ao chão. Retorne à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=vq5-vdgJc0I'
    },
    {
        'name': 'Agachamento com Kettlebell (Goblet Squat)',
        'description': 'Em pé, segure um kettlebell junto ao peito com as duas mãos. Com os pés na largura dos ombros, realize um agachamento, mantendo as costas retas e o peito erguido. Retorne à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=QrVgpDOLlgM'
    },
    {
        'name': 'Agachamento Isométrico na Parede (Wall Sit)',
        'description': 'Apoie as costas em uma parede, abaixe o corpo até que as coxas fiquem paralelas ao chão, formando um ângulo de 90 graus nos joelhos. Mantenha essa posição pelo tempo desejado.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=XULOKw4E4P4'
    },
    {
        'name': 'Afundo (Walking Lunges)',
        'description': 'Em pé, segurando halteres ao lado do corpo ou uma barra nas costas, dê um passo à frente com uma perna. Flexione ambos os joelhos até que a coxa da frente fique paralela ao chão e o joelho de trás quase toque o chão. Empurre o pé da frente e avance com a outra perna, continuando o movimento.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=L8fvypPrzzs'
    },
    {
        'name': 'Ponte de Glúteos',
        'description': 'Deite-se de costas no chão, com os joelhos flexionados e os pés apoiados no chão. Eleve o quadril, contraindo os glúteos, até que o corpo forme uma linha reta do joelho ao ombro. Retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=wPM8icPu6H8'
    },
    {
        'name': 'Flexão Plantar Sentado (Panturrilha)',
        'description': 'Sentado na máquina de panturrilha, posicione as pontas dos pés na plataforma e os joelhos sob as almofadas. Eleve os calcanhares, contraindo as panturrilhas, e depois abaixe-os controladamente.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=JbyjNymZOt0'
    },
    {
        'name': 'Flexão Plantar em Pé (Panturrilha)',
        'description': 'Em pé, com as pontas dos pés sobre um degrau ou plataforma e os calcanhares no ar, eleve-se na ponta dos pés, contraindo as panturrilhas. Abaixe os calcanhares abaixo do nível da plataforma e repita.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=wxwY7GXxL4k'
    },
    {
        'name': 'Flexão Plantar no Leg Press (Panturrilha)',
        'description': 'Sentado na máquina leg press, posicione as pontas dos pés na parte inferior da plataforma. Empurre a plataforma estendendo os tornozelos, e depois flexione-os controladamente.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=UC1oiV7PzXU'
    },
    {
        'name': 'Agachamento com TRX',
        'description': 'Em pé, segure as alças do TRX com os braços estendidos à frente. Abaixe o corpo em um agachamento, mantendo as costas retas e o peito erguido, usando o TRX para auxiliar no equilíbrio. Retorne à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=nMHCVuMXMKY'
    },
    {
        'name': 'Ponte Unilateral',
        'description': 'Deite-se de costas no chão, com os joelhos flexionados e os pés apoiados no chão. Estenda uma perna e eleve o quadril, contraindo os glúteos, até que o corpo forme uma linha reta do joelho ao ombro. Retorne controladamente à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=mQf7UgIPT-s'
    }
]

# Função para adicionar os exercícios ao banco de dados
def adicionar_exercicios_pernas():
    with app.app_context():
        # Adicionar cada exercício ao banco de dados
        for exercicio in exercicios_pernas:
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
        print(f"Foram adicionados {len(exercicios_pernas)} exercícios de pernas ao banco de dados!")