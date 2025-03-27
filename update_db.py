# create_exercise_load_table.py
from app import app, db, ExerciseLoad

def init_exercise_load_table():
    with app.app_context():
        db.create_all()
        print("Tabela ExerciseLoad criada com sucesso!")

if __name__ == "__main__":
    init_exercise_load_table()