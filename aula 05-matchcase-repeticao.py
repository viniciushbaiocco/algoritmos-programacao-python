## exercicio 1: verificar se a idade permite doar sangue
##idade=int(input("idade: "))
##while 18<=idade<=67:
##    print("voce pode doar sangue")
##    idade=int(input("idade: "))
##else:
##    print("idade não esta entre os valores 18 e 67")

## exercicio 2: testar se um valor z está entre x e y
##x=int(input("x: "))
##y=int(input("y: "))
##z=int(input("z: "))
##if z>=x:
##    if z<=y:
##        print("está entre os intervalos x e y")
##    else:
##        print("ultrapassou valor de y")
##else: 
##    print("valor menor que x")

## exercicio 3: ordenar tres valores em ordem crescente
##A=int(input("A: "))
##B=int(input("B: "))
##C=int(input("C: "))
##if A<B and A<C:
##    if B<C:
##        print(f"{A}, {B}, {C}")
##   else:
##        print(f"{A}, {C}, {B}")
##if B<A and B<C:
##    if A<C:
##       print(f"{B}, {A}, {C}")
##    else:
##        print(f"{B}, {C}, {A}")
##if C<A and C<B:
##    if A<B:
##        print(f"{C}, {A}, {B}")
##    else:
##        print(f"{C}, {B}, {A}")

## exercicio 4: reajustar salario conforme o plano de trabalho com match case
# plano=int(input("digite o plano de trabalho: "))
# salario=int(input("digite o salario: "))
# match plano:
#     case 1:
#         SalNovo = salario * 1.10
#     case 2:
#         SalNovo = salario * 1.15
#     case 3:
#         SalNovo = salario * 1.20
# print(f"plano escolhido {plano}, o seu salario foi pra {SalNovo}")

## exercicio 5: calcular potencia de x elevado a n com repeticao
# x = int(input("Digite o valor de x: "))
# n = int(input("Digite o valor de n: "))
# resultado = 1
# numero = 0
# while numero<n:
#     resultado *= x
#     numero = numero + 1
# print(f"{resultado}")

## exercicio 6: executar operacao escolhida entre dois numeros
# numero1=int(input("numero1: "))
# numero2=int(input("numero2: "))
# escolha=int(input("escolha: "))
# match escolha:
#     case 1:
#         print((numero1+numero2)/2)
#     case 2:
#         if numero1>numero2:
#             print(numero1-numero2)
#         else:
#             print(numero2-numero1)
#     case 3:
#         print(numero1*numero2)
#     case 4:
#         print(numero1/numero2)

## exercicio 7: classificar produto pelo codigo usando match case
# codigo=int(input("codigo do produto: "))
# match codigo:
#     case 1:
#         print("Alimento não perecivel")
#     case 2|3|4:
#         print("alimento perecivel")
#     case 5|6:
#         print("Vestuario")
#     case 7:
#         print("higiene pessoal")
#     case 8|9|10|11|12|13|14|15:
#         print("limpeza e utensilios domesticos")
#     case _:
#         print("codigo invalido, apenas do 1 ate o 15 são validos")

## exercicio 8: mostrar multiplos de 7 entre 100 e 450
# numero = 100

# while numero <= 450:
#     if numero % 7 == 0:
#         print(numero)
#     numero += 1

## exercicio 9: somar os pares e contar os impares de uma sequencia
# n=int(input("qtde de numeros: "))
# x=0
# pares=0
# impares=0
# while x<n:
#     numeros=int(input("escreva os numeros: "))
#     if numeros%2 == 0:
#         pares +=numeros
#     else:
#         impares +=1
#     x += 1

# print(f"soma dos pares:{pares}")
# print(f"quantidade de impares:{impares}")

## exercicio 10: calcular o fatorial de um numero

# n=int(input('valor de n: '))
# i=n
# if n == 0:
#     print("valor 1 por definição")
# else:
#     while i>1:
#         i-=1
#         n*=i
#     print(n)

## exercicio 11: encontrar o maior e o menor entre varios numeros
# quant=int(input("quantos numeros: "))
# control = quant
# if quant <10:
#     print("numero tem que ser maior que 10")
# else:
#     n = int(input("n: "))
#     maior = n
#     menor = n
#     control -= 1
#     while control>0:
#         control -= 1
#         n=int(input("n: "))
#         if maior<n:
#             maior = n
#             print("o numero maior ta sendo esse", maior)
#             print("o numero menor ta sendo esse", menor)
#         else:
#             if n<menor:
#                 menor = n
#                 print("o numero maior ta sendo esse", maior)
#                 print("o numero menor ta sendo esse", menor)
#     print(maior,menor)
