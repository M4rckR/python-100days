import random
import my_module

# Genera un número aleatorio entre 1 y 1000
numeroAleatorio = random.randint(1, 1000)

print("Adivina el número que estoy pensando entre 1 y 1000")
print(my_module.my_favorite_number)

# Convertimos en int por que si no no funcionarian los condicionales
intento = int(input("Introduce un número: "))


if  intento == numeroAleatorio:
    print("¡Felicidades! ¡Has adivinado el número!")
elif intento < numeroAleatorio:
    print("El número que estoy pensando es mayor que", intento)
else:
    print("El número que estoy pensando es menor que", intento)
