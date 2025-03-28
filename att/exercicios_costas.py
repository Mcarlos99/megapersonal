from app import app, db, Exercise

# Exercícios de COSTAS (25 exercícios)
exercicios_costas = [
    {
        'name': 'Puxada Frontal na Máquina',
        'description': 'Sente-se na máquina de puxada, agarre a barra com as mãos um pouco mais afastadas que a largura dos ombros. Puxe a barra para baixo até tocar a parte superior do peito, contraindo as costas, e retorne controladamente à posição inicial.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=r5O0QPNzrrM'
    },
    {
        'name': 'Puxada Aberta na Máquina',
        'description': 'Sente-se na máquina de puxada, agarre a barra com pegada aberta (mãos bem afastadas). Puxe a barra para baixo em direção ao peito, contraindo as costas, e retorne lentamente à posição inicial.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=lueEJGjTuPQ'
    },
    {
        'name': 'Puxada Fechada na Máquina',
        'description': 'Sente-se na máquina de puxada, agarre uma barra em V ou uma barra reta com as mãos próximas. Puxe a barra para baixo até tocar a parte inferior do peito, mantendo os cotovelos junto ao corpo, e retorne controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=ecRF8ERf2q4'
    },
    {
        'name': 'Puxada com Pegada Supinada',
        'description': 'Sente-se na máquina de puxada, agarre a barra com as palmas voltadas para você (supinada). Puxe a barra para baixo até a altura do peito, concentrando-se em contrair as costas, e retorne lentamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=CjgK_BLxj2w'
    },
    {
        'name': 'Remada Curvada com Barra',
        'description': 'Em pé, segure a barra com as mãos na largura dos ombros, dobre os joelhos levemente e incline o tronco à frente mantendo as costas retas. Puxe a barra em direção ao abdômen, contraindo as costas, e desça controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=kBWAon7ItDw'
    },
    {
        'name': 'Remada Curvada com Pegada Invertida',
        'description': 'Realize a remada curvada segurando a barra com as palmas voltadas para cima (pegada supinada). Incline o tronco à frente mantendo as costas retas, puxe a barra em direção ao abdômen e desça controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=WHKG_D8nGNM'
    },
    {
        'name': 'Remada Unilateral com Halter',
        'description': 'Apoie um joelho e uma mão em um banco, mantendo as costas paralelas ao chão. Com a outra mão, segure um halter e puxe-o até a altura da cintura, mantendo o cotovelo próximo ao corpo. Desça controladamente e repita.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=pYcpY20QaE8'
    },
    {
        'name': 'Remada Cavalinho (Máquina T)',
        'description': 'Sente-se na máquina de remada, segure as alças e mantenha o peito apoiado no suporte. Puxe as alças para trás, aproximando-as da cintura, contraindo as costas. Retorne lentamente à posição inicial.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=9JolyuXVD0Y'
    },
    {
        'name': 'Remada Baixa no Cabo',
        'description': 'Sente-se na máquina de remada baixa, segure a barra ou alça e mantenha os joelhos levemente flexionados. Puxe a barra em direção ao abdômen, mantendo as costas retas, e retorne controladamente à posição inicial.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=GZbfZ033f74'
    },
    {
        'name': 'Remada na Máquina Hammer',
        'description': 'Sente-se na máquina Hammer para remada, ajuste a altura do banco e segure as alças. Puxe as alças para trás, contraindo as costas, e retorne controladamente à posição inicial.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=NhzIYtJMwO0'
    },
    {
        'name': 'Barra Fixa (Pull-up) com Pegada Pronada',
        'description': 'Segure a barra fixa com as palmas das mãos voltadas para frente e as mãos na largura dos ombros. Partindo da posição com braços estendidos, puxe-se para cima até que o queixo ultrapasse a barra, e desça controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=eGo4IYlbE5g'
    },
    {
        'name': 'Barra Fixa (Pull-up) com Pegada Supinada',
        'description': 'Segure a barra fixa com as palmas das mãos voltadas para você e as mãos na largura dos ombros. Partindo da posição com braços estendidos, puxe-se para cima até que o queixo ultrapasse a barra, e desça controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=XB_7En-zf_M'
    },
    {
        'name': 'Barra Fixa (Pull-up) com Pegada Neutra',
        'description': 'Segure as alças paralelas em uma barra com pegada neutra (palmas voltadas uma para a outra). Partindo da posição com braços estendidos, puxe-se para cima até que o queixo ultrapasse a altura das alças, e desça controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=JY0MZjMiA8s'
    },
    {
        'name': 'Barra Fixa (Pull-up) com Pegada Aberta',
        'description': 'Segure a barra fixa com as palmas das mãos voltadas para frente e as mãos bem afastadas. Partindo da posição com braços estendidos, puxe-se para cima até que o queixo ultrapasse a barra, e desça controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=iZ6yujqSuEE'
    },
    {
        'name': 'Levantamento Terra Convencional',
        'description': 'Em pé, posicione-se com os pés na largura dos ombros e a barra sobre eles. Flexione os joelhos e quadris, mantendo as costas retas, segure a barra e estenda o corpo levantando a barra, mantendo-a próxima às pernas.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=op9kVnSso6Q'
    },
    {
        'name': 'Levantamento Terra Sumo',
        'description': 'Em pé, posicione-se com os pés bem afastados e a barra entre eles. Flexione os joelhos e quadris, mantendo as costas retas, segure a barra com as mãos entre as pernas e estenda o corpo levantando a barra.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=XsrD5y8EIKU'
    },
    {
        'name': 'Levantamento Terra Romeno',
        'description': 'Em pé, segure a barra com as mãos na largura dos ombros. Mantendo as pernas quase estendidas e as costas retas, incline o tronco à frente, abaixando a barra até a altura das canelas, e retorne à posição inicial.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=JCXUYuzwNrM'
    },
    {
        'name': 'Puxada Alta na Polia',
        'description': 'Em pé, segure a corda ou barra de puxada com as mãos. Puxe a corda para baixo em direção ao queixo, levantando os cotovelos para cima e para fora. Contraia a parte superior das costas no topo do movimento e retorne controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=uAyrH0FJBTg'
    },
    {
        'name': 'Pullover com Corda na Polia Alta',
        'description': 'Ajoelhe-se de frente para a polia alta, segure a corda com os braços estendidos acima da cabeça. Puxe a corda para baixo e para trás, dobrando os cotovelos até que as mãos cheguem próximas à nuca, e retorne controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=mvB-Q-vIeOA'
    },
    {
        'name': 'Face Pull',
        'description': 'Em pé, de frente para a polia alta, segure a corda com as mãos. Puxe a corda em direção ao rosto, afastando os cotovelos para os lados, e retorne controladamente. Foque em contrair as costas e os ombros posteriores.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=V8dZ3pyiCBo'
    },
    {
        'name': 'Remada com Barra T',
        'description': 'Posicione-se sobre a barra T, segure as alças com os braços estendidos. Mantenha as costas retas e puxe a barra em direção ao peito, contraindo as costas, e desça controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=j3Igk5nyZE4'
    },
    {
        'name': 'Levantamento Terra com Trap Bar (Hexagonal)',
        'description': 'Posicione-se dentro da barra hexagonal, segure as alças com os braços estendidos ao lado do corpo. Flexione os joelhos e quadris, mantenha as costas retas, e estenda o corpo levantando a barra.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=1jBc5jM3VrI'
    },
    {
        'name': 'Hiperextensão (Banco Romano)',
        'description': 'Posicione-se no banco romano, com o quadril apoiado na almofada e os pés presos. Comece com o tronco flexionado para baixo, e estenda-o até que o corpo esteja em linha reta, contraindo as costas. Retorne controladamente à posição inicial.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=ph3pddpKzzw'
    },
    {
        'name': 'Puxada na Máquina Assistida',
        'description': 'Sente-se ou ajoelhe-se na máquina assistida para pull-ups, ajuste o nível de assistência, segure a barra ou alças e puxe o corpo para cima até que o queixo ultrapasse a barra. Desça controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=quFfF3XuCpI'
    },
    {
        'name': 'Remada com Corda na Polia Baixa',
        'description': 'Em pé, de frente para a polia baixa, segure a corda com os braços estendidos. Puxe a corda em direção ao abdômen, mantendo os cotovelos junto ao corpo, e retorne controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=yunz2QdNFMQ'
    },
    {
        'name': 'Pull-Over com Haltere',
        'description': 'Deite-se perpendicularmente em um banco, com apenas a parte superior das costas apoiada. Segure um haltere com as duas mãos acima do peito, abaixe-o em um arco atrás da cabeça até sentir um alongamento nas costas e no peito, e retorne à posição inicial.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=tpLnfSQJ0gg'
    },
    {
        'name': 'Remada Alta com TRX/Suspensão',
        'description': 'Segure as alças do TRX e incline o corpo para trás, mantendo os braços estendidos. Puxe o corpo para frente e para cima, dobrando os cotovelos e mantendo-os altos, contraindo as costas. Retorne controladamente à posição inicial.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=evwVlJRKnqI'
    },
    {
        'name': 'Remada Curvada com Halteres',
        'description': 'Em pé, segure um halter em cada mão, dobre os joelhos levemente e incline o tronco à frente mantendo as costas retas. Puxe os halteres em direção ao abdômen, contraindo as costas, e desça controladamente.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=roCP3wJ7YIY'
    }
]

# Função para adicionar os exercícios ao banco de dados
def adicionar_exercicios_costas():
    with app.app_context():
        # Adicionar cada exercício ao banco de dados
        for exercicio in exercicios_costas:
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
        print(f"Foram adicionados {len(exercicios_costas)} exercícios de costas ao banco de dados!")