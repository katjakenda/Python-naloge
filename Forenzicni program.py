DNK = open("DNK.txt", "r").read()

Ziga = "korencek, okrogel, rjave, moski, belec"
Matej = "crna, ovalen, modre, moski, belec"
Miha = "rjava, kvadraten, zelene, moski, belec"


if DNK.find("CCAGCAATCGC") != -1:
    barva_las = "crna"
elif DNK.find("GCCAGTGCCG") != -1:
    barva_las = "rjava"
elif DNK.find("TTAGCTATCGC") != -1:
    barva_las = "korencek"

if DNK.find("GCCACGG") != -1:
    oblika_obraza = "kvadraten"
elif DNK.find("ACCACAA") != -1:
    oblika_obraza = "okrogel"
elif DNK.find("AGGCCTCA") != -1:
    oblika_obraza = "ovalen"

if DNK.find("TTGTGGTGGC") != -1:
    barva_oci = "modre"
elif DNK.find("GGGAGGTGGC") != -1:
    barva_oci = "zelene"
elif DNK.find("AAGTAGTGAC") != -1:
    barva_oci = "rjave"

if DNK.find("TGCAGGAACTTC") != -1:
    spol = "moski"
elif DNK.find("TGAAGGACCTTC") != -1:
    spol = "zenska"

if DNK.find("AAAACCTCA") != -1:
    rasa = "belec"
elif DNK.find("CGACTACAG") != -1:
    rasa = "crnec"
elif DNK.find("CGCGGGCCG") != -1:
    rasa = "azijec"

if barva_las == "korencek" and oblika_obraza == "okrogel" and barva_oci == "rjava" and spol == "moski" and rasa == "belec":
    print "Sladoled je pojedel Ziga."

elif barva_las == "crna" and oblika_obraza == "ovalen" and barva_oci == "modre" and spol == "moski" and rasa == "belec":
    print "Sladoled je pojedel Matej."

elif barva_las == "rjava" and oblika_obraza == "kvadraten" and barva_oci == "zelene" and spol == "moski" and rasa == "belec":
    print "Sladoled je pojedel Miha."