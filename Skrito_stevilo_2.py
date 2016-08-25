# -*- coding: utf-8 -*-

from random import randint


def main():
    print("UGANITE SKRITO ŠTEVILO!" + "\n" + "Skrito število je celo število, ki se nahaja med 1 in 100.")
    skrito = randint(1, 100)

    while True:
        ugibanje = int(raw_input("Uganite skrito število: "))

        print skrito
        skrito_stevilo(ugibanje, skrito)

        ponovno = raw_input("Želite ponovno ugibati (da/ne)? ")

        if ponovno.lower() == "ne":
            print "Nasvidenje"
            break

        if skrito_stevilo == True:
            skrito = randint(1, 100)



def skrito_stevilo(guess, secret):

    if guess == secret:
        print("ZADETEK! Čestitamo. Ugotovili ste skrito število.")
        return True


    else:
        print("Brez zadetka. Več sreče prihodnjič")
        return False


if __name__ == "__main__":
    main()