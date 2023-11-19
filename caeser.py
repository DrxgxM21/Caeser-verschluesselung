Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]                #Das grosse Alphabet für das suchen nach den Zahlen
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]                #Das kleine Alphabet für das suchen nach den Zahlen

with open('DerText.txt', 'r', encoding= 'utf-8') as file:                 #Datei wird ausgelesen
    Text = file.read()
Buchstaben = []                                                                         #Liste für die Stellen

for i in Text:                                                                            #Buchtsaben werden einzeln in die Liste gepackt
    Buchstaben.append(i)

anzahl_der_wechsel = 6                                                                      #Die Anzahl um wie viele Stellen es verschoben wird

for wechsel in range(len(Buchstaben)):                                                      #For Schleife die so lange ist wie die Liste stellen hat
    if Buchstaben[wechsel] in Alphabet:                                                     #Schaut nach ob das vorhanden ist
        index = Alphabet.index(Buchstaben[wechsel])                                         #Die Variable index wird zum index von dem Alphabtet bezüglich des indexes in den Buchstaben
        neuer_index = (index + anzahl_der_wechsel) % len(Alphabet)                          #Varaiable neuer_index ist dann der Buchtabe der bei der verschiebung ausgegeben wird
        Buchstaben[wechsel] = Alphabet[neuer_index]                                         #Die Buchstaben werden in der liste ersetzt

for wechsel in range(len(Buchstaben)):                                                      #Siehe Zeile 13-17 
    if Buchstaben[wechsel] in alphabet:
        index = alphabet.index(Buchstaben[wechsel])
        neuer_index = (index + anzahl_der_wechsel) % len(alphabet)
        Buchstaben[wechsel] = alphabet[neuer_index]

fertiger_Schluessel= ''.join(Buchstaben)                                                    #Liste mit mehreren Strings wird zu einem String umgewandelt

with open("EntverschlüsselterText.txt", "w") as f:
     f.write(fertiger_Schluessel)

print(fertiger_Schluessel)                                                                  #Ausgabe des fertigen Textes