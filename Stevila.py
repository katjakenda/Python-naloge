
vnos = raw_input("Napisi stevilko med 1 in 100: ")
while 1 == 1:
    if vnos.isdigit():
       vnos = int(vnos)
       break
    else:
        vnos = raw_input("Ponovno napisi stevilko med 1 in 100: ")

stevilo = int(vnos)
for ostanek in range(1, stevilo):

    if ostanek % 3 == 0 and ostanek % 5 == 0:
        print ("fizzbuzz")
    elif ostanek % 5 == 0:
        print ("buzz")
    elif ostanek % 3 == 0:
        print ("fizz")
    else:
        print "drugo:" + str(ostanek)