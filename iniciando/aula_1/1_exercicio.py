# Exercicio de Aplicação

# Constante de Bonus

constante_bonus = 1000

# Solicitar ao usuário que digite o nome:

usuario = input("Digite seu Nome mane: ")

# Solicitar o valor dde salario do mesmo, converter para Float

valor_salario = float(input("Coloca ai seu salario mane: "))

# Solitar o valor do Bonus recebido

valor_bonus = float(input("Coloca ai seu bonus fio: "))

# Valor do bonus final

valor_final = float(constante_bonus + valor_salario * valor_bonus)

# Inprima para o user texto com variaveis

print(f"O cabra {usuario}, possui o salario de {valor_salario} e tem o bonus de {valor_bonus}. Ficou com o valor final de {valor_final}")