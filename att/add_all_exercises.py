# add_all_exercises.py
from app import app, db, Exercise
from exercicios_gluteos import adicionar_exercicios_gluteos
from exercicios_lombar import adicionar_exercicios_lombar
from exercicios_panturrilha import adicionar_exercicios_panturrilha
from exercicios_cardio import adicionar_exercicios_cardio
from exercicios_abdomen import adicionar_exercicios_abdomen
from exercicios_biceps import adicionar_exercicios_biceps
from exercicios_costas import adicionar_exercicios_costas
from exercicios_ombros import adicionar_exercicios_ombros
from exercicios_triceps import adicionar_exercicios_triceps
from exercicios_peito import adicionar_exercicios_peito
from exercicios_pernas import adicionar_exercicios_pernas



def adicionar_todos_exercicios():
    # Adicionar todos os grupos de exercícios
    adicionar_exercicios_gluteos()
    adicionar_exercicios_lombar()
    adicionar_exercicios_panturrilha()
    adicionar_exercicios_cardio()
    adicionar_exercicios_abdomen()
    adicionar_exercicios_biceps()
    adicionar_exercicios_costas()
    adicionar_exercicios_ombros()
    adicionar_exercicios_triceps()
    adicionar_exercicios_peito()
    adicionar_exercicios_pernas()
    


    
    # Contar o total de exercícios no banco de dados
    with app.app_context():
        total_exercicios = Exercise.query.count()
        print(f"Total de exercícios no banco de dados: {total_exercicios}")

if __name__ == "__main__":
    adicionar_todos_exercicios()