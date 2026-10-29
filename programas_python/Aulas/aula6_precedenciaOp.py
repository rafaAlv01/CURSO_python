# 1. (n+n) -> dentro de parênteses
# 2. **
# 3. * / // %
# 4. + -
# 5. = += -= *= /= //= **= %=

conta_1 = 10 + 3 * 2  # Multiplicação antes da soma
conta_2 = (10 + 3) * 2  # Parênteses
conta_3 = 10 ** 2 + 3 * 2 - 8 / 4 // 2  # Ordem de precedência
print('Conta 1:', conta_1)  # Saída: 16
print('Conta 2:', conta_2)  # Saída: 26
print('Conta 3:', conta_3)  # Saída: 109.0