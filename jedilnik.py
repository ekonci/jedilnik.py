print "JEDILNIK"

dnevni_meni = {}

while True:
    jed = raw_input("Vnesi glavno jed: ")
    cena = raw_input("Vnesi ceno: ")

    dnevni_meni[jed] = cena

    konec = raw_input("Ali zelis nadaljevati DA/NE? ")

    if konec == "NE":
        print dnevni_meni
        break

todo_file = open("jedilnik.txt", "w+")
todo_file.write("JEDILNIK")
for k, v in dnevni_meni.iteritems():
    todo_file.write("\n jed: " + k + "\n cena: " + v)

print "KONEC"
for k, v in dnevni_meni.iteritems():
    print "\n jed: " + k + " / cena: " + v
