# Ejercicio: Piedra, papel o tijeras
import random

hands_forms = ['piedra', 'papel', 'tijeras']
option_bot = random.randint(0, 2)

print("Bienvenido al juego de piedra, papel o tijeras")
print("Selecciona una opción:")
print("1. Piedra")
print("2. Papel")
print("3. Tijeras")


option_human = int(input("Selecciona una opcion para jugar: ")) - 1

print("Tu has seleccionado: ", hands_forms[option_human])
print("El bot ha seleccionado: ", hands_forms[option_bot])

if(option_human == option_bot):
    print("Empate")
elif(option_human == 0 and option_bot == 2):
    print("Ganaste")
elif(option_human == 1 and option_bot == 0):
    print("Ganaste")
elif(option_human == 2 and option_bot == 1):
    print("Ganaste")
else:
    print("Perdiste")