import re as reg_expresion

'''
--------------------FORMATADOR DE VETORES COM NOME E SOBRENOME--------------------
'''
def name_lastname_data():
         user_name_lastname = input("Digite nome e sobrenome: ")
         array_name = user_name_lastname.split(' ')
         '''Usuario tem nome e 2 sobrenomes, a validação abaixo verifica se o usuario escreveu 
           mais de um sobrenome e se certifica que o vetor seja de 2 posições ('Nome' , 'Sobrenome') '''
         if len(array_name)>1 :  
              first_name = array_name[0]
              last_name = ' '.join([i for i in array_name[1:]])
              array_name.clear()
              array_name.insert(0,first_name)
              array_name.insert(1, last_name)

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
                   if  str(keyword_search) in str(array[1]) or str(keyword_search) == str(array[1]):     #sobrenome
                        result.append(i)
              else:
                     if  str(keyword_search) in str(array[0]) or str(keyword_search) == str(array[0]):                           #nome
                          result.append(i)
              
          if len(result) > 0 :
                return result
          else:
                return None

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
     opcao = input("Desejo fazer a busca por: \n1-Nome\n2-Sobrenome\n\nOpção: ")
     finded_users = []
     if opcao.isdigit() and opcao == '1':
          
          search = str(input('Digite o nome do usuário que deseja procurar:')).strip().lower()
          finded_users = name_lastname_finder(data_bank[0], search)
          print(finded_users)
     
     elif opcao.isdigit() and opcao == '2':
        
         search = str(input('Digite o sobrenome do usuário que deseja procurar:')).strip().lower()
         finded_users = name_lastname_finder(data_bank[0], search, True)
         print(finded_users)
         if not finded_users:
              print('\nO usuário não foi  encontrado!')
         else:
               show_user_info(finded_users)       
              
     else:
          print('ERRO! Digite uma opção válida.')
          
     for i, dataset in enumerate(data_bank[0]):
                 if finded_users(i) in dataset :
                    print('\n--- Dados do Usuário ---')
                    print(f"Nome completo: {dataset[0]}")
                    print(f'E-mail: {dataset[1]}')
                    return dataset
                 

databank = []    
databank = user_registration(databank) 

print(databank)
search_user(databank)
