#Produtos, conversão e frete.
#Obs: utilizei \n para poupar linhas e escrever os prints seguidos um dentro do outro.
taxa = 5.09

produtos = {
    'notebook': 750.00,
    'smartwatch': 250.00
}
frete = {
    'brasil': 52.00,
    'argentina': 75.00
}

def titulo(txt):
    print('-'*24)
    print(' '*3, txt)

def convert(valor):
    return valor * taxa

#programa principal
titulo("Bem-vindo a loja")
titulo('   Produtos')
print('Notebook..... US$750.00 \nSmartwatch....US$250.00')

#escolha do produto:
escolha = input("Qual produto você deseja? ").lower()

if escolha in produtos:
    preco_usd = produtos[escolha]
    preco_brl = convert(preco_usd)
    print(f"O preço do {escolha} em reais é: R$ {preco_brl:.2f}")

    titulo("Locais de Envio")
    print('Brasil...... US$52.00 \nArgentina... US$75.00')

    destino = input("Para qual local o produto será enviado? ").lower()

    if destino in frete:
            frete_usd = frete[destino]
            frete_brl = convert(frete_usd)
            total_brl = preco_brl + frete_brl
            print(f"O preço do frete para {destino} em reais é: R${frete_brl:.2f}")
            print(f"\nValor total: R${total_brl:.2f}")
    else:
        print("Destino de envio inválido.")
else:
    print("Produto inválido.")

