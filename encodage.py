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
		'..--.-': '_'}
		
#cryp Morse (txt a morse)
def convertToMorseCode(phrase):
    phrase = phrase.upper()
    phrasecrypte = ""
    for lettre in phrase:
        phrasecrypte += MORSE[lettre] + " " 
    return phrasecrypte


def carre(texte):
    texte = texte.lower()
    lettres = list(re.findall("\w", texte))
    specials = list(re.findall("\W", texte))
    texte = list(texte)
    ordonnee = [0]*len(texte)
    abscisse = [0]*len(texte)
    crypted_text = ""
    loop_ab = 0
    loop_or = 0
    for coco in range(len(texte)):
        if lettres.count(texte[coco]) > 0:
            lettres[loop_ab] = ord(lettres[loop_ab]) - 97
            ordonnee[loop_ab] = ((lettres[loop_ab] % 5) + 1)
            abscisse[loop_ab] = (lettres[loop_ab]//5)+1
            crypted_text = crypted_text+str(abscisse[loop_ab])
            crypted_text = crypted_text+str(ordonnee[loop_ab])
            loop_ab = loop_ab+1
        elif specials.count(texte[coco]) > 0:
            abscisse[loop_or] = 6
            specials[loop_or] = ord(specials[loop_or])
            if specials[loop_or] == 32:
                ordonnee[loop_or] = 2
            elif specials[loop_or] == 39:
                ordonnee[loop_or] = 5
            elif specials[loop_or] == 44:
                ordonnee[loop_or] = 4
            elif specials[loop_or] == 46:
                ordonnee[loop_or] = 3
            crypted_text = crypted_text+str(abscisse[loop_or])
            crypted_text = crypted_text+str(ordonnee[loop_or])
            loop_or = loop_or+1
    return crypted_text


def alphabet(décryptage):
    crypted_texte = list(str(décryptage))
    texte = [0]*(len(crypted_texte)//2)
    rang = 0
    for loop in range(len(crypted_texte)):
        if loop % 2 == 0:
            indice_lettre = int(crypted_texte[loop])
        elif loop % 2 == 1:
            lettre = chr((5*(indice_lettre-1)+int(crypted_texte[loop]))+96)
            texte[rang] = lettre
            rang = rang+1
    phrase = "".join(texte)
    return phrase

rep = input("Voulez-vous encrypter ou décoder un texte ? ")
codage = re.search(r"\Bncod\B", rep)
décodage = re.search(r"\Bécrypt\B", rep)

if (codage):  # pour encoder un texte
    code = input("Quelle sorte de codage voulez-vous utiliser ? ")
    Carre = re.search(r"\Barr\B" and r"lphabet\b", code)
    Morse = search("morse" or "Morse", code)
    if (Carre):
        texte = input(
            "Quel texte voulez-vous encrypter ? /!\ pas de caractères spéciaux s'il vous plaît : ) ")
        texte = carre(texte)
        print(texte)
    elif (Morse):
	print('Le message à mettre en morse ?')
	message = input()
	morse = convertToMorseCode(message)
	print(texte)
	
elif (décodage):  # pour décoder un texte
    décode = input("Quel est le texte à décoder ? ")
# message encrypté avec des nombres et/ou des caractères spéciaux
    specials = re.search("\d", décode)
    if (specials):
        if len(list(décryptage)) % 2 == 0:
            texte = alphabet(décode)
            print(texte)
 #      elif (morse):
