try:
  n1 = int (input("Digite o primeiro numero:"))
  print(n1)
  n2 = int (input("Digite o segundo numero:"))
  print(n2)

  calculo = n1/n2
  print ("Resultado da Divisao", calculo)

except ValueError:
  print("Digite um valor numerico")
except ZeroDivisionError:
  print ("Nao e possivel dividir por zero")  
except:
  print ("Erro inesperado!")  
finally:
  #"O que é finally bloco, se especificado, será executado Independentemente se o bloco de tentativa levanta um erro ou não."
  print ( "The 'try except' is finished")  