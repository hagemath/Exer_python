#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temp = float(input("Qual a temperatura de graus Fahrenheit? "))
celcius = ((5)*(temp-32))/9
print(f"A temperatura em celcius é de {celcius :.2f}°C")