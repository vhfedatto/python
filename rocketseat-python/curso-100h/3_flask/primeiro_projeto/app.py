from flask import Flask

app = Flask(__name__) # __name__ = "__main__" -> Quando rodado de forma manual (local)

@app.route("/") # Dentro se passa o endpoint.
def hello_world():
    return "Hello World"

@app.route("/about") # As rotas são a porta de acesso para estabelecer uma comunicação entre os programas que estão acessando a informação ou usuários que queiram acessar.
def about():
    return "Página Sobre"

# Funcionar
if __name__ == "__main__": # Garantir que só execute se o app estiver sendo rodado de forma manual -> Desenvolvimento local.
    app.run(debug=True)

"""
Interpretação:

"GET /about HTTP/1.1" 200
[>>] Puxou as informações do about, foi http e 200 (padrão - quando funciona)
"""