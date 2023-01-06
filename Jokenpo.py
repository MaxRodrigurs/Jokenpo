from time import sleep
from random import choice
import emoji

pc_count=0
player_count=0

while True:
    print('\n{:=^40}'.format(' JOKENPO '))
    print('{:-^40}'.format(f' PC: {pc_count} X Jogador: {player_count} '))
    print("\n\tPedra | Papel | Tesoura\n")
    
    pc = ['Papel', 'Pedra', 'Tesoura']
    escolha_pc= choice(pc)
    
    segunda_p = str(input('\tEscolha com sabedoria:\n ').upper().split())
    segunda_p= segunda_p[4]

    if not segunda_p == 'D' and not segunda_p == 'P' and not segunda_p == 'S':
      print('\n\tOPA! ESCOLHA NÂO RECONHECIDA! \nTente novamente.')
      exit = str(input('Acha melhor deixar para outra hora? Digite "Sim". \nSenão, digite "Continuar"\n').upper().split())
      exit=exit[2]
      
      if exit == 'S': 
        break
      elif exit == 'C':
        continue 
      else:
        break
    
    else:
      print('\n\t1')
      sleep(1)
      print('\t2')
      sleep(1)
      print('\t3!\n')
    
    pedra= emoji.emojize(':punch:', language='alias')
    papel= emoji.emojize(':paper:', language='alias')
    tesoura= emoji.emojize(':tesoura:', language='alias')

    if escolha_pc == 'Pedra':
        print(f'PC: {pedra}')
    elif escolha_pc == 'Papel':
        print(f'PC: {papel}')
    else:
        print(f'PC: {tesoura}')

    if segunda_p == 'D':
        print(f'Sua escolha: {pedra}')
    elif segunda_p == 'P':
        print(f'Sua escolha: {papel}')
    elif segunda_p == 'S':
        print(f'Sua escolha: {tesoura}')

    if escolha_pc == 'Pedra' and segunda_p == 'P':
        player_count += 1

    elif escolha_pc == 'Pedra' and segunda_p == 'S':        
        pc_count += 1

    elif escolha_pc == 'Pedra' and segunda_p == 'D':
        print('\tEmpate')

    elif escolha_pc == 'Papel' and segunda_p == 'D':
        pc_count += 1
            
    elif escolha_pc == 'Papel' and segunda_p == 'S':
        player_count += 1
            
    elif escolha_pc == 'Papel' and segunda_p == 'P':
        print('\tEmpate')

    elif escolha_pc == 'Tesoura' and segunda_p == 'P':
        pc_count += 1
            
    elif escolha_pc == 'Tesoura' and segunda_p == 'D':
        player_count += 1

    elif escolha_pc == 'Tesoura' and segunda_p == 'S':
        print('\tEmpate')