mensagem = input().strip()
crib = input().strip()

tamanho_mensagem = len(mensagem)
tamanho_crib = len(crib)

posicoes_validas = 0

for i in range(tamanho_mensagem - tamanho_crib + 1):
    
    possivel = True
    
    for j in range(tamanho_crib):
        if mensagem[i + j] == crib[j]:
            possivel = False
            break
    
    if possivel:
        posicoes_validas += 1

print(posicoes_validas)