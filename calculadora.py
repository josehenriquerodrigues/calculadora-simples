1
1# funçao para realizar a adiçao
def adiçao(a, b):
    return a + b

# funçao para realizar a subitraçao
def subitraçao(a, b):
    return a - b

#funçao para realizar a mutiplicaçao
def mutiplicaçao(a, b):
    return a * b

#funçao para realizar a divisao
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return " nao e possivel dividir por zero. "
    
#funçao principal para a calculadora
def calculadora():
    print("calculadora simples")
    print("escolha a operaçao:")
    print("1. adiçao")
    print("2. subtraçao")
    print("3. mutiplicaçao")
    print("4. diviçao")
    
    escolha = input("digite o numero da operaçao desejada: ")
    
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    
    if escolha == '1':
        resultado = adiçao(num1, num2)
        print(f"resultado: {resultado}")
    elif escolha == '2':
        resultado = subitraçao(num1, num2)
        print(f"resultado: {resultado}")
    elif escolha == '3':
        resultado = mutiplicaçao(num1, num2)
        print(f"resultado: {resultado}") 
    elif escolha == '4':
        resultado = divisao(num1, num2)
        print(f"resultado {resultado}") 
    else:
        print("opçao invalida. por favor, escolha uma opçao  valida. ")
        
# chama a funçao principal da culculadora
calculadora()