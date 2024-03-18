import random
import re as  regex

fruits = ["maçã", "banana", "morango", "abacaxi", "uva", "pêssego", "laranja", "limão", "melancia", "manga"]
cars = ["toyota", "honda", "ford", "chevrolet", "volkswagen", "mercedesbenz", "bmw", "audi", "tesla", "ferrari"]
things = ["computador", "telefone", "mesa", "cadeira", "caneta", "livro", "relógio", "óculos", "copo", "chave"]
animals = ["cachorro", "gato", "elefante", "leão", "girafa", "tigre", "zebra", "panda", "pinguim", "gorila"]
colors = ["vermelho", "azul", "verde", "amarelo", "roxo", "laranja", "preto", "branco", "cinza", "marrom"]
countries = ["brasil", "espanha", "frança", "japão", "china", "índia", "rússia", "alemanha", "canadá", "austrália"]

'''======================BD PALAVRAS======================'''

vector_list = [fruits,cars,animals,colors, countries]

'''======================ESTA FUNÇÃO VETORIZA A PALAVRA ESCOLIDA======================'''

def word_vectorizer(vector_list):
          random_num = random.randint
          random_word = random.choice(vector_list[random_num(0, len(vector_list)-1)])
          vectorized_word = []
          for i in range(len(random_word)):
                vectorized_word += (random_word[i])
          return vectorized_word


'''======================ESTA FUNÇÃO VERIFICA SE A LETRA ESTA NA PALAVRA======================'''

def hanged(hidden_word, guess_word, sugested_letter):
     have_letter = False
     for i in range(len(hidden_word)):
           if sugested_letter == hidden_word[i]:
               have_letter = True
               guess_word[i] = sugested_letter
     return guess_word, have_letter

'''======================ESTA FUNÇÃO VERIFICA SE A LISTA DE LETRAS DA PALAVRA ADIVINHADA ESTA CHEIA======================'''

def list_is_full(guess_word):
  #for i in range(len(guess_word)):
     if "_" in guess_word:
          return False 
 
     return True
     
   
'''======================ESTA FUNÇÃO DESENHA O ENFORCADO======================'''

def hanged_design(errors):
     characters = ["0", "/", "|", "\\", "/", " \\"]
     if errors == 0:
          print(f'''
___________________________________________
|             |       
|             
|           
|             
|             
|            
|
___________________________________________
''')
     elif errors == 1:
          print(f'''
___________________________________________
|             |       
|             {characters[0]}
|            
|             
|             
|           
|
___________________________________________
''')
     elif errors == 2:
          print(f'''
___________________________________________
|             |       
|             {characters[0]}
|            {characters[1]}
|                 
|             
|            
|
___________________________________________
''')

     if errors == 3:
          print(f'''
___________________________________________
|             |       
|             {characters[0]}
|            {characters[1]}{characters[2]}
|             {characters[2]}    
|             {characters[2]}
|           
|
___________________________________________
''')
     
     elif errors == 4:
          print(f'''
___________________________________________
|             |       
|             {characters[0]}
|            {characters[1]}{characters[2]}{characters[3]}
|             {characters[2]}    
|             {characters[2]}
|            
|
___________________________________________
''')
     elif errors == 5:
          print(f'''
___________________________________________
|             |       
|             {characters[0]}
|            {characters[1]}{characters[2]}{characters[3]}
|             {characters[2]}    
|             {characters[2]}
|            {characters[4]}
|
___________________________________________
''')
     elif errors == 6:
          print(f'''
___________________________________________
|             |       
|             {characters[0]}
|            {characters[1]}{characters[2]}{characters[3]}
|             {characters[2]}    
|             {characters[2]}
|            {characters[4]}{characters[5]}
|
___________________________________________
''')

'''======================ESTA FUNÇÃO VALIDA QUE O CARACTER SEJA ALFABÉTICO.
    SE SIM, RETORNA TRUE; CASO CONTRÁRIO, FALSE.======================'''

def is_letter(letter):
     pattern = r'^[a-zA-ZáâãéêíóõôúûçÁÂÃÉÊÍÓÕÔÚÛ]+$'
     if not (regex.match(pattern, letter)):
           print("Carater invalido")
           return False
     return True

'''======================ESTA FUNÇÃO VERIFICA SE O USUÁRIO DIGITOU UMA LETRA REPETIDA.
    SE SIM, RETORNA TRUE; CASO CONTRÁRIO, FALSE.======================'''

def char_repeat_control(list_char,letter):
      if letter in list_char:
         return list_char,True
      else:
         list_char.append(letter)
         return list_char,False
def should_continue()
'''====================== FUNÇÂO MAIN ======================'''

def main(letter_list):
     print("\n\nSeja benvindo ao jogo  da forca!\n")
     hidden = word_vectorizer(vector_list)
     guess_word = ["_"] * len(hidden)
     repeated_char = []
     errors = 0
     lifes = 6
     print('Vidas: ', lifes )
     while True:
          guess_format_word = ' '.join(guess_word)
          hidden_format_word  = ' '.join(hidden)
          
          print(guess_format_word)
          if(not letter_list):
               letter = input("\nDigite uma letra: ").strip().lower()
          else:
               letter =  letter_list.pop(0)  

          guess_word, have_letter  = hanged(hidden,guess_word , letter)
          
          if errors == 5:
               hanged_design(6)
               lifes = 0
               print('Vidas: ', lifes )
               print("Você perdeu")
               
               print("A palavra era",' '.join(hidden))
               break
               
          if is_letter(letter):
                    repeated_char,is_repeated = char_repeat_control(repeated_char,letter)
                    if(not is_repeated):
                          if (have_letter):
                              print(f"A letra '{letter}' existe nessa palavra. Voce acertou")
                              if (list_is_full(guess_word)):
                                   print("Parabens você venceu!!")
                                   print("A palavra era ", hidden_format_word)
                                   break
                                                               
                          else:
                                   print(f"A letra '{letter}' não existe nessa palavra.")
                                   errors += 1
                                   lifes -= 1
                                   hanged_design(errors)
                                   print('Vidas: ', lifes)
                    else:
                         print("Essa letra ja foi indicada anteriormente.")



'''=============================TESTES========================='''

if __name__==  '__main__':
    chars = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m','á','â','ã','é','ê','í','ó','õ','ô','ú','û']
    for i in range(5):
          print(f'''\n\n\t\t\t\t\t {i+1} Rodada automatica''')
          main(random.sample(chars, len(chars)))


'''=============================EXECUÇÃO========================='''

if __name__==  '__main__':
    while True:
          main(None)