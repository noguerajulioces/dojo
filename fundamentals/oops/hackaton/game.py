from classes.deck import Deck
from classes.highcard import HighCardWinsGame

while True:
    print("-"*40)
    print("Bienvenidos a HighCardWinsGame")
    print("-"*40)
    print('Presione "1" para iniciar el juego')
    print('Presione "2" para mostrar las intrucciones')
    print('Presione "3" para salir')
    opcion = input(" ")
    print("-"*40)

    
    if(opcion == "1"):
        game = HighCardWinsGame()
        game.play_round()
        input("Presione Enter para continuar...")
    elif opcion == "2":
        print("El jugador que tenga la carta más alta gana la ronda.")
        print("-" * 40) #imprime - 40 veces en la consola para que quede bonito
        input("Presione Enter para continuar...")
    elif(opcion == "3"):
        break