# update_trainers.py
from app import app, db
from sqlalchemy import text

def add_is_active_column():
    with app.app_context():
        # Verificar se a coluna já existe
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        columns = [c['name'] for c in inspector.get_columns('trainer')]
        
        if 'is_active' not in columns:
            # Adicionar a coluna is_active usando a nova sintaxe
            with db.engine.connect() as conn:
                conn.execute(text('ALTER TABLE trainer ADD COLUMN is_active BOOLEAN DEFAULT TRUE'))
                conn.commit()
            print("Coluna 'is_active' adicionada com sucesso à tabela trainer!")
        else:
            print("A coluna 'is_active' já existe na tabela trainer.")

if __name__ == "__main__":
    add_is_active_column()