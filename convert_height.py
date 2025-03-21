# convert_height.py
from app import app, db, Client

def convert_heights():
    with app.app_context():
        # Buscar todos os clientes
        clients = Client.query.all()
        
        updated_count = 0
        for client in clients:
            # Se a altura estiver definida e parecer estar em centímetros (maior que 3)
            if client.height and client.height > 3:
                # Converter de cm para m
                old_height = client.height
                client.height = client.height / 100
                updated_count += 1
                print(f"Cliente {client.name}: Altura convertida de {old_height}cm para {client.height}m")
        
        # Salvar alterações
        if updated_count > 0:
            db.session.commit()
            print(f"{updated_count} clientes atualizados com sucesso!")
        else:
            print("Nenhum cliente precisou ser atualizado.")

if __name__ == "__main__":
    convert_heights()