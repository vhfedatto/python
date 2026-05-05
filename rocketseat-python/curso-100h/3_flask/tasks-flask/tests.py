import pytest
import requests

# CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }

    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    
    assert response.status_code == 200 # O assert diz: TEM QUE SER o valor que você disse, se não, quebra o teste.

    response_json = response.json()
    assert "message" in response_json # Não tá verificando a mensagem, apenas se ela existe
    assert "id" in response_json # Não tá verificando o id, apenas se ele existe

    tasks.append(response_json['id'])

