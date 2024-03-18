def nome_e_sobrenome(arrayNome):
         iniciais_maiusculo = ''
         for  i in range(len(arrayNome)):
            iniciais_maiusculo +=  arrayNome[i][0].upper()        #--------->>> Pega a primeira letra de cada palavra e junta.
         return iniciais_maiusculo


def email_valido(email):
      reg = r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$'
      



print(nome_e_sobrenome(["Elian", "Montes"]))