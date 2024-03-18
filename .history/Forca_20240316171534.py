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
          random_list = random.choice(vector_list[random_num(0, len(vector_list)-1)])
          random_word = random.choice(random_list)
          vectorized_word
          for i in range(len(random_word)):
            vectorized_word +=  random_word+random_word[i]
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



hidden = word_vectorizer(vector_list)
print(hidden)
guess_word=[]
word, booleano  = forca(hidden,guess_word , "a")                
print("Letras já adivinhadas: ", ' '.join(word))
if booleano : print("\nParabéns você acertou!")
else:         print("\nErrou! Tente novamente.")