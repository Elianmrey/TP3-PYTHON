import random
import re as  regex

fruits = ["maçã", "banana", "morango", "abacaxi", "uva", "pêssego", "laranja", "limão", "melancia", "manga"]
cars = ["toyota", "honda", "ford", "chevrolet", "volkswagen", "mercedes-benz", "bmw", "audi", "tesla", "ferrari"]
things = ["computador", "telefone", "mesa", "cadeira", "caneta", "livro", "relógio", "óculos", "copo", "chave"]
animals = ["cachorro", "gato", "elefante", "leão", "girafa", "tigre", "zebra", "panda", "pinguim", "gorila"]
colors = ["vermelho", "azul", "verde", "amarelo", "roxo", "laranja", "preto", "branco", "cinza", "marrom"]
countries = ["brasil", "estados unidos", "frança", "japão", "china", "índia", "rússia", "alemanha", "canadá", "austrália"]


vector_list = [fruits,cars,animals,colors, countries]

def word_vectorizer(vector_list):
          random_num = random.randint
          random_word = random.choice(vector_list[random_num(0, len(vector_list)-1)])
          vectorized_word = []
          for i in range(len(random_word)):
                vectorized_word += (random_word[i])
          return vectorized_word

def hanged(hidden_word, guess_word, sugested_letter):
     have_letter = False
     for i in range(len(hidden_word)):
           if sugested_letter == hidden_word[i]:
               have_letter = True
               guess_word[i] = sugested_letter
     return guess_word, have_letter

def list_is_full(guess_word):
   if "_" not in guess_word:
        return False
   else:
     return True

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
---------------------------------
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
---------------------------------
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
---------------------------------
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
---------------------------------
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
---------------------------------
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
---------------------------------
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
---------------------------------
''')

"""Esta função valida que o carater seja uma letra. Se sim, retorna True; caso contrário, False."""
def is_letter(letter):
     pattern = r'^[a-zA-Z]+$'
     if not (regex.match(pattern, letter)):
           print("Carater invalido")
           return False
     return True

"""Esta função verifica se o usuário digitou uma letra repetida. Se sim, retorna True; caso contrário, False."""
def char_repeat_control(list_char,letter):
      if letter in list_char:
         return list_char,True
      else:
         list_char.append(letter)
         return list_char,False

'''----------------------------- FUNÇÂO MAIN ----------------------------------------'''
def main(letter_list):
     print("Seja benvindo ao jogo  da forca!")
     hidden = word_vectorizer(vector_list)
     guess_word = ["_"] * len(hidden)
     repeated_char = []
     errors = 0

     while True:
          guess_format_word = ' '.join(guess_word)
          hidden_format_word  = ' '.join(hidden)
          
          print(guess_format_word)
          if(not letter_list):
               letter = input("\nDigite uma letra: ").strip().lower()
          else:
               letter =  letter_list.pop(0)  

          guess_word, have_letter  = hanged(hidden,guess_word , letter)
          
          if errors == 6:
               print("Você perdeu")
               print("A palavra era",' '.join(hidden))
               break
               
          if is_letter(letter):
                    repeated_char,is_repeated = char_repeat_control(repeated_char,letter)
                    if(not is_repeated):
                          if (have_letter):
                              print(f"A letra '{letter}' existe na palavra. Voce acertou")
                              #print(guess_format_word)
                              if (list_is_full ==True):
                                   print("Parabens você venceu!!")
                                   print("A palavra era ", hidden_format_word)
                                   break
                              else:
                                   continue
                          else:
                                   errors += 1
                                   hanged_design(errors)
                    else:
                         print("Essa letra ja foi indicada anteriormente.")

'''=============================TESTES========================='''

if __name__==  '__main__':
    chars = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m']
    for i in range(5):
          main(random.sample(chars, len(chars)))

if __name__==  '__main__':
     main(None)