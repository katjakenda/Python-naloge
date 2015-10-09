x = raw_input("Vnesi stevilo x: ")

while 1 == 1:
    if x.isdigit():
       x = int(x)
       break
    else:
        x = raw_input("Ponovno vnesi stevilo x. Bodi pozoren, da gre res za stevilo: ")

y = raw_input("Vnesi stevilo y: ")
while 1 == 1:
    if y.isdigit():
       y = int(y)
       break
    else:
        y = raw_input("Ponovno vnesi stevilo y. Bodi pozoren, da gre res za stevilo: ")

operacija = raw_input("Vnesi zeljeno operacijo (+, -, *, /)")
while 1 == 1:
    if operacija == "+":
        print x + y
        break
    elif operacija == "-":
        print x - y
        break
    elif operacija == "*":
        print x * y
        break
    elif operacija == "/":
        print x / y
        break
    else:
        operacija = raw_input("Ponovno vpisi operacijo, bodi pozoren, da si jo vpisal z naslednjimi znaki (+, -, *, /): ")