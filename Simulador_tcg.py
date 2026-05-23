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

# Funções essenciais para o desenvolvimento da luta
## Função de ataque, que recebe os dados dos inputs e mostra o resultado do ataque, além de calcular o hp restante do defensor  
def Atacar(nome_atacante, nome_defensor, Ataque, hp):
  ''' Função que recebe diretamente os dados dos inputs e mostra ao usuário quem ataca e quanto de dano irá causar, além de calcular o hp que resta'''
  hp_defensor = hp - Ataque

  if hp_defensor <= 0:
    hp_defensor = 0
  print(f"\n{nome_atacante} atingiu {nome_defensor} e causou {Ataque} pontos de dano!")
  return hp_defensor

### Função que exibe o placar a cada turno com o hp atualizado dos monstros
def exibir_placar(Monstro_1, Monstro_2, hp_1, hp_2):
  ''' Função que recebe os dados de hp atualizados e exibe como está '''
  print("\n Fim do turno, aqui estão os resultados de ataque")
  print(f"{Nome_monstro} possui {hp_1} pontos de vida")
  print(f"{Nome_monstro_2} possui {hp_2} pontos de vida restantes")
  return