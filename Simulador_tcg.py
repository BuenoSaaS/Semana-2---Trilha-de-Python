# Inputs que coletarão dados para desenvolver a luta

while True:
  try:

    Nome_monstro = input("Insira o nome do primeiro monstro ")
    HP = int(input("Quantos pontos de vida possui a criatura? "))
    Ataque = int(input("Por fim, qual o dano causado pelo seus ataques? "))
    Nome_monstro_2 = input("Insira o nome do segundo monstro ")
    HP_2 = int(input("Quantos pontos de vida possui a segunda criatura? "))
    Ataque_2 = int(input("Quanto dano essa carta causa? "))

# Verificador de dados para evitar que monstros possuam números no nome ou que sejam enviados dados de ataque e vida negativos ou iguais a 0 
## Interrompendo o código em caso positivo e e pedindo para inserir novamente
    if Nome_monstro.isalpha() and Nome_monstro_2.isalpha() and HP_2 > 0  and HP > 0  and Ataque > 0 and Ataque_2 > 0:
      break
    else:
      print("Insira apenas letras no nome e não são aceitos valores negativos ou iguais a 0, monstro morto ou sem ataque não batalha")
      continue
  except ValueError:
    print("Insira valores numéricos para os pontos de vida e ataque, reproduza novamente o programa")
    break