import re as reg_expresion

'''
--------------------FORMATADOR DE VETORES COM NOME E SOBRENOME--------------------
'''

def name_lastname_data():
         user_name_lastname = input("Digite nome e sobrenome: ")
         array_name = user_name_lastname.split(' ')
         
         if len(array_name)>1 :  
              first_name = array_name[0]
              last_name = ' '.join([i for i in array_name[1:]])
              array_name.clear()
              array_name.insert(0,first_name)
              array_name.insert(1, last_name)

         uppercase_vector = []
         for  i in range(len(array_name)):
            uppercase_vector.append(array_name[i].title())        
         
         return uppercase_vector

'''
--------------------VALIDAÇÃO DE EMAIL--------------------
'''
def email_valido(email):
      regex = r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$'
      if reg_expresion.match(regex, email):
          return True
      else:
            return False
'''
--------------------CONTROLE DE EMAIL--------------------
'''
def user_email_data():      
      email = input('Digite seu email: ')
      while not email_valido(email):
         print( '\nE-mail invalido\n')
         print( '1 - Tentar novamente\n0 - Cancelar\n')   
         us_select = input("\nDigite a opção escolhida: ")
                
         if us_select ==  '1':
            email_user =  user_email_data()
            return  email_user
         elif us_select == '0':
              break  
         else: 
             print('Opção inválida! Digite uma das opções disponíveis.')

      return email

'''
--------------------BUSCADOR DE INDICE DE NOME OU SOBRENOME--------------------
'''
def name_lastname_index_finder(name_list, keyword_search, lastname=False):
    result = []
    for i, user_info in enumerate(name_list):
        if lastname:
            if keyword_search.lower() in user_info[1].lower(): #Procurando o indice de sobrenome
                result.append(i)
        else:
            if keyword_search.lower() in user_info[0].lower(): # Procurando o indice de nome
                result.append(i)
    if len(result) > 0:
        return result
    else:
        return None
        

'''
--------------------CADASTRAR USUARIO--------------------
'''
def user_registration(data_bank):
     
     user_data = name_lastname_data()   
     user_email = user_email_data()
     user_info = user_data + [user_email]
     data_bank.append(user_info)
       
     return  data_bank

'''
--------------------BUSCAR USUARIO--------------------
'''
def  search_user(data_bank):
     opcao = input("Desejo fazer a busca por: \n1-Nome\n2-Sobrenome\n\nOpção: ")
     finded_users = []
     if opcao.isdigit() and opcao == '1':
          
          search = str(input('Digite o nome do usuário que deseja procurar:')).strip().lower()
          finded_users = name_lastname_index_finder(data_bank, search)
          print(finded_users)
     
     elif opcao.isdigit() and opcao == '2':
        
         search = str(input('Digite o sobrenome do usuário que deseja procurar:')).strip().lower()
         finded_users = name_lastname_index_finder(data_bank, search, True)
         
        
                         
     else:
          print('ERRO! Digite uma opção válida.')
     if not None in finded_users:      
        for index in finded_users:
          
                print('\n--- Dados do Usuário ---')
                print(f"Nome completo:", data_bank[index][0] + ' ' + data_bank[index][1])
                print(f'E-mail: {data_bank[index][2]}')
     else:
                print('O usuário não foi encontrado na base de dados.')

databank = []    
databank = user_registration(databank) 


search_user(databank)



