def gerar_sequencia_media(a, b):
    N = 10
    """
    Gera uma sequência onde cada elemento é a média dos dois antecessores.
    Args:
        a (float/int): O primeiro elemento da sequência.
        b (float/int): O segundo elemento da sequência.
    """
    # Inicializa a sequência com os dois primeiros elementos.
    sequencia = [a,b]
    # Gera os elementos restantes.
    for i in range(2, N):
        # O novo elemento é a média dos dois antecessores imediatos.
        # Os antecessores são sequencia[i-2] e sequencia[i-1].
        proximo_elemento = (sequencia[i-2] + sequencia[i-1]) / 2
        sequencia.append(proximo_elemento)
    print(f"a = {a}, b = {b} | Nº de elementos: {N}")
    print(f"{sequencia}\n")
    return sequencia

# --- Testes ---
gerar_sequencia_media(2,3) # a = 2 ; b = 3
gerar_sequencia_media(3,2) # a = 3 ; b = 2
gerar_sequencia_media(0,5) # a = 0 ; b = 5
gerar_sequencia_media(5,0) # a = 5 ; b = 0
gerar_sequencia_media(1,1) # a = 1 ; b = 1
gerar_sequencia_media(2,2) # a = 2 ; b = 2