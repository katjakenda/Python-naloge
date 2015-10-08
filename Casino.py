
stevilo = 27

ponavljaj = True
while ponavljaj == True:

    x = raw_input("Katero je skrito stevilo? ")
    vnos = int(x)

    if stevilo < vnos:
        print("Manjsa je")
    elif stevilo > vnos:
        print("Vecja je")


    else:
        print("Zadetek")
        break


