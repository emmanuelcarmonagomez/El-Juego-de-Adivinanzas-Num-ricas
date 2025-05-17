import random

numero_secreto = random.randint(1, 50)

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en un número entre 1 y 50. Tienes 10 intentos para adivinarlo.")
print("Recuerda: Solo puedes ingresar números ENTEROS.")

for intento in range(1, 11):
    try:
        numero = int(input(f"Intento {intento}: Ingresa tu número: "))

        if numero == numero_secreto:
            print(f"🎉 ¡Felicidades! Adivinaste el número secreto ({numero_secreto}) en {intento} intento(s).")
            break

        elif numero > numero_secreto:
            print("🔻 El número secreto es menor.")
        else:
            print("🔺 El número secreto es mayor.")     
    except ValueError:
        print("⚠️ Por favor, ingresa un número entero válido.")

else:
    print(f"❌ Se acabaron los intentos. El número secreto era {numero_secreto}.")

print("Gracias por jugar.")
input("Presiona Enter para salir del juego...")
