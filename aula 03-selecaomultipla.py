# ALGPROG - Aula 03 (if / else)
# se for executar só descomente apenas o bloco do exercicio desejado
# este arquivo funciona como historico de evolucão em lógica

## exercicio 1: verificar se um numero inteiro e par ou impar.

##n = int(input("numero: "))
##if n%2 == 0:
##    print("numero é par")
##else:
##    print ("o numero é impar")

## exercicio 2: verificar se um numero é multiplo de 5

##n = int(input("numero: "))
##if n%5 == 0:
##    print("numero é multiplo de 5")
##else:
##    print("numero não multiplo de 5")

## exercicio 3: se A e B forem iguais, soma, caso contrario multiplica

##A = int(input("numero: "))
##B = int(input("numero B:"))

##if A == B:
##    print(A+B)
##else:
##    print(A*B)

## exercicio 4: aplicar reajuste salarial por faixa de valor

##n = int(input("salario: "))

##if n < 500:
##    print(n * 1.15)
##else:       
##    if n >= 500 and n < 1000:
##        print(n * 1.10)
##    else:
##        print(n * 1.05)

## exercicio 5: testar se o primeiro numero é divisivel pelo segundo

##n1 = int(input("numero: "))
##n2 = int(input("numero2: "))

##if n1%n2 == 0:
##    print ("1° digito é divisivel")
##else:
##    print ("1° digito não é divisivel")

#exercicio 6: aumentar preco em 10% apenas se for ate 100.
##n = int(input("preço: "))

##if n > 100:
##    print ("o preço se mantem")
##else:
##    print(n * 1.10)

## exercicio 7: validar senha fixa e informar acesso ou erro

##n = int(input("senha: "))

##if n == 2026:
##    print ("logado")
##else:
##    print ("erro")

## exercicio 8: decidir aprovacao de credito com base em prestação e tempo de servico

##n = int(input("salario bruto: "))
##prestacao = int(input("prestação: "))

##if prestacao > n * 0.30:
##    print("negado")
##else:
##    tempo_de_servico = int(input("digite o tempo em anos: "))
##    if prestacao <= n * 0.30 and tempo_de_servico >= 2:
##        print("aprovado com bonus")
##    else:
##        if tempo_de_servico < 2 and prestacao <= n * 0.30:
##           print("aprovado")

## exercicio 9: classificar categoria com base em idade e peso

##idade = int(input("idade: "))
##if idade >= 18:
##    peso = int(input("peso(kg): "))
##    if peso > 80:
##        print("categoria peso pesado")
##        print("peso médio")
##    else:
##        print("peso inválido")
##else:
##    print("categoria juvenil")

## exercicio 10: aplicar reajuste salarial por faixa de valor denovo

##n = int(input("salario: "))

##if n <= 1500:
##    print(n * 1.15)
##else:
##    if n > 1500 and n <= 3000:
##       print (n * 1.10)
##    else: 
##        if n > 3000:
##            print (n * 1.05)

## exercicio 11: identificar o quadrante de um ponto no plano cartesiano
##x= int(input("x: "))
##y= int(input("y: "))
##if x ==0:
##    if y == 0:
##        print("origem")
##    else:
##        print("eixo y")
##else:
##    if x>0:
##        if y==0:
##            print("eixo x, porem x positivo")
##        else:
##            if y>0:
##                print("Q1")
##            else:
##                print("Q4")
##    else:
##        if y==0:
##            print("eixo x, porem x negativo")
##        else:
##            if y>0:
##                print("Q2")
##            else:
##                print("Q3")

## exercicio 12: verificar condição de existência do triangulo e classificar o tipo

##l1 = int(input("lado 1 do triangulo: "))
##l2 = int(input("lado 2 do triangulo: "))
##l3 = int(input("lado 3 do triangulo: "))

##if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
##    print ("não é um triangulo pela condição de existencia de um triangulo")
##else: 
##    if l1 == l2 == l3:
##        print ("triangulo equilatero")
##    else:
##        if l1 == l2 or l1 == l3 or l2 == l3:
##           print ("triangulo isosceles")
##        else:
##            print ("triangulo escaleno")


## exercicio 13: calcular raizes reais da equacao do 2o grau via delta.

##a = int(input("valor de a: "))
##b = int(input("valor de b: "))
##c = int(input("valor de c: "))

##if a != 0:
##    delta = (b**2 - 4*a*c)
##    if delta < 0:
##        print("não ha raizes reais")
##    else:
##        if (delta) == 0:
##            x = (-b)/(2*a)
##            print (f"há uma raiz real: {x}")
##        else:
##            if delta > 0:
##                x1= (-b + delta**0.5)/(2*a)
##                x2= (-b - delta**0.5)/(2*a)
##                print(f"há duas raizes reais distintas: {x1},{x2}")
##else:
##     print("não existe equação do segundo grau com A = 0")

## exercicio 14: resolver sistema linear quando divisao é possivel

##a = int(input("valor de a: "))
##b = int(input("valor de b: "))
##c = int(input("valor de c: "))
##d = int(input("valor de d: "))
##e = int(input("valor de e: "))
##f = int(input("valor de f: "))

##divisao= a*e - b*d
##if divisao != 0:
##    x= (c*e - b*f) / divisao
##    y= (a*f - c*d) / divisao
##    print (x,y)
##else:
##    print ("infinitas soluções ou nenhuma solução")

# VALE NOTAR : x + y = 2 e 2x + 2y = 4 é uma solução infinita
# VALE NOTAR : a=1 b=1 c=2 d=2 e=2 f=5 é uma solucao invalida, pois x+y = 2 e 2x+2y = 5
