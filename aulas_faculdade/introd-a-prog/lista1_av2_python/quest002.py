#Faça um dicionário que contenha as notas de três alunos em uma disciplina e calcule a média de cada um

alunos = {
    "Mateus": {"av1":9.0,"av2":10.0},
    "Ana": {"av1":7.0,"av2":9.0},
    "Adam": {"av1":8.8,"av2":7.9}
}

medias = {aluno: round((notas["av1"] + notas["av2"]) / 2, 3) for aluno, notas in alunos.items()}

for aluno, medias in medias.items():
    print(f"{aluno}: {medias}")


    