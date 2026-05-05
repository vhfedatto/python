from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__) 

# CRUD
# CREATE, READ, UPDATE AND DELETE
# Tabela: Tarefa - criar, ler, atualizar e deletar.

tasks = [] # como não está usando BD, usa uma lista
task_id_control = 1

# POST - CREATE
@app.route("/tasks", methods=["POST"])
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

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id): # Ver apenas uma tarefa pelo ID
    for i in tasks:
        if i.id == id:
            return jsonify(i.to_dict())
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

# No Postman, abrir um Get, colocar na URL: {{baseURL}}/tasks/id - colocar 1, 2... - só enviar e pronto.

# UPDATE - PATCH & PUT
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = None
    for i in tasks:
        if i.id == id:
            task = i
        
    if task == None:
        return({"message": "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    return jsonify({"message": "Tarefa atualizada com sucesso"})


# DELETE - DELETE
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = None
    for i in tasks:
        if i.id == id:
            task = i # Não é recomendado excluir da lista durante a iteração.
            break # Se encontrar, ele não percorre mais a lista toda sem necessidade - para quando achar.
        
    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"}), 200 # Não precisa do 200, pq já é o padrão

# MAIN
if __name__ == "__main__":
    app.run(debug=True)