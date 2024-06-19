# Patrícia Lima Massolini RA: 1136999
import os, time
import sys
os.system("cls")
erros = 0
def jogar():
 def desenhoForca(erros):
      if erros == 0:
        print("  _____ ")
        print(" |     |")
        print("       |")
        print("       |")
        print("       |")
        print("       |")
      elif erros == 1:
        print("  _____ ")
        print(" |     |")
        print(" O     |")
        print("       |")
        print("       |")
        print("       |")
        print(" ______|_")
      elif erros == 2:
        print("  _____ ")
        print(" |     |")
        print(" O     |")
        print(" |     |")
        print("       |")
        print("       |")
        print(" ______|_")
      elif erros == 3:
        print("  _____ ")
        print(" |     |")
        print(" O     |")
        print("/|     |")
        print("       |")
        print("       |")
        print(" ______|_")
      elif erros == 4:
        print("  _____ ")
        print(" |     |")
        print(" O     |")
        print("/|\    |")
        print("       |")
        print("       |")
        print(" ______|_")
      elif erros == 5:
        print("  _____ ")
        print(" |     |")
        print(" O     |")
        print("/|\    |")
        print("/      |")
        print("       |")
        print(" ______|_")
      elif erros == 6:
        print("  _____ ")
        print(" |     |")
        print(" O     |")
        print("/|\    |")
        print("/ \    |")
        print("       |")
        print(" ______|_")

 print('''
      
     __   __   _  _                 __   __   __           __
    |__) |__   |\/| __ \  / | |\ | |  \ /  \ /__`     /\  /  \ 
    |__) |___  |  |     \/  | | \| |__/ \__/ .__/    /~~\ \__/ 
                                                            
       _                         _         ______                  _ 
      | |                       | |       |  ____|                | |
      | | ___   __ _  ___     __| | __ _  | |__ ___  _ __ ___ __ _| |
  _   | |/ _ \ / _` |/ _ \   / _` |/ _` | |  __/ _ \| '__/ __/ _` | |
 | |__| | (_) | (_| | (_) | | (_| | (_| | | | | (_) | | | (_| (_| |_|
  \____/ \___/ \__, |\___/   \__,_|\__,_| |_|  \___/|_|  \___\__,_(_)
                __/ |                                                
               |___/                                                  
                                                                     ''')


 time.sleep(3)
 resultado = ''
 def numeroPalavraChave(resultado,palavraChave):
   for k in palavraChave:
        if k != ' ':
                resultado +='*'
        else:
                resultado += ' '
   print("O número de letras da Palavra Chave é : ", resultado)
 os.system("cls")
 desafiante = input("Digite o nome do Desafiante: ")
 competidor = input("Digite o nome do Competidor: ")
 time.sleep(1)
 os.system("cls")
 print("Desafiante, forneça as seguintes informações: ")
 palavraChave = input("Informe a Palavra Chave: ").lower()
 dicas = [input("Informe a Dica 1: "), input("Informe a Dica 2: "), input("Informe a Dica 3: ") ]
 palavraOculta = ''
 letrasDoUsuario = []
 letrasCorretas = []
 maxErros = int(6)
 os.system("cls")
 numeroPalavraChave(resultado, palavraChave)
 print("\n #### AVISOS ####\n  Você pode usar as dicas apenas 3 vezes!!! \n O espaço está sendo considerado uma letra também.\n Você só pode errar 6 vezes ####### ") 
 


 def competidorGanha(letrasCorretas, palavraChave) :
      if len(letrasCorretas)  == len(palavraChave):
            return f"O Competidor '{competidor}' Ganhou!" 
      
 
 def acertou(letrasCorretas, palavraChave, letraDoUsuario):
       if letraDoUsuario in palavraChave:
              letrasCorretas.append(letraDoUsuario)
  
      

 def elementoRepetido(letrasDoUsuario, letraDoUsuario):
       while True:
        if letraDoUsuario not in letrasDoUsuario:
              return letrasDoUsuario.append(letraDoUsuario)
              
        else:
              print("Você já tentou essa letra, tente outra :( ")
              letraDoUsuario = input("Digite uma letra que você acha que a Palavra Chave contém: ")
              acertou(letrasCorretas, palavraChave, letraDoUsuario)
              print(f" Erro {erros}")
              breakpoint 
               

                
 def erro(palavraChave, letraDoUsuario):
       global erros
       if letraDoUsuario not in palavraChave:
                 erros += 1 
                 print(f"Erro:{erros}" )
       elif letraDoUsuario in palavraChave and letraDoUsuario not in letrasCorretas:
                  print("Você acertou")   

 def menufinal(letrasCorretas, palavraChave):
  global erros
  while  set(letrasCorretas) == set(palavraChave) or int(erros)>= maxErros:
        print("Pressione (j) para jogar novamente")
        print("Pressione (s) para sair do jogo")
        opcao1 = input("")
        if   opcao1 == "j":
             os.system("cls")
             print("Reiniciando o Game ....")
             time.sleep(3)
             erros = 0
             letrasDoUsuario = []
             letrasCorretas = []
             jogar()
        elif opcao1 == "s":
             sys.exit(0)
        
        
             
 
 dicaAtual = 0
 letrasCorretas = []
###################################################################################

 

 while int(erros) < maxErros :
        print(" \n (0) para Jogar")
        print(" \n (1) para Solicitar Dica ")
        opcao = input(" ")
        os.system("cls")


        if opcao == "0":
               while True:
                     letraDoUsuario = input("Digite uma letra que você acha que a Palavra Chave contém: ")
                     if letraDoUsuario and len(letraDoUsuario) == 1:
                            break
                     else:
                            print("Por favor, digite apenas uma letra ou apenas um número.")
               desenhoForca(erros)
               elementoRepetido(letrasDoUsuario,letraDoUsuario)
               erro(palavraChave, letraDoUsuario)
               print(f"Competidor, você já tentou as letras/números {letrasDoUsuario}")
               acertou(letrasCorretas, palavraChave, letraDoUsuario)
               competidorGanha(letrasCorretas, palavraChave)

               if letraDoUsuario in palavraChave and letraDoUsuario not in letrasCorretas:
                  letrasCorretas.append(letraDoUsuario)


              
               
               
               for letraDoUsuario in palavraChave.lower():
                if letraDoUsuario.lower() in letrasDoUsuario:
                       print(letraDoUsuario, end = " ")
                else:
                       print("*", end = " ")





                if set(letrasCorretas) == set(palavraChave):
                    print(f"\n\n\nParabéns! Você acertou a palavra! \n O Competidor '{competidor}' Ganhou o jogo!")
                    print(f"A palavra era {''.join(palavraChave.lower())}")
                    menufinal(letrasCorretas, palavraChave)
                    

########################################################################################
        elif opcao == "1":
               if dicaAtual < len(dicas):
                     print(f"Dica: {dicas[dicaAtual]}")
                     dicaAtual += 1
               else: 
                     print("Você já usou todas as dicas!")

               while True:
                     letraDoUsuario = input("Digite uma letra que você acha que a Palavra Chave contém: ")
                     if letraDoUsuario and len(letraDoUsuario) == 1:
                            break
                     else:
                            print("Por favor, digite apenas uma letra ou apenas um número.")
               desenhoForca(erros)
               elementoRepetido(letrasDoUsuario,letraDoUsuario)   
               erro(palavraChave, letraDoUsuario)
               print(f"Competidor, você já tentou as letras {letrasDoUsuario}")
               acertou(letrasCorretas, palavraChave, letraDoUsuario)
               competidorGanha(letrasCorretas, palavraChave)


               if letraDoUsuario in palavraChave and letraDoUsuario not in letrasCorretas:
                   letrasCorretas.append(letraDoUsuario)



               for letraDoUsuario in palavraChave:
                if letraDoUsuario in letrasDoUsuario:
                       print(letraDoUsuario, end = " ")
                else:
                       print("*", end = " ") 
        
                if set(letrasCorretas) == set(palavraChave):
                    print(f"\n Parabéns! Você acertou a palavra! \n O Competidor '{competidor}' ganhou o jogo!")
                    print("Total de erros:", erros)
                    menufinal(letrasCorretas, palavraChave)

                        
                            
                               
 if int(erros) >= maxErros:
        print("\n _____ ")
        print(" |     |")
        print(" O     |")
        print("/|\    |")
        print("/ \    |")
        print("       |")
        print(" ______|_")
        print(f"\nAcabaram suas chances :( . O Desafiante '{desafiante}' ganhou o jogo!")
        print("Total de erros:", erros)
        print(f"A palavra era: {''.join(palavraChave)}")
        menufinal(letrasCorretas, palavraChave)
############################################################################################

while True:
        print("Pressione (i) para iniciar o jogo")
        print("Pressione (s) para sair do jogo")
        opcaoFinal = input("")
        if opcaoFinal == "i":
            jogar()
        elif opcaoFinal == "s":
            sys.exit(0) 
        else:
           print("Opção inválida! Por favor, escolha 'i' para iniciar ou 's' para sair.")
           continue
        