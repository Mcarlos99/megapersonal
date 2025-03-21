# save_as_recreate_db.py
from app import app, db
import os

# Caminho para o banco de dados
db_path = 'megapersonal.db'

# Exclui o banco de dados se existir
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Banco de dados '{db_path}' excluído com sucesso.")
else:
    print(f"Banco de dados '{db_path}' não encontrado.")

# Cria as tabelas com o novo esquema
with app.app_context():
    db.create_all()
    print("Novas tabelas foram criadas com sucesso.")

print("Banco de dados foi recriado com sucesso!")