Translate = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
toochange = int(input("Bitte zahl die umgewandelt werden soll hier eingeben:"))
Basis = int(input("nur noch den dezimal werts:"))

if(len(Translate)<Basis):
    print("Basis ist Größer als Übersetzungs-Tabell")
    print("Breche ab.....")
    exit()

if(Basis<2):
    print("Error: Basis < 1")
    exit()

temp = toochange
out =  ""

while(temp > 0):
    note = int(temp % Basis)
    temp = int(temp / Basis)
    out =  Translate[note] + out
    
print("Ergebnis: %s" %out)