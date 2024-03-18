import re as reg_expresion


def nome_e_sobrenome(arrayNome):
         iniciais_maiusculo = ''
         for  i in range(len(arrayNome)):
            iniciais_maiusculo +=  arrayNome[i][0].upper()        #--------->>> Pega a primeira letra de cada palavra e junta.
         return iniciais_maiusculo


def email_valido(email):
      regex = r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$'
      if reg_expresion.match(regex, email):
          return True
      else:
            return False
      



print(nome_e_sobrenome(["Elian", "Montes"]))

if email_valido("elian060893@gmail.com"):
print("Email é válido")