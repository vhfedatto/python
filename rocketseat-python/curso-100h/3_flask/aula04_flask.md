# LESSON 04 - FLASK
## INTRODUÇÃO AO FLASK

- Flask -> Framework leve e poderoso para construir aplicações web em Python
- Framework -> Conjunto de ferramentas, bibliotecas e convenções que fornecem uma estrutura para desenvolver aplicações.

> Vantagens: Simplicidade (Código legível, intuitivo, popular para iniciantes), Escalabilidade (), Flexibilidade ().

- Lançado em 01/04/2010, por Ronacher.
- Ideia do Flask: Criar um framework simples e fácil de usar - mas também ser poderoso e capaz de suportar o desenvolvimento de aplicações web robustas.
- Filosofia central: Manter a simplicidade e fornecer aos desenvolvedores a liberdade para escolherem suas próprias ferramentas e abordagens de desenvolvimento.

- Usos: Pinteres, LinkedIn, Netflix, Uber. 

- É uma biblioteca externa. Tem que instalar.

### Como Instalar?
```bash
pip3 install Flask==2.3.0
```

- Crie um arquivo de requisito: "requirements.txt" -> Vai ter todas as dependências do projeto.

```text
Flask==2.3.0
Flask-SQLAlchemy==3.1.1
Flask-Cors==3.0.10
Werkzeug==2.3.0
```

- Baixar a instalação das dependências

```bash
pip3 install -r requirements.txt
```
- Primeiro projeto:

```python
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
```
---

## CONCEITOS: API E API Rest

- Comunicação é algo muito importante.

- API (Application Programming **Interface**) -> Porta de entrada, forma de estabelecer essa comunicação. Um dos lados é o sistema, que oferece uma API para que outro sistema possa se conectar.

> API -> Conjunto de regras, protocolos e ferramentas, que permitem que diferentes softwares se comuniquem entre si. Ponte que permite que aplicativos diferentes troquem informações.

Exemplo:

```
Client (browser) -> Request -> API -> API server 
API server -> API -> Response -> Client (browser)
```

- Sistemas precisam ter um conjunto de regras que permitem que se comuniquem de forma eficaz.
- O request precisa ser entendido pelo API server para gerar uma Response.

### API Rest

> Rest -> Representational State Transfer

- Conjunto de regras que essa comunicação aconteça de forma fluída.
- Regras precisam ser respeitadas.
- Rest se baseia no protocolo HTTP -> Que tem operações já existentes (GET, POST, PUT, DELETE E PATCH)
    - Ajudam a entender a finalidade da request.
    - Com isso, é possível acessar os recursos (endpoints)
    - Formato de representação -> json ou xml para retornar o response. Formato de devolver a informação para o cliente.
    
    Client --http (GPPDP) & URL (endpoint)--> Server

    Server --json & xml --> Client

### API Restful

> Quando respeita todos os fundamentos do Rest - é um adjetivo que se dá a uma API Rest.

- APIs que já foram construídas e que respeitam todos os conceitos da API Rest.

---

## Métodos de Requisição HTTP

[Documentação HTTP da Mozilla](https://developer.mozilla.org/pt-BR/docs/Web/HTTP)

- ```GET``` -> Solicita a representação de um recurso -> O estado atual dele (o endpoint). RETORNAR DADOS! 

- ```POST``` -> Inserir informações a um recurso específico.

- ```PUT``` -> ATUALIZAÇÕES -> Cliente já cadastrado pelo ```POST```, puxa as informações pelo ```GET```, atualiza os dados usando ```PUT``` -> Substitui TODAS as informações atuais. Sou obrigado a ENVIAR TUDO!

- ```PATCH``` -> ATUALIZAR, modificações PARCIAIS -> APENAS ALGUMAS INFORMAÇÕES.

- ```DELETE``` -> Remove o recurso específico. Cliente cadastrado, requisição Delete, remove.


## Códigos de Resposta HTTP

[Códigos de Resposta - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)
[Cats - Código de Resposta](https://http.cat/)

- **INFORMATIVAS** (100-199): Voltam uma informação -> Mas não diz se deu certo ou não.

- ✅ **BEM-SUCEDIDAS** (200-299): Diz que deu tudo certo! Requisição deu tudo certo - inserir, atualizar, deletar, buscar... (+ usados: 200, 201)

- ⚠ **REDIRECIONAMENTO** (300-399): Tenta acessar um recurso que mudou de lugar. Acessar uma página que não existe mais naquele endereço. Redireciona.

- ❌🚹 **ERRO DO CLIENT** (400-499): Client envia o formato do CEP no envio de um formulário -> Sistema envia um 400, pq é o Client que errou na requisição. 404 = não encontrado. (+ usados: 400, 401 - não ta logado, 403 - já sabe quem é o cliente, 404 - servidor não achou o recurso). 

- ❌💾 **ERRO DO SERVER** (500-599): Erros dentro do servidor. Client fez tudo correto, mas teve um erro no BD, por exemplo, ai lança um 500 (internal server error), a aplicação entende que o erro foi no servidor e não no formato enviado. (+ comum: 500 - abrir um suporte para eles resolverem).

---

## DOCUMENTAÇÃO DE API COM SWAGGER

Importância:
1. **Antes da construção**: Visualizar como vão funcionar os endpoints, quais os tipos de resposta, quais os parâmetros para receber - Visão da API de como ela deve ser.

2. **Depois da construção**: Stakeholders farão uso da documentação para entender como a sua API funciona.

> **Swagger**: Dá exemplo de como uma API pode ser documentada. [Editor - Swagger](https://editor.swagger.io/) 

---

## TESTES DE API COM POSTMAN (APIDOG, INSOMNIA)

- Coleção -> Agrupamento de requisições (Get, Post, Put, Delete...)

- Vá no Swagger, baixe o YAML, vai no Postman > Import (faça login ou sign-in) > Coloca o .yaml > ele cria a coleção com todas as requisições do swagger.

- Vá em **Environments** > New > Nome > variável é o nome que tá no yaml (nesse caso, "baseUrl") > initial value: link do 127.0.0.1:5000.
- Volte na sua coleção e selecione o seu novo environment no icone superior direito de "Environment".

- Essa parte do "Environment" é importante para você não ter que ficar trocando no teu código quando o baseUrl mudar (tipo rodar em AWS etc.).

---

## GIT, GITHUB X GITLAB X BITBUCKET

> Git: Software de código aberto para VERSIONAMENTO de código - sucessor do SVN.

- Caso tenha um problema, você pode voltar para a versão anterior.
- Diversas outras empresas usam o Git, mas com uma interface mais bonita etc (github, gitlab...)

> GitHub: Local com diversos repositórios públicos, privados, para armazenar os seus códigos. Mais usados por programadores.

> GitLab: Não é só uma ferramenta para versionamento, pois possui uma esteira de CI/CD para implementação do código. Mais comum em empresas.

> BitBucket: Mais usado em empresas também, pois tem uma boa integração com o Jira - usado pela galera dos Métodos Ágeis - controle de atividades.

---

### GitHub
- Roda todos os tipos de arquivo - versiona todos os tipos de arquivo.

> Ramificações: Separação melhor do código

Hora de criar o repositório do projeto: "tasks-flask-crud" + ReadMe + Public + gitignore= "python".

Meu repositório: [vhfedatto/tasks-flask]()


#### Baixar o repositório:
```git
git clone [link do repositorio]
```



---