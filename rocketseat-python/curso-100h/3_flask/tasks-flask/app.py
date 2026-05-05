from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__) 

# CRUD
# CREATE, READ, UPDATE AND DELETE
# Tabela: Tarefa - criar, ler, atualizar e deletar.

tasks = [] # como não está usando BD, usa uma lista
task_id_control = 1

# POST - CREATE
@app.route("/tasks", methods=['POST'])
def create_task():
    global task_id_control # Função terá acesso ao valor original da variável criada fora e poderá atualizar o valor.

    data = request.get_json() # request vem do Flask - recuperar as informações
    new_task = Task(id= task_id_control, name=data['title'], description=data.get("description", ""))
    task_id_control+=1

    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"}) # Retorno com dicionário que será um json. Melhor para as APIs conseguirem controlar no futuro.

# GET - READ
@app.route("/tasks", methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route("/tasks/<int: id>", method=['GET'])
def get_task(id): # Ver apenas uma tarefa pelo ID
    for i in tasks:
        if i.id == id:
            return jsonify(i.to_dict())
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

# No Postman, abrir um Get, colocar na URL: {{baseURL}}/tasks/id - colocar 1, 2... - só enviar e pronto.

# UPDATE - PATCH & PUT







# MAIN
if __name__ == "__main__":
    app.run(debug=True)