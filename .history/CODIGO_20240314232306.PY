import re as reg_expresion


def nome_e_sobrenome(arrayNome):
         iniciais_maiusculo = ''
         for  i in range(len(arrayNome)):
            iniciais_maiusculo +=  arrayNome[i][0].upper()        #--------->>> Pega a primeira letra de cada palavra e junta.
         return iniciais_maiusculo


def email_valido(email):
      regex = r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$'
      if reg_expresion.match(regex, email):
          return True
      else:
            return False
'''
---------------CONTROLE DE EMAIL------------
'''
def controle_email(email):      
        if email_valido(email):
            return email
        else:
            while True:
                print( '1 - Tentar novamente\n0 - Cancelar\n')   
                us_select = input("\nDigite a opção escolhida: ")
                if us_select ==  '1':
                     user_xeset = input("Digite o email novamente: "
                     if controle_email(email_write)):
                          
                elif us_select == '0':
                     break  
                else: 
                     print('Opção inválida! Digite uma das opções disponíveis.')


print(nome_e_sobrenome(["Elian", "Montes"]))

print(controle_email("elian1245@gmail.com"))