import re
#dictionnaire txt to morse
MORSE = {' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}
	
#dictionnaire morse to txt
TXT = {'_': ' ', 
	'.----.': "'", 
	'-.--.-': '(', 
	'-.--.-': ')', 
	'--..--': ',', 
	'-....-': '-', 
	'.-.-.-': '.', 
	'-..-.': '/', 
	'-----': '0', 
	'.----': '1', 
	'..---': '2', 
	'...--': '3', 
	'....-': '4', 
	'.....': '5', 
	'-....': '6', 
	'--...': '7', 
	'---..': '8', 
	'----.': '9', 
	'---...': ':', 
	'-.-.-.': ';', 
	'..--..': '?', 
	'.-': 'A', 
	'-...': 'B', 
	'-.-.': 'C', 
	'-..': 'D', 
	'.': 'E', 
	'..-.': 'F', 
	'--.': 'G', 
	'....': 'H', 
	'..': 'I', 
	'.---': 'J', 
	'-.-': 'K', 
	'.-..': 'L', 
	'--': 'M', 
	'-.': 'N', 
	'---': 'O', 
	'.--.': 'P', 
	'--.-': 'Q', 
	'.-.': 'R', 
	'...': 'S', 
	'-': 'T', 
	'..-': 'U', 
	'...-': 'V', 
	'.--': 'W', 
	'-..-': 'X', 
	'-.--': 'Y', 
	'--..': 'Z', 
	'..--.-': '_'
	
}

def cesar (texte,key) :
    crypted_text=list(texte)
    for loop in range (len(crypted_text)) :
      crypted_text[loop]=chr(ord(crypted_text[loop]) + key)
    texte="".join(crypted_text)
    return texte

def affine (texte, key) :
    liste_key=list(key)
    premiers="".join(liste_key[:2])
    derniers="".join(liste_key[-2:])
    coeff=re.search("x$", premiers)
    coeff_bis=re.search("x$", derniers)
    crypted_text=list(texte)
    if (coeff) :
        coefficient=int(liste_key[0])
        ordonnee=int(liste_key[3])
    elif (coeff_bis) :
        coefficient=int(liste_key[2])
        ordonnee=int(liste_key[0])
    else :
        print("Veuillez réessayer : )   (en relançant le programme) ")
        print("N'oubliez pas que les chiffres doivent être compris entre 0 et 9")
    for loop in range (len(crypted_text)) :
      crypted_text[loop]=chr(ord(crypted_text[loop]) * coefficient + ordonnee)
    texte="".join(crypted_text)
    return texte

def vigenere (texte, key) :
    crypted_text=list(texte)
    key=list(key)
    a=0
    for loop in range (len(crypted_text)) :
        while a < len(key) :
            key[a]=ord(key[a])
            crypted_text[a]=chr(ord(crypted_text[a]) + key[a])
            a=a+1
        crypted_text[a]=chr(ord(crypted_text[a]) + key[a%len(key)])
        a=a+1
    texte="".join(crypted_text)
    return texte

def carre (texte) :
    texte=texte.lower()
    lettres= list(re.findall("\w", texte))
    specials= list(re.findall("\W", texte))
    texte=list(texte)
    ordonnee=[0]*len(texte)
    abscisse=[0]*len(texte)
    crypted_text=""
    loop_ab=0
    loop_or=0
    for coco in range (len(texte)) :
        if lettres.count(texte[coco]) > 0 :
            lettres[loop_ab]=ord(lettres[loop_ab]) - 97
            ordonnee[loop_ab]=((lettres[loop_ab] % 5) +1)
            abscisse[loop_ab]=(lettres[loop_ab]//5)+1
            crypted_text=crypted_text+str(abscisse[loop_ab])
            crypted_text=crypted_text+str(ordonnee[loop_ab])
            loop_ab=loop_ab+1
        elif specials.count(texte[coco]) > 0 :
            abscisse[loop_or]=6
            specials[loop_or]=ord(specials[loop_or])
            if specials[loop_or]==32 :
                ordonnee[loop_or]=2
            elif specials[loop_or]==39 :
                ordonnee[loop_or]=5
            elif specials[loop_or]==44 :
                ordonnee[loop_or]=4
            elif specials[loop_or]==46 :
                ordonnee[loop_or]=3
            crypted_text=crypted_text+str(abscisse[loop_or])
            crypted_text=crypted_text+str(ordonnee[loop_or])
            loop_or=loop_or+1
    return crypted_text

def alphabet(décryptage) :
    crypted_texte=list(str(décryptage))
    texte=[0]*(len(crypted_texte)//2)
    rang=0
    for loop in range (len(crypted_texte)) :
        if loop%2==0 :
            indice_lettre=int(crypted_texte[loop])
        elif loop%2==1 :
            lettre=chr((5*(indice_lettre-1)+int(crypted_texte[loop]))+96)
            texte[rang]=lettre
            rang=rang+1
    phrase="".join(texte)
    return phrase

def convertToMorseCode(phrase):
    phrase = phrase.upper()
    phrasecrypte = ""
    for lettre in phrase:
        phrasecrypte += MORSE[lettre] + " " 
    return phrasecrypte

rep=input("Voulez-vous encrypter ou décoder un texte ? ")
cryptage=re.search(r"\Bncrypt\B", rep) or re.search(r"\Bncod\B", rep)
décodage=re.search(r"\Bécod\B", rep) or re.search(r"\Bécrypt\B", rep)

if (cryptage) :
    codage = input("Quelle sorte de codage voulez-vous utiliser ? ")
    Cesar=re.search(r"sar\b", codage)
    Affine=re.search(r"ffine\b", codage)
    Vigenere=re.search(r"\Bigen\B", codage)
    Carre=re.search(r"\Barr\B" and r"lphabet\b", codage)
    if (Cesar) :
        texte=input("Quel texte voulez-vous encrypter ? /!\ pas de nombre s'il vous plaît : ) ")
        key=int(input("De combien voulez-vous décaler votre texte ? "))
        texte=cesar (texte, key)
        print(texte)
    elif (Affine) :
        texte=input("Quel texte voulez-vous encrypter ? /!\ pas de nombre s'il vous plaît : ) ")
        key=input("Quelle est la fonction de cryptage secrète ? /!\ mettre sous la forme d'une fonction ENTRE 0 ET 9 !! ")
        texte=affine (texte, key)
        print(texte)
    elif (Vigenere) :
        texte=input("Quel texte voulez-vous encrypter ? /!\ pas de nombre s'il vous plaît : ) ")
        key=input("Quelle est la clé de cryptage secrète ? ")
        texte=vigenere (texte, key)
        print(texte)
    elif (Carre) :
        texte=input("Quel texte voulez-vous encrypter ? /!\ pas de caractères spéciaux s'il vous plaît : ) ")
        texte=carre (texte)
        print(texte)
    else :
        print ("Nous n'avons pas de correspondance pour ce type d'encryptage. Vérifiez l'orthographe et le nom de l'encryptage que vous souhaitez : )")
        
elif (décodage) :
    décryptage=input("Quel est le texte à décoder ? ")
    specials=re.search("\d", décryptage)
    if (specials) :
        if len(list(décryptage))%2==0 :
            texte=alphabet(décryptage)
            print(texte)
        elif (MORSEk ) :
        	print('Le message à mettre en morse ?')
        	message = input()
        	morse = convertToMorseCode(message)
        	print(MORSE)
    elif :
        ANALYSE FRÉQUENTIELLE

    
else :
    print ("Vérifiez l'orthographe des mots saisis")
    print ("Saisissez bien des mots de la famile d'encodage, encryptage, décodage ou décryptage")import re

def cesar (texte,key) :
    crypted_text=list(texte)
    for loop in range (len(crypted_text)) :
      crypted_text[loop]=chr(ord(crypted_text[loop]) + key)
    texte="".join(crypted_text)
    return texte

def affine (texte, key) :
    liste_key=list(key)
    premiers="".join(liste_key[:2])
    derniers="".join(liste_key[-2:])
    coeff=re.search("x$", premiers)
    coeff_bis=re.search("x$", derniers)
    crypted_text=list(texte)
    if (coeff) :
        coefficient=int(liste_key[0])
        ordonnee=int(liste_key[3])
    elif (coeff_bis) :
        coefficient=int(liste_key[2])
        ordonnee=int(liste_key[0])
    else :
        print("Veuillez réessayer : )   (en relançant le programme) ")
        print("N'oubliez pas que les chiffres doivent être compris entre 0 et 9")
    for loop in range (len(crypted_text)) :
      crypted_text[loop]=chr(ord(crypted_text[loop]) * coefficient + ordonnee)
    texte="".join(crypted_text)
    return texte

def vigenere (texte, key) :
    crypted_text=list(texte)
    key=list(key)
    a=0
    for loop in range (len(crypted_text)) :
        while a < len(key) :
            key[a]=ord(key[a])
            crypted_text[a]=chr(ord(crypted_text[a]) + key[a])
            a=a+1
        crypted_text[a]=chr(ord(crypted_text[a]) + key[a%len(key)])
        a=a+1
    texte="".join(crypted_text)
    return texte

def carre (texte) :
    texte=texte.lower()
    lettres= list(re.findall("\w", texte))
    specials= list(re.findall("\W", texte))
    texte=list(texte)
    ordonnee=[0]*len(texte)
    abscisse=[0]*len(texte)
    crypted_text=""
    loop_ab=0
    loop_or=0
    for coco in range (len(texte)) :
        if lettres.count(texte[coco]) > 0 :
            lettres[loop_ab]=ord(lettres[loop_ab]) - 97
            ordonnee[loop_ab]=((lettres[loop_ab] % 5) +1)
            abscisse[loop_ab]=(lettres[loop_ab]//5)+1
            crypted_text=crypted_text+str(abscisse[loop_ab])
            crypted_text=crypted_text+str(ordonnee[loop_ab])
            loop_ab=loop_ab+1
        elif specials.count(texte[coco]) > 0 :
            abscisse[loop_or]=6
            specials[loop_or]=ord(specials[loop_or])
            if specials[loop_or]==32 :
                ordonnee[loop_or]=2
            elif specials[loop_or]==39 :
                ordonnee[loop_or]=5
            elif specials[loop_or]==44 :
                ordonnee[loop_or]=4
            elif specials[loop_or]==46 :
                ordonnee[loop_or]=3
            crypted_text=crypted_text+str(abscisse[loop_or])
            crypted_text=crypted_text+str(ordonnee[loop_or])
            loop_or=loop_or+1
    return crypted_text

def alphabet(décryptage) :
    crypted_texte=list(str(décryptage))
    texte=[0]*(len(crypted_texte)//2)
    rang=0
    for loop in range (len(crypted_texte)) :
        if loop%2==0 :
            indice_lettre=int(crypted_texte[loop])
        elif loop%2==1 :
            lettre=chr((5*(indice_lettre-1)+int(crypted_texte[loop]))+96)
            texte[rang]=lettre
            rang=rang+1
    phrase="".join(texte)
    return phrase

def convertToMorseCode(phrase):
    phrase = phrase.upper()
    phrasecrypte = ""
    for lettre in phrase:
        phrasecrypte += MORSE[lettre] + " " 
    return phrasecrypte

rep=input("Voulez-vous encrypter ou décoder un texte ? ")
cryptage=re.search(r"\Bncrypt\B", rep) or re.search(r"\Bncod\B", rep)
décodage=re.search(r"\Bécod\B", rep) or re.search(r"\Bécrypt\B", rep)

if (cryptage) :
    codage = input("Quelle sorte de codage voulez-vous utiliser ? ")
    Cesar=re.search(r"sar\b", codage)
    Affine=re.search(r"ffine\b", codage)
    Vigenere=re.search(r"\Bigen\B", codage)
    Carre=re.search(r"\Barr\B" and r"lphabet\b", codage)
    if (Cesar) :
        texte=input("Quel texte voulez-vous encrypter ? /!\ pas de nombre s'il vous plaît : ) ")
        key=int(input("De combien voulez-vous décaler votre texte ? "))
        texte=cesar (texte, key)
        print(texte)
    elif (Affine) :
        texte=input("Quel texte voulez-vous encrypter ? /!\ pas de nombre s'il vous plaît : ) ")
        key=input("Quelle est la fonction de cryptage secrète ? /!\ mettre sous la forme d'une fonction ENTRE 0 ET 9 !! ")
        texte=affine (texte, key)
        print(texte)
    elif (Vigenere) :
        texte=input("Quel texte voulez-vous encrypter ? /!\ pas de nombre s'il vous plaît : ) ")
        key=input("Quelle est la clé de cryptage secrète ? ")
        texte=vigenere (texte, key)
        print(texte)
    elif (Carre) :
        texte=input("Quel texte voulez-vous encrypter ? /!\ pas de caractères spéciaux s'il vous plaît : ) ")
        texte=carre (texte)
        print(texte)
    else :
        print ("Nous n'avons pas de correspondance pour ce type d'encryptage. Vérifiez l'orthographe et le nom de l'encryptage que vous souhaitez : )")
        
elif (décodage) :
    décryptage=input("Quel est le texte à décoder ? ")
    specials=re.search("\d", décryptage)
    if (specials) :
        if len(list(décryptage))%2==0 :
            texte=alphabet(décryptage)
            print(texte)
        elif (MORSEk ) :
        	print('Le message à mettre en morse ?')
        	message = input()
        	morse = convertToMorseCode(message)
        	print(MORSE)
    elif :
        ANALYSE FRÉQUENTIELLE

    
else :
    print ("Vérifiez l'orthographe des mots saisis")
    print ("Saisissez bien des mots de la famile d'encodage, encryptage, décodage ou décryptage")
