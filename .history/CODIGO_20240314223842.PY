def nome_e_sobrenome(arrayNome):
         iniciais = (arrayNome[0][0]).join(arrayNome[1][0]).t
         return iniciais


print(nome_e_sobrenome(["Elian", "Montes"]))