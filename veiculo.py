# Entrada de dados
rodas = int(input("Informe a quantidade de rodas do veículo: "))
peso = int(input("Informe o peso bruto do veículo (em kg): "))
pessoas = int(input("Informe a capacidade de pessoas do veículo: "))

# Lógica para determinar a categoria
if rodas == 2 or rodas == 3:
  categoria = "A"
elif rodas >= 4 and peso <= 3500 and pessoas <=8:
  categoria = "B"
elif rodas >= 4 and peso >= 3500 and peso <= 6000:
  categoria = "C"
elif rodas >= 4 and pessoas > 8:
  categoria = "D"
elif rodas >= 4 and peso > 6000:
  categoria = "E"

# Exibir resultado
print("Categoria da habilitação necessária:", categoria)