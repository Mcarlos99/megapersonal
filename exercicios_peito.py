from app import app, db, Exercise

# Exercícios de PEITO (25 exercícios)
exercicios_peito = [
    {
        'name': 'Supino Reto com Barra',
        'description': 'Deite-se em um banco reto, segure a barra com as mãos um pouco mais afastadas que a largura dos ombros. Abaixe a barra controladamente até tocar levemente o peitoral e depois empurre para cima até estender completamente os braços, sem travar os cotovelos.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=rT7DgCr-3pg'
    },
    {
        'name': 'Supino Inclinado com Barra',
        'description': 'Deite-se em um banco inclinado (30-45°), segure a barra com as mãos um pouco mais afastadas que a largura dos ombros. Abaixe a barra controladamente até tocar levemente o peitoral superior e depois empurre para cima até estender os braços.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=SrqOu55lrYU'
    },
    {
        'name': 'Supino Declinado com Barra',
        'description': 'Deite-se em um banco declinado, segure a barra com as mãos mais afastadas que a largura dos ombros. Abaixe a barra até o peito inferior e empurre de volta para cima até estender os braços.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=LfyQBUKR8SE'
    },
    {
        'name': 'Supino Reto com Halteres',
        'description': 'Deite-se em um banco reto, segure um halter em cada mão ao lado do peito. Empurre os halteres para cima até que os braços estejam estendidos e então abaixe-os de volta à posição inicial de forma controlada.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=VmB1G1K7v94'
    },
    {
        'name': 'Supino Inclinado com Halteres',
        'description': 'Deite-se em um banco inclinado (30-45°), segure um halter em cada mão ao lado do peito. Empurre os halteres para cima até que os braços estejam estendidos e então abaixe-os de volta à posição inicial de forma controlada.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=0G2_XV7slIg'
    },
    {
        'name': 'Supino Declinado com Halteres',
        'description': 'Deite-se em um banco declinado, segure um halter em cada mão ao lado do peito inferior. Empurre os halteres para cima até que os braços estejam estendidos e então abaixe-os de volta à posição inicial de forma controlada.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=R8JuBVL3dxQ'
    },
    {
        'name': 'Crucifixo Reto com Halteres',
        'description': 'Deite-se em um banco reto, segure os halteres acima do peito com os braços estendidos e levemente flexionados. Abra os braços para os lados em um movimento de arco até sentir um alongamento no peito, então retorne à posição inicial.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=QENKPHhQVi4'
    },
    {
        'name': 'Crucifixo Inclinado com Halteres',
        'description': 'Deite-se em um banco inclinado, segure os halteres acima do peito com os braços estendidos e levemente flexionados. Abra os braços para os lados em um movimento de arco até sentir um alongamento no peito, então retorne à posição inicial.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=tJ2kaO29NDM'
    },
    {
        'name': 'Crossover no Cabo (Polias Altas)',
        'description': 'Posicione-se no centro de uma máquina de cabos com as polias altas, segure uma alça em cada mão e dê um passo à frente. Com os braços abertos e cotovelos levemente flexionados, traga as mãos em um movimento de arco à frente do corpo até se tocarem.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=taI4XduLpTk'
    },
    {
        'name': 'Crucifixo no Cabo (Polias Médias)',
        'description': 'Posicione-se no centro de uma máquina de cabos com as polias na altura do peito, segure uma alça em cada mão. Com os braços abertos e cotovelos levemente flexionados, traga as mãos em um movimento de arco à frente do corpo até se tocarem.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=Iwe6AmxVf7o'
    },
    {
        'name': 'Crucifixo no Cabo (Polias Baixas)',
        'description': 'Posicione-se no centro de uma máquina de cabos com as polias baixas, segure uma alça em cada mão. Com os braços abertos e cotovelos levemente flexionados, traga as mãos em um movimento de arco à frente do corpo e para cima até se tocarem.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=0s6uUjiooIE'
    },
    {
        'name': 'Flexão de Braço Tradicional',
        'description': 'Apoie-se no chão com as mãos na largura dos ombros e os pés juntos, mantendo o corpo reto. Flexione os cotovelos, abaixando o peito em direção ao chão, e então estenda-os para retornar à posição inicial.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=IODxDxX7oi4'
    },
    {
        'name': 'Flexão Declinada (Pés Elevados)',
        'description': 'Realize uma flexão com os pés elevados em um banco ou caixa. Isso aumenta a ênfase na parte superior do peito. Mantenha o corpo reto e abaixe-se até que o peito quase toque o chão.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=3YvfRx31xDE'
    },
    {
        'name': 'Flexão Inclinada (Mãos Elevadas)',
        'description': 'Realize uma flexão com as mãos elevadas em um banco ou caixa. Isso coloca mais ênfase na parte inferior do peito. Mantenha o corpo reto e abaixe-se até que o peito quase toque o objeto elevado.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=3YvfRx31xDE'
    },
    {
        'name': 'Flexão com Palmas Juntas (Diamond Push-up)',
        'description': 'Faça uma flexão com as mãos próximas, formando um diamante com os polegares e indicadores. Mantenha os cotovelos junto ao corpo ao descer, trabalhando mais o tríceps e o centro do peito.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=J0DnG1_S92I'
    },
    {
        'name': 'Flexão com Palmas Afastadas (Wide Push-up)',
        'description': 'Faça uma flexão com as mãos posicionadas mais afastadas que a largura dos ombros. Isso coloca mais ênfase nas partes externas do peito.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=aMnBFbs2yqE'
    },
    {
        'name': 'Supino Hammer Strength',
        'description': 'Sente-se na máquina Hammer Strength para peito, ajuste o banco e segure as alças. Empurre para frente até estender os braços completamente e depois retorne controladamente à posição inicial.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=Gk2KV3elXQY'
    },
    {
        'name': 'Peck Deck (Máquina de Voo)',
        'description': 'Sente-se na máquina Peck Deck, posicionando os antebraços nas almofadas ou segurando as alças. Pressione as almofadas/alças para a frente até que se encontrem, contraindo o peito, e depois retorne lentamente à posição inicial.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=xUm0BiZCWlQ'
    },
    {
        'name': 'Crucifixo com Máquina',
        'description': 'Sente-se na máquina de crucifixo, posicionando os cotovelos ligeiramente dobrados nas almofadas. Pressione os braços à frente até aproximá-los, contraindo o peito, e retorne controladamente à posição inicial.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=gqog4wm1LJk'
    },
    {
        'name': 'Supino com Barra Smith',
        'description': 'Deite-se em um banco reto sob a barra Smith, posicione as mãos ligeiramente mais afastadas que a largura dos ombros. Desengate a barra, abaixe-a até o peito e depois empurre para cima até estender os braços.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=l9hUpK1SZnc'
    },
    {
        'name': 'Supino Inclinado com Barra Smith',
        'description': 'Deite-se em um banco inclinado sob a barra Smith, posicione as mãos ligeiramente mais afastadas que a largura dos ombros. Desengate a barra, abaixe-a até a parte superior do peito e depois empurre para cima até estender os braços.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=9wD8xXoIBAw'
    },
    {
        'name': 'Pullover com Halter',
        'description': 'Deite-se transversalmente em um banco reto, com apenas as escápulas apoiadas. Segure um halter com ambas as mãos acima do peito, abaixe-o em um arco atrás da cabeça até sentir o alongamento no peito, e retorne à posição inicial.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=tpLnfSQJ0gg'
    },
    {
        'name': 'Flexão com Aplausos',
        'description': 'Faça uma flexão tradicional, mas ao empurrar para cima, faça-o com força suficiente para tirar as mãos do chão, bater palmas e voltar à posição inicial para a próxima repetição. Este é um exercício avançado de potência.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=EYwWCgMqDc0'
    },
    {
        'name': 'Flexão no Anel de Suspensão (TRX)',
        'description': 'Segure as alças de um TRX ou anéis de suspensão na posição de flexão. Abaixe o corpo flexionando os cotovelos e depois estenda-os para retornar à posição inicial. O equilíbrio necessário aumenta o trabalho muscular.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=DkqNc1nST6I'
    },
    {
        'name': 'Mergulho Entre Bancos para Peito',
        'description': 'Posicione-se entre dois bancos, com as mãos apoiadas em um banco atrás de você e os pés apoiados no banco à frente. Abaixe o corpo flexionando os cotovelos até sentir o alongamento no peito, e depois estenda os braços para retornar à posição inicial.',
        'muscle_group': 'Peito',
        'video_url': 'https://www.youtube.com/watch?v=jdFzYGmvDyg'
    }
]

# Função para adicionar os exercícios ao banco de dados
def adicionar_exercicios_peito():
    with app.app_context():
        # Adicionar cada exercício ao banco de dados
        for exercicio in exercicios_peito:
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
        print(f"Foram adicionados {len(exercicios_peito)} exercícios de costas ao banco de dados!")