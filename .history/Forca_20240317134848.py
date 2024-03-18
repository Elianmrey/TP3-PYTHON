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
    for i in len(guess_word):  
      if guess_word[i]  is None:
        return False
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
def letter_repeat_control(list_char,letter):
      
      if letter in list_char:
         return list_char,True
      else:
         list_char.append(letter)
         return list_char,False

def main():
     
     while True:
          hidden = word_vectorizer(vector_list)
          guess_word = []
          repeated_char = 
          print("Seja benvindo ao jogo  da forca!")
          
          errors = 0
          while True:
               if errors == 6:
                    break
               letter = input("\nDigite uma letra: ").strip().lower()
               if  is_letter(letter):
                    guess_word,is_new
               word, have_letter  = hanged(hidden,guess_word , letter)



'''=============================TESTES========================='''



                
for i in range(7):
      hanged_design(i)
print(word, booleano)


lista_repeat_charge = []
value_list, repeating = letter_repeat_control(lista_repeat_charge,"a")

other, value =  letter_repeat_control(lista_repeat_charge,"b")

valor, bo =  letter_repeat_control(lista_repeat_charge,"25")


print("Value List", value_list)
print(repeating)

print("Value List", other)
print(value)

print("Value List", valor)
print(bo)

