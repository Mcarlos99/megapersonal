from app import app, db, Exercise

# Exercícios de TRÍCEPS (25 exercícios)
exercicios_triceps = [
    {
        'name': 'Tríceps Corda na Polia',
        'description': 'Em pé, de frente para a polia alta, segure a corda com as duas mãos. Com os cotovelos junto ao corpo, estenda os braços, separando as pontas da corda para os lados no final do movimento. Retorne controladamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=vB5OHsJ3EME'
    },
    {
        'name': 'Tríceps Barra na Polia',
        'description': 'Em pé, de frente para a polia alta, segure a barra com as duas mãos. Com os cotovelos junto ao corpo, estenda os braços, empurrando a barra para baixo até que os braços estejam completamente estendidos. Retorne controladamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=2-LAMcpzODU'
    },
    {
        'name': 'Tríceps Francês com Halter',
        'description': 'Sentado ou em pé, segure um halter com as duas mãos atrás da cabeça, com os cotovelos flexionados. Estenda os cotovelos, elevando o halter até que os braços estejam completamente estendidos acima da cabeça.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=m9me06UBPKc'
    },
    {
        'name': 'Tríceps Francês com Barra EZ',
        'description': 'Sentado ou em pé, segure uma barra EZ com as duas mãos acima da cabeça, com os cotovelos flexionados. Estenda os cotovelos, elevando a barra até que os braços estejam completamente estendidos acima da cabeça.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=30ahR_z-V_c'
    },
    {
        'name': 'Tríceps Testa com Barra',
        'description': 'Deitado em um banco reto, segure uma barra acima do peito com os braços estendidos. Flexione os cotovelos, abaixando a barra até próximo à testa, e estenda-os novamente, retornando à posição inicial.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=NIWKqMm0Nqw'
    },
    {
        'name': 'Tríceps Testa com Barra EZ',
        'description': 'Deitado em um banco reto, segure uma barra EZ acima do peito com os braços estendidos. Flexione os cotovelos, abaixando a barra até próximo à testa, e estenda-os novamente, retornando à posição inicial.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=L0AK_mxJDJQ'
    },
    {
        'name': 'Tríceps Testa com Halteres',
        'description': 'Deitado em um banco reto, segure um halter em cada mão acima do peito com os braços estendidos. Flexione os cotovelos, abaixando os halteres até próximo à testa, e estenda-os novamente, retornando à posição inicial.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=DGGZVlPd2XI'
    },
    {
        'name': 'Supino Fechado com Barra',
        'description': 'Deitado em um banco reto, segure a barra com as mãos próximas (menos que a largura dos ombros). Abaixe a barra até o peito e empurre-a para cima estendendo os braços completamente, focando na contração dos tríceps.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=nEF0bv2FW94'
    },
    {
        'name': 'Mergulho no Banco (Dips)',
        'description': 'Posicione as mãos no banco atrás de você, com os dedos voltados para frente. Estenda as pernas à frente, mantendo os quadris próximos ao banco. Flexione os cotovelos até aproximadamente 90 graus e empurre-se para cima novamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=jdFzYGmvDyg'
    },
    {
        'name': 'Mergulho Entre Barras Paralelas',
        'description': 'Apoie-se em barras paralelas, com os braços estendidos. Abaixe o corpo flexionando os cotovelos até aproximadamente 90 graus, mantendo os cotovelos junto ao corpo, e empurre-se para cima novamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=2z8JmcrW-As'
    },
    {
        'name': 'Tríceps Coice com Halter',
        'description': 'Incline o tronco para frente, mantendo as costas retas e os joelhos levemente flexionados. Segure um halter com uma mão, mantendo o cotovelo flexionado e junto ao corpo. Estenda o cotovelo, empurrando o halter para trás, e retorne controladamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=aVj6K7v6gl4'
    },
    {
        'name': 'Tríceps Coice com Cabo',
        'description': 'Em pé, de lado para uma polia baixa, segure a alça com uma mão, mantendo o cotovelo flexionado e junto ao corpo. Estenda o cotovelo, empurrando a alça para trás, e retorne controladamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=vPgKZJDsN-4'
    },
    {
        'name': 'Extensão de Tríceps Deitado com Halteres',
        'description': 'Deitado em um banco reto, segure um halter em cada mão acima do peito com os braços estendidos. Mantendo a parte superior dos braços estacionária, flexione os cotovelos, abaixando os halteres ao lado da cabeça, e estenda-os novamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=THC3uDR8NsA'
    },
    {
        'name': 'Extensão de Tríceps no Banco Inclinado',
        'description': 'Deitado em um banco inclinado, segure um halter em cada mão acima do peito com os braços estendidos. Mantendo a parte superior dos braços estacionária, flexione os cotovelos, abaixando os halteres ao lado da cabeça, e estenda-os novamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=Qrd6YuC-QeM'
    },
    {
        'name': 'Tríceps Corda Invertido',
        'description': 'Em pé, de costas para a polia baixa, segure a corda com as duas mãos. Com os cotovelos junto ao corpo e para cima, estenda os braços para frente, separando as pontas da corda para os lados no final do movimento. Retorne controladamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=IeLtMPIHhNI'
    },
    {
        'name': 'Tríceps Mergulho na Máquina',
        'description': 'Sente-se na máquina de mergulho para tríceps, segure as alças e estenda os braços completamente para baixo. Retorne controladamente à posição inicial, flexionando os cotovelos.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=Hd-u9Vh3Clc'
    },
    {
        'name': 'Tríceps na Polia com Uma Mão',
        'description': 'Em pé, de lado para a polia alta, segure a alça com uma mão. Com o cotovelo junto ao corpo, estenda o braço, empurrando a alça para baixo até que o braço esteja completamente estendido. Retorne controladamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=nZS7PvK8VWg'
    },
    {
        'name': 'Tríceps Testa na Polia',
        'description': 'Sentado ou em pé, de costas para a polia alta, segure a corda ou barra acima e atrás da cabeça. Estenda os cotovelos, empurrando a corda para cima até que os braços estejam completamente estendidos. Retorne controladamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=MkOCxJCj0gA'
    },
    {
        'name': 'Tríceps Kickback com Cabo em V',
        'description': 'Em pé, inclinado para frente, segure um cabo em V conectado a uma polia baixa. Com os cotovelos junto ao corpo e flexionados a 90 graus, estenda os braços para trás, contraindo os tríceps no final do movimento. Retorne controladamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=z6K2Sfn_Hlg'
    },
    {
        'name': 'Flexão Fechada (Diamond Push-up)',
        'description': 'Posicione-se na posição de flexão, com as mãos juntas formando um diamante com os polegares e indicadores. Abaixe o corpo flexionando os cotovelos, mantendo-os junto ao corpo, e empurre-se para cima novamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=J0DnG1_S92I'
    },
    {
        'name': 'Tríceps com Banco (Bench Dips)',
        'description': 'Posicione as mãos em um banco atrás de você, com os dedos voltados para frente e as pernas estendidas à frente. Abaixe o corpo flexionando os cotovelos e empurre-se para cima novamente. Para maior intensidade, eleve os pés em outro banco.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=0326dy_-CzM'
    },
    {
        'name': 'Tríceps no TRX',
        'description': 'Segure as alças do TRX com as mãos e posicione-se de frente para o ponto de ancoragem. Incline-se para frente com os braços estendidos. Flexione os cotovelos, abaixando o corpo, e empurre-se para cima novamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=eXs5HAl-t_o'
    },
    {
        'name': 'Tríceps com Barra V na Polia (V-Bar Pushdown)',
        'description': 'Em pé, de frente para a polia alta, segure a barra V com as duas mãos. Com os cotovelos junto ao corpo, estenda os braços, empurrando a barra para baixo até que os braços estejam completamente estendidos. Retorne controladamente.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=2kMhxCpL3Hs'
    },
    {
        'name': 'Tríceps Testa com Barra no Smith',
        'description': 'Deitado em um banco reto posicionado na máquina Smith, ajuste a barra acima do peito com os braços estendidos. Flexione os cotovelos, abaixando a barra até próximo à testa, e estenda-os novamente, retornando à posição inicial.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=ZvpBLQpPC8c'
    },
    {
        'name': 'Tríceps na Polia Alta com Corda (Overhead Extension)',
        'description': 'Em pé, de costas para a polia baixa, segure a corda com as duas mãos acima da cabeça. Mantendo os braços próximos às orelhas, estenda os cotovelos completamente e retorne controladamente à posição inicial.',
        'muscle_group': 'Tríceps',
        'video_url': 'https://www.youtube.com/watch?v=jkG4sTdSnNI'
    }
]

# Função para adicionar os exercícios ao banco de dados
def adicionar_exercicios_triceps():
    with app.app_context():
        # Adicionar cada exercício ao banco de dados
        for exercicio in exercicios_triceps:
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
        db.session.commit
        print(f"Foram adicionados {len(exercicios_triceps)} exercícios de triceps ao banco de dados!")