import re as reg_expresion

'''
--------------------FORMATADOR DE VETORES COM NOME E SOBRENOME--------------------
'''
def name_lastname_data():
         user_name_lastname = input("Digite nome e sobrenome: ")
         array_name = user_name_lastname.split(' ')
         uppercase_vector = []
         for  i in range(len(array_name)):
            uppercase_vector.append(array_name[i].title())        #--------->>> Pega a primeira letra de cada palavra e junta.
         
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
def  name_lastname_finder(name_list, keyword_search, lastname=False): 
          
          result = []
          for i, array in enumerate(name_list):
              if lastname:
                   if  keyword_search.lower() in array[1].lower():     #sobrenome
                        result.append(i)
              else:
                     if keyword_search in array[0]:                            #nome
                          result.append(i)
              
          if len(result) > 0 :
                return result
          else:
                return ''' Sem coincidências  com o termo de busca'''

'''
--------------------CADASTRAR USUARIO--------------------
'''
def user_registration(data_bank):
     user_data = name_lastname_data()   
     #format_user_data = user_data[0] +' '+ user_data[1]
     
     user_email = user_email_data() 

     data_bank.append(user_data)
     data_bank.append(user_email)

     return  data_bank


'''
--------------------BUSCAR USUARIO--------------------
'''
def  search_user(data_bank):
     op = input("Desejo fazer a busca por: \n1-Nome\n2-Sobrenome\n\nOpção: ")

     if keyword.isdigit() and keyword == '1':
          finded_users = []
          search = str(input('Digite o nome do usuário que deseja procurar:')).strip().lower()
          finded_users = name_lastname_finder(data_bank, search)
     
     elif keyword.isdigit() and keyword == '2':
        
         search = str(input('Digite o sobrenome do usuário que deseja procurar:')).strip().lower()
         finded_users = name_lastname_finder(data_bank, search, True)
     else:
          print('ERRO! Digite uma opção válida.')
        
     for i, dataset in enumerate(data_bank):
          for num in enumerate(finded_users): 
               if num == i :
                    print('\n--- Dados do Usuário ---')
                    print(f"Nome completo: {dataset[0]}")
                    print(f'E-mail: {dataset[1]}')
                    return dataset
               else:
                    print('Dados de usuario não encontrados') 

     
databank = []
user_reg_data = user_registration(databank) 
print(databank)
search_user(user_reg_data)
