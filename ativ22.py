# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.
contador = 0

while True:
    nm = int(input("Digite os numeros que deseja somar (digite 0 quando quiser parar):"))
    if nm == 0:
        break
    contador += nm

print(contador)
