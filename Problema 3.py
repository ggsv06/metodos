import matplotlib.pyplot as plt
import numpy as np


E = 10000
a = 0.01
N = 10*12

print(f'\nE = {E}')
print(f'a = {a}')
print(f'N = {N}')

# Devemos calcular:
# * Valor total pago
# * Valor máximo da parcela
# * Comportamento da dívida


# -------------------------------------------
# Sistema de amortização constante (SAC)

# Montante
def m_sac(k):
    return E - E*k/N

# Parcela
def p_sac(k):
    return E/N*(1+a*(N-k))

# -------------------------------------------
# Sistema de parcelas fixas (Tabela Price)

# Parcela
p_price = (E*a*(1+a)**N)/((1+a)**N-1)

# Montante
def m_price(k):
    return E*(a+1)**k + (p_price/a)*(1-(a+1)**k)

# -------------------------------------------
# Cálculo do valor total pago
total_price = 0
total_sac = 0
max_sac = 0
for i in range(0, N+1):
    total_price+=p_price
    total_sac+=p_sac(i)
    if p_sac(i) > max_sac:
        max_sac = p_sac(i)
    else:
        continue
    
print(f'\nTotal price: {total_price}')
print(f'Total sac: {total_sac}')
print(f'\nParcela máxima price: {p_price}')
print(f'Parcela máxima sac: {max_sac}')

# -------------------------------------------
# Gerador de gráficos

k = np.linspace(0, N, N+1)

# Parcelas
psac = p_sac(k)
pprice_values = np.full_like(k, p_price)

fig, ax = plt.subplots()

ax.plot(k, psac, 'o-', linewidth=2, color='blue', label='SAC')
ax.plot(k, pprice_values, 'o-', linewidth=2, color='red', label='PRICE')

plt.title("Parcelamentos")
plt.xlabel("mês k")
plt.ylabel('valor em reais da parcela')
plt.grid(True)
plt.legend()
plt.show()

# Dívidas
msac = m_sac(k)
mprice = m_price(k)

fig, ax = plt.subplots()

ax.plot(k, msac, 'o-', linewidth=2, color='blue', label='SAC')
ax.plot(k, mprice, 'o-', linewidth=2, color='red', label='PRICE')

plt.title("Dívidas")
plt.xlabel('mês k')
plt.ylabel('valor em reais da dívida')
plt.grid(True)
plt.legend()
plt.show()










