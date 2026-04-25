#Titulos:
def titulo(txt):
    print('-'*60)
    print(' '*15,txt)
    print('-'*60)
    
def titulo2(txt):
    print('-'*60)
    print(' '*7,txt)
    print('-'*60)

#Entrar no site:
def tela_inicial():
    while True:
        titulo("Bem-vindo à Folhas e Letras")
        print('1. Entrar')
        print('2. Sair')
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            tela_login()
        elif escolha == '2':
            print("Saindo da aplicação. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


#Login
def tela_login():
    while True:
        titulo('Você já é um cliente?')
        login_choise = input("[S/N]").strip().upper()
        if login_choise == 'S':
            titulo("Seja Bem-vindo de volta!")
            cliente_encontrado = None

            while not cliente_encontrado:
                print("Informe seus dados para entrar:")
                username = input('Username: ')
                password = input("Senha: ")
                if username == 'adm' and password == 'adm123':
                    exibir_relatorio_vendas()
                else:
                    cliente_encontrado = None
                for cliente in clientes.values():
                    if cliente['login'] == username and cliente['senha'] == password:
                        cliente_encontrado = cliente
                        break
                if cliente_encontrado:
                    titulo2(f"Olá {cliente_encontrado['nome']}, estávamos esperando por você!")
                else:
                    print("Username ou senha inválidos. Tente novamente.\n")

        else:
            print('Vamos criar uma conta para você!')
            print('Para isso, responda os campos abaixo:')
            login = input("\nDigite o seu nome de login: ")
            senha = input("Digite a sua senha: ")
            nome = input("Digite o seu nome completo: ")
            email = input("Digite o seu email: ")
            telefone = input("Digite o telefone: ")
            endereco = input("Digite o seu endereço: ")
            data_nascimento = input("Digite a sua data de nascimento: ")

            cliente_id = 'cliente' + str(len(clientes) + 1)
            clientes[cliente_id] = {
                'login': login,
                'senha': senha,
                'nome': nome,
                'email': email,
                'telefone': telefone,
                'endereco': endereco,
                'data_nascimento': data_nascimento
            }
            cliente_encontrado = clientes[cliente_id]
            titulo2(f"Cadastro realizado com sucesso, {nome}!")



#Home - pagina inicial
def home(txt):
    while True:
        print('-'*60)
        print(' '*15, txt)
        print('-'*60)
        print('1. Ver Produtos')
        print('2. Adicionar ao carrinho')
        print('3. Ver carrinho')
        print('4. Remover ou ajustar os itens do carrinho')
        print('5. Finalizar compra')
        print('6. Sair')
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            exibir_produtos()
        elif opcao == '2':
            carrinho_add()
        elif opcao == '3':
            exibir_carrinho()
        elif opcao == '4':
            remover_do_carrinho()
        elif opcao == '5':
            finalizar_compra()
            print("Compra finalizada. Obrigado por comprar conosco!")
            break
        elif opcao == '6':
            print("Saindo da loja. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

#Opção 01 - Exibindo Produtos
def exibir_produtos():
    titulo("Livros Disponíveis")
    for codigo, info in produtos.items():
        print(f"ID: {codigo} | Nome: {info['nome']} | Autor: {info['autor']}")
        print(f"Estilo: {info['estilo']} | Preço: R${info['preco']} | Em Estoque: {info['estoque']}")
        print('-' * 60)

#Opção 02 - Adicionando ao carrinho
def carrinho_add():
    produto_id = input("Digite o ID do produto que deseja adicionar ao carrinho: ").strip()
    if produto_id in produtos:
        quantidade = int(input("Digite a quantidade: "))
        while quantidade > produtos[produto_id]['estoque']:
            print("Quantidade solicitada não disponível em estoque. Escolha novamente")
            quantidade = int(input("Digite a quantidade: "))

        if produto_id in carrinho:
            carrinho[produto_id]['quantidade'] += quantidade
        else:
            carrinho[produto_id] = {
                'nome': produtos[produto_id]['nome'],
                'preco': produtos[produto_id]['preco'],
                'quantidade': quantidade
            }
        produtos[produto_id]['estoque'] -= quantidade
        print(f"{quantidade} unidade(s) de '{produtos[produto_id]['nome']}' foram adicionadas ao carrinho.")
    else:
        print("ID de produto inválido.")

#Opção 03 - exibindo o carrinho
def exibir_carrinho():
    titulo('Seu Carrinho')
    if not carrinho:
        print("O carrinho está vazio.")
    else:
        total = 0
        for produto_id, item in carrinho.items():
            subtotal = item['preco'] * item['quantidade']
            total += subtotal
            # Incluindo o ID do produto ao lado dos detalhes
            print(f"ID: {produto_id} | {item['nome']} - {item['quantidade']} unidade(s) - R${subtotal:.2f}")
        print('-' * 60)
        print(f"Total: R${total:.2f}")


#Opção 04 - removendo do carrinho
def remover_do_carrinho():
    if not carrinho:
        print("O carrinho está vazio.")
        return
    exibir_carrinho()
    produto_id = input('Digite o ID do produto que deseja editar: ').strip()
    if produto_id in carrinho:
        qtde = carrinho[produto_id]['quantidade']
        print(f"Quantidade atual de {carrinho[produto_id]['nome']}':{qtde}")
        new_qtde = input('Digite quantos queres que permaneça (0 para remover): ').strip()

        if new_qtde.isdigit():
            new_qtde = int(new_qtde)
        
            if new_qtde == 0:
                produtos[produto_id]['estoque'] += qtde
                del carrinho[produto_id]
                print(f"'{carrinho[produto_id]['nome']}' foi removido do carrinho.")
            elif new_qtde < qtde:
                quantidade_retirada = qtde - new_qtde
                produtos[produto_id]['estoque'] += quantidade_retirada
                carrinho[produto_id]['quantidade'] = new_qtde
                print(f"Quantidade de '{carrinho[produto_id]['nome']}' foi ajustada para {new_qtde}.")
            else:
                print("A nova quantidade deve ser menor que a quantidade atual.")
        else:
            while new_qtde == False:
                print("Entrada inválida. Digite um número inteiro.")
                new_qtde = input('Digite quantos queres que permaneça (0 para remover): ').strip()   
    else:
        print("ID do produto não encontrado no carrinho.")

#Opção 05 - Finalizando a compra
def finalizar_compra():
    titulo("Finalização da Compra")
    exibir_carrinho()
    # Seleção do vendedor
    print("Vendedores disponíveis para atendimento:")
    for codigo, info in vendedores.items():
        print(f"ID: {codigo} - Nome: {info['nome']}")
    vendedor_id = input("Digite o ID do vendedor que o atendeu: ").strip()
    if vendedor_id not in vendedores:
        print("ID de vendedor inválido. Tente novamente.")
        return
    total_compra = sum(item['preco'] * item['quantidade'] for item in carrinho.values())
    imposto = total_compra * 0.25
    com_imposto = total_compra + imposto
    comissao = total_compra * 0.05
    vendedores[vendedor_id]['comissao'] += comissao

    nota_fiscal = {
        'cliente': cliente_encontrado['nome'],
        'vendedor': vendedores[vendedor_id]['nome'],
        'itens': carrinho.copy(),
        'total_sem_imposto': total_compra,
        'imposto': imposto,
        'com_imposto': com_imposto
    }

    relatorio_vendas.append(nota_fiscal)
    
    print("\n---- Nota Fiscal ----")
    print(f"Cliente: {nota_fiscal['cliente']}")
    print(f"Atendido por: {nota_fiscal['vendedor']}")
    for item_id, item_info in nota_fiscal['itens'].items():
        print(f"{item_info['nome']} - {item_info['quantidade']} unidade(s) - R${item_info['preco'] * item_info['quantidade']:.2f}")
    print(f"Subtotal: R${total_compra:.2f}")
    print(f"Imposto (25%): R${imposto:.2f}")
    print(f"Total com imposto: R${com_imposto:.2f}")
    print("Obrigado por sua compra!\n")

#ADM - ver o relatorio:
def exibir_relatorio_vendas():
    titulo("Relatório de Vendas - Acesso Administrativo")
    if not relatorio_vendas:
        print("Nenhuma venda registrada ainda.")
    else:
        total_vendas = 0
        total_impostos = 0
        total_livros = 0

        for venda in relatorio_vendas:
            total_sem_imposto = venda['total_sem_imposto']
            imposto = venda['imposto']
            total_com_imposto = venda['com_imposto']

            total_vendas += total_com_imposto
            total_impostos += imposto
            total_livros += total_sem_imposto

        print(f"Total de Vendas (com impostos): R${total_vendas:.2f}")
        print(f"Total de Impostos arrecadados: R${total_impostos:.2f}")
        print(f"Lucro bruto (livros): R${total_livros:.2f}")

        print("\nComissão por Vendedor:")
        for vendedor_id, vendedor_info in vendedores.items():
            print(f"{vendedor_info['nome']}: R${vendedor_info['comissao']:.2f}")

    input("\nPressione Enter para voltar ao menu inicial.")