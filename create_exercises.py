from app import app, db, Exercise

# Lista de exercícios iniciais com nome, descrição, grupo muscular e link de vídeo
initial_exercises = [
    {
        'name': 'Supino Reto com Barra',
        'description': 'O supino reto com barra é um exercício composto que trabalha principalmente os músculos peitorais, mas também envolve os deltoides anteriores e os tríceps. Deite-se em um banco plano, segure a barra com as mãos um pouco mais afastadas que a largura dos ombros, abaixe a barra até tocar levemente o peito e depois empurre de volta para cima.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=rT7DgCr-3pg'
    },
    {
        'name': 'Agachamento Livre',
        'description': 'O agachamento livre é um exercício composto que trabalha principalmente os músculos das pernas, como quadríceps, isquiotibiais e glúteos. Posicione a barra nos trapézios, mantenha o peito erguido, abaixe o corpo flexionando os joelhos e quadris até que as coxas fiquem paralelas ao chão, e então retorne à posição inicial.',
        'muscle_group': 'Pernas',
        'video_url': 'https://www.youtube.com/watch?v=SW_C1A-rejs'
    },
    {
        'name': 'Puxada Alta na Máquina',
        'description': 'A puxada alta é um exercício que trabalha principalmente os músculos das costas, especialmente o latíssimo do dorso. Segure a barra com as mãos afastadas, sente-se na máquina com os joelhos fixados, mantenha o tronco ereto, puxe a barra para baixo até que toque a parte superior do peito, e depois retorne lentamente à posição inicial.',
        'muscle_group': 'Costas',
        'video_url': 'https://www.youtube.com/watch?v=lueEJGjTuPQ'
    },
    {
        'name': 'Desenvolvimento com Halteres',
        'description': 'O desenvolvimento com halteres é um exercício que trabalha principalmente os deltoides (ombros). Sente-se em um banco com encosto, segure os halteres na altura dos ombros com as palmas voltadas para frente, empurre os halteres para cima até que os braços estejam estendidos, e depois abaixe lentamente de volta à posição inicial.',
        'muscle_group': 'Ombros',
        'video_url': 'https://www.youtube.com/watch?v=qEwKCR5JCog'
    },
    {
        'name': 'Rosca Direta com Barra',
        'description': 'A rosca direta com barra é um exercício de isolamento que trabalha principalmente os músculos bíceps. Em pé, segure a barra com as mãos na largura dos ombros e as palmas voltadas para cima, mantenha os cotovelos junto ao corpo, flexione os cotovelos para levantar a barra até os ombros, e depois abaixe lentamente de volta à posição inicial.',
        'muscle_group': 'Bíceps',
        'video_url': 'https://www.youtube.com/watch?v=in7PaeYlhrM'
    },
    {
        'name': 'Tríceps Corda',
        'description': 'O tríceps corda é um exercício de isolamento que trabalha principalmente os músculos tríceps. Utilizando a polia alta com o acessório de corda, segure as extremidades da corda com as mãos, mantenha os cotovelos junto ao corpo, estenda os antebraços para baixo até que estejam completamente esticados, e depois retorne lentamente à posição inicial.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=kiuVA7dn8p4'
    },
    {
        'name': 'Abdominal Crunch',
        'description': 'O abdominal crunch é um exercício que trabalha principalmente os músculos abdominais. Deite-se de costas com os joelhos flexionados e os pés apoiados no chão, coloque as mãos atrás da cabeça ou cruzadas sobre o peito, levante os ombros do chão contraindo os abdominais, e depois abaixe lentamente de volta.',
        'muscle_group': 'Abdômen',
        'video_url': 'https://www.youtube.com/watch?v=Xyd_fa5zoEU'
    },
    {
        'name': 'Levantamento Terra',
        'description': 'O levantamento terra é um exercício composto que trabalha vários grupos musculares, incluindo costas, glúteos, pernas e core. Posicione-se com os pés na largura dos ombros, segure a barra com as mãos afastadas, mantenha a coluna reta, levante a barra estendendo os joelhos e quadris até ficar completamente ereto, e depois abaixe a barra com controle.',
        'muscle_group': 'Lombar',
        'video_url': 'https://www.youtube.com/watch?v=1ZXobu7JvvE'
    }
]

# Cria um contexto de aplicação
with app.app_context():
    # Verifica se já existem exercícios
    if Exercise.query.count() == 0:
        for exercise_data in initial_exercises:
            exercise = Exercise(
                name=exercise_data['name'],
                description=exercise_data['description'],
                muscle_group=exercise_data['muscle_group'],
                video_url=exercise_data['video_url']
            )
            db.session.add(exercise)
        
        db.session.commit()
        print(f"Foram adicionados {len(initial_exercises)} exercícios ao banco de dados!")
    else:
        print("Já existem exercícios no banco de dados.")