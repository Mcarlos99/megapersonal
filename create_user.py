from app import app, db, Trainer
from werkzeug.security import generate_password_hash

# Cria um contexto de aplicação
with app.app_context():
    # Verifica se já existe algum trainer
    if Trainer.query.count() == 0:
        # Cria um novo trainer
        new_trainer = Trainer(
            name="Administrador",
            email="admin@admin.com",
            password=generate_password_hash("admin123"),
            phone="(11) 99999-9999"
        )
        
        # Adiciona ao banco de dados
        db.session.add(new_trainer)
        db.session.commit()
        
        print("Usuário criado com sucesso!")
        print("Email: admin@admin.com")
        print("Senha: admin123")
    else:
        print("Já existe pelo menos um usuário no sistema.")