from flask import Flask, request
from models.task import Task

app = Flask(__name__) 

# CRUD
# CREATE, READ, UPDATE AND DELETE
# Tabela: Tarefa - criar, ler, atualizar e deletar.

tasks = [] # como não está usando BD, usa uma lista


# POST 
@app.route("/tasks", methods=['POST'])
def create_task():
    data = request.get_json() # request vem do Flask - recuperar as informações
    print(data)
    return 'Teste'







# MAIN
if __name__ == "__main__":
    app.run(debug=True)