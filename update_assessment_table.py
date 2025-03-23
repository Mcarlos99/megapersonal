# update_assessment_table.py
from app import app, db
from sqlalchemy import text

def add_anthropometric_columns():
    with app.app_context():
        # Lista de novas colunas para adicionar
        new_columns = [
            ('neck', 'FLOAT'),
            ('shoulders', 'FLOAT'),
            ('forearms', 'FLOAT'),
            ('wrists', 'FLOAT'),
            ('calves', 'FLOAT'),
            ('ankles', 'FLOAT'),
            ('abdomen', 'FLOAT'),
            ('skinfold_triceps', 'FLOAT'),
            ('skinfold_biceps', 'FLOAT'),
            ('skinfold_subscapular', 'FLOAT'),
            ('skinfold_suprailiac', 'FLOAT'),
            ('skinfold_abdominal', 'FLOAT'),
            ('skinfold_thigh', 'FLOAT'),
            ('skinfold_calf', 'FLOAT')
        ]
        
        # Verificar quais colunas já existem
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        existing_columns = [c['name'] for c in inspector.get_columns('assessment')]
        
        # Adicionar apenas colunas que não existem ainda
        for column_name, column_type in new_columns:
            if column_name not in existing_columns:
                # Adicionar a coluna usando SQL direto
                sql = f'ALTER TABLE assessment ADD COLUMN {column_name} {column_type}'
                db.session.execute(text(sql))
                print(f"Coluna '{column_name}' adicionada com sucesso!")
            else:
                print(f"Coluna '{column_name}' já existe.")
        
        db.session.commit()
        print("Atualização da tabela assessment concluída!")

if __name__ == "__main__":
    add_anthropometric_columns()