# Criar um script chamado create_template_tables.py
from app import app, db, WorkoutTemplate, WorkoutTemplateExercise

with app.app_context():
    db.create_all()
    print("Tabelas de templates de treino criadas com sucesso!")