import re as reg_expresion

'''
---------------GERADOR DE VETORES COM NOME E SOBRENOME------------
'''
def name_lastname():
         user_name_lastname = input("Digite nome e sobrenome: ")
         array_name = user_name_lastname.split(' ')
         uppercase_vector = []
         for  i in range(len(array_name)):
            uppercase_vector.append(array_name[i].title())        #--------->>> Pega a primeira letra de cada palavra e junta.
         
         return uppercase_vector

'''
---------------VALIDAÇÃO DE EMAIL------------
'''
def email_valido(email):
      regex = r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$'
      if reg_expresion.match(regex, email):
          return True
      else:
            return False
'''
---------------CONTROLE DE EMAIL------------
'''
def controle_email():      
      email = input('Digite seu email: ')
      while not email_valido(email):
         print( '\nE-mail invalido\n')
         print( '1 - Tentar novamente\n0 - Cancelar\n')   
         us_select = input("\nDigite a opção escolhida: ")
                
         if us_select ==  '1':
            email_user =  controle_email()
            return  email_user
         elif us_select == '0':
              break  
         else: 
             print('Opção inválida! Digite uma das opções disponíveis.')

      return email

'''
---------------BUSCADOR DE NOME OU SOBRENOME------------
'''
def  name_lastname_finder(name_list, keyword_search, lastname=False):
     for  x in name_list:
        ikeyword_search.lower()):