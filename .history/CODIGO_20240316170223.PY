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
--------------------MOSTRAR USUARIO--------------------
'''

#def show_user_info(array_user):



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
          
     for i in range(len(data_bank)):
           print('\n--- Dados do Usuário ---')
           print(f"Nome completo:",data_bank[finded_users[i]][0] + ' ' + data_bank[finded_users[i]][1])
           print(f'E-mail: {data_bank[finded_users[i]][2]}')
                 

databank = []    
databank = user_registration(databank) 

print(databank)
search_user(databank)



import random

fruits = ["Maçã", "Banana", "Morango", "Abacaxi", "Uva", "Pêssego", "Laranja", "Limão", "Melancia", "Manga"]
cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen", "Mercedes-Benz", "BMW", "Audi", "Tesla", "Ferrari"]
things = ["Computador", "Telefone", "Mesa", "Cadeira", "Caneta", "Livro", "Relógio", "Óculos", "Copo", "Chave"]
animals = ["Cachorro", "Gato", "Elefante", "Leão", "Girafa", "Tigre", "Zebra", "Panda", "Pinguim", "Gorila"]
colors = ["Vermelho", "Azul", "Verde", "Amarelo", "Roxo", "Laranja", "Preto", "Branco", "Cinza", "Marrom"]
countries = ["Brasil", "Estados Unidos", "França", "Japão", "China", "Índia", "Rússia", "Alemanha", "Canadá", "Austrália"]

object_list = [fruits,cars,animals,colors, countries]

def word_vectorizer(object_list):
          def word_randomizer(object_list):
               random_num = random.randint
               random_list = random.choice(object_list[random_num(0, len(object_list)-1)])
               random_word = random.choice(random_list)
               return random_word
          
          vectorized_word =  (word_randomizer(object_list)).split('')
          return vectorized_word

def forca(hidden_word, guess_word, sugested_letter):
     have_letter = False
     if ''.join(hidden_word) == ''.join(guess_word):
            have_letter = True
            return guess_word, True
     
     else:
          for i, letter in  enumerate(hidden_word):
                if letter == sugested_letter:
                   have_letter = True
                   guess_word[i] = sugested_letter
                   return  guess_word, have_letter 
                else:
                     return guess_word, have_letter
guess_word=[]
word, booleano  = forca(["c","a","s","a"],guess_word , "a")                
print("Letras já adivinhadas: ", ' '.join(word))
if booleano : print("\nParabéns você acertou!")
else:         print("\nErrou!