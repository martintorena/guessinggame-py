
import random


secret_number = random.randint(1,100)
intents_count = 0
max_intents = 7
ending_counter=0

print("Voy a pensar un numero del 1 al 100 y debes adivinarlo")


while(ending_counter == 0 and intents_count < max_intents):

    number = int(input("¿En que número estoy pensando? \n\t"))

    if (secret_number == number):
        print("Felicidades has adivinado el número.")
        ending_counter += 1
    elif (secret_number < number):
        print("El numero es más  pequeño.")
    else:
        print("El número es más grande.")      

    intents_count += 1

    if ending_counter == 0 and intents_count != max_intents:
        print("Te quedan",max_intents-intents_count,"intentos.")
    elif intents_count == max_intents and ending_counter == 0:
        print("Lo siento has perdido, se te acabaron los intentos.")
    else:
        pass
        
   
        








