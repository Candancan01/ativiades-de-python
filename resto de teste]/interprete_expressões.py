print("aqui vamos fazer alguns testes de True e False e operadores logicos")

idade= int(input("digite sua idade: "))
nota=float(input("digite sua nota: "))
frequencia=int(input("digite sua frequencia: "))

a = idade >= 18 and nota >= 6
b = nota >= 8 or frequencia >= 75
c = not (idade < 18)
d = idade >= 18 and nota >= 6 and frequencia >= 75

print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)

if a == False:
 if idade < 18:
  print(" o campo A deu falso pq a idade é menor que 18")

if nota < 6:
    print(" o campo A deu falso pq a nota é menor que 6")
    print("\n")

if b == False:
 if nota < 8:
  print(" o campo B deu falso pq a nota é menor que 8") 

if frequencia < 75:
    print(" o campo B deu falso pq a frequencia é menor que 75")
    print("\n")

if c == False:
 if idade < 18:
  print(" o campo C deu falso pq a idade é menor que 18") 
  print("\n")

if d == False:
  if idade < 18:
   print(" o campo D deu falso pq a idade é menor que 18")
  if nota < 6:
   print(" o campo D deu falso pq a nota é menor que 6")
  if frequencia < 75:
   print(" o campo D deu falso pq a frequencia é menor que 75")
   