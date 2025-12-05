def gerar_sequencia_media(peso_0, peso_1):
    N = 11
    a = 2   # Condições iniciais
    b = 3   # da sequência são fixas
    """
    Gera uma sequência onde cada elemento é a média ponderada dos dois antecessores.
    Args:
        peso_0 (float/int): peso do elemento y(k)
        peso_1 (float/int): peso do elemento y(k+1)
    """
    # Inicializa a sequência com os dois primeiros elementos.
    sequencia = [a,b]
    # Gera os elementos restantes.
    for i in range(2, N):
        # O novo elemento é a média ponderada dos dois antecessores imediatos.
        # Os antecessores são sequencia[i-2] e sequencia[i-1].
        proximo_elemento = peso_0*sequencia[i-2] + peso_1*sequencia[i-1]
        sequencia.append(proximo_elemento)
    print(f"peso_0 = {peso_0}, peso_1 = {peso_1} | Nº de elementos: {N}")
    print(f"{sequencia}\n")
    return sequencia

# --- Testes ---
gerar_sequencia_media(0.5,0.5)      # peso_0 = 0.5 ; peso_1 = 0.5
gerar_sequencia_media(0.25,0.75)    # peso_0 = 0.25 ; peso_1 = 0.75
gerar_sequencia_media(0.75,0.25)    # peso_0 = 0.75 ; peso_1 = 0.25
gerar_sequencia_media(0.1,0.9)      # peso_0 = 0.1 ; peso_1 = 0.9
gerar_sequencia_media(0.9,0.1)      # peso_0 = 0.9 ; peso_1 = 0.1
gerar_sequencia_media(0,1)          # peso_0 = 0 ; peso_1 = 1
gerar_sequencia_media(1,0)          # peso_0 = 1 ; peso_1 = 0

