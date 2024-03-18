import random
import re as  regex
fruits = ["Maçã", "Banana", "Morango", "Abacaxi", "Uva", "Pêssego", "Laranja", "Limão", "Melancia", "Manga"]
cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen", "Mercedes-Benz", "BMW", "Audi", "Tesla", "Ferrari"]
things = ["Computador", "Telefone", "Mesa", "Cadeira", "Caneta", "Livro", "Relógio", "Óculos", "Copo", "Chave"]
animals = ["Cachorro", "Gato", "Elefante", "Leão", "Girafa", "Tigre", "Zebra", "Panda", "Pinguim", "Gorila"]
colors = ["Vermelho", "Azul", "Verde", "Amarelo", "Roxo", "Laranja", "Preto", "Branco", "Cinza", "Marrom"]
countries = ["Brasil", "Estados Unidos", "França", "Japão", "China", "Índia", "Rússia", "Alemanha", "Canadá", "Austrália"]

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
     guess_word = [None] * len(hidden_word)
     for i in range(len(hidden_word)):
           if sugested_letter == hidden_word[i]:
               have_letter = True
               guess_word[i] = sugested_letter
     return guess_word, have_letter

def list_is_full(guess_word):
   if None in guess_word[i]:
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

def main():
     
     while True:
          hidden = word_vectorizer(vector_list)
          guess_word = []
          repeated_char = []
          print("Seja benvindo ao jogo  da forca!")
          
          errors = 0

           guess_word, have_letter  = hanged(hidden,guess_word , letter)
          while True:
               if errors == 6:
                    print("Você perdeu")
                    print("A palavra era",' '.join(guess_word))
                    break
               
               if is_letter(letter):
                    repeated_char,is_repeated = char_repeat_control(repeated_char,letter)
                    if(not is_repeated):
                        
                         
                        

                         if (have_letter):
                              print("A letra existe na palavra. Voce acertou")
                              print(guess_word)
                              if (list_is_full ==True):
                                   print("Parabens você venceu!!")
                                   print("A palavra era ",guess_word)
                                   break
                              else:
                                   continue
                    else:
                         print("Essa letra ja foi indicada anteriormente.")


if __name__==  '__main__':
      main()

'''=============================TESTES========================='''



                





