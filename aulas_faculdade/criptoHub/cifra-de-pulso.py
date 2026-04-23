def cifra_pulso(letra_inicial):
    alfabeto = list("abcdefghijklmnopqrstuvwxyz")
    nova_ordem = [None] * 26

    # Posição base da letra inicial no alfabeto
    pos_inicial = alfabeto.index(letra_inicial.lower())
    nova_ordem[pos_inicial] = 'a'

    esquerda = pos_inicial - 1
    direita = pos_inicial + 1
    letra_atual = ord('b')

    while letra_atual <= ord('z'):
        if esquerda >= 0:
            nova_ordem[esquerda] = chr(letra_atual)
            letra_atual += 1
            esquerda -= 1
        if letra_atual <= ord('z') and direita < 26:
            nova_ordem[direita] = chr(letra_atual)
            letra_atual += 1
            direita += 1

    # Criando o mapa de substituição
    mapa = dict(zip(alfabeto, nova_ordem))

    return mapa

# Criando o mapa com 'a' sendo igual a 'p'
mapa = cifra_pulso('p')

# Exibindo o mapeamento completo
'''for k, v in mapa.items():
    print(f"{k} -> {v}")'''

# Criptografando uma mensagem simples
def criptografar(mensagem, mapa):
    return ''.join(mapa.get(c, c) for c in mensagem.lower())

mensagem = input("digite uma mensagem: ")
criptografada = criptografar(mensagem, mapa)
print(f"\nMensagem criptografada: {criptografada}")