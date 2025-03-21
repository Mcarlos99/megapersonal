# create_tables.py
from app import app, db
from app import Trainer, Client, Exercise, Workout, WorkoutExercise, Assessment, Attendance, ClientUser

def init_db():
    with app.app_context():
        # Cria todas as tabelas baseadas nos modelos
        db.create_all()
        print("Todas as tabelas foram criadas com sucesso!")

        # Verificar se já existe algum trainer
        if Trainer.query.count() == 0:
            # Criar um trainer inicial para testes
            from werkzeug.security import generate_password_hash
            
            admin = Trainer(
                name="Admin Trainer",
                email="admin@teste.com",
                password=generate_password_hash("senha123"),
                phone="(99) 99999-9999"
            )
            db.session.add(admin)
            db.session.commit()
            print("Usuário admin criado com sucesso!")

if __name__ == "__main__":
    init_db()