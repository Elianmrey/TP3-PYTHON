import random

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

def hanged_design():

hidden = word_vectorizer(vector_list)

guess_word=[]
word, booleano  = forca(hidden,guess_word , "a")                

print(word, booleano)