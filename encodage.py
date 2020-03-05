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

rep = input("Voulez-vous encrypter ou décoder un texte ? ")
cryptage = re.search(r"\Bncrypt\B", rep) or re.search(r"\Bncod\B", rep)
décodage = re.search(r"\Bécod\B", rep) or re.search(r"\Bécrypt\B", rep)

if (cryptage):  # pour encoder un texte
    codage = input("Quelle sorte de codage voulez-vous utiliser ? ")
    Carre = re.search(r"\Barr\B" and r"lphabet\b", codage)
    Morse = search("morse" or "Morse", codage)
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
    décryptage = input("Quel est le texte à décoder ? ")
# message encrypté avec des nombres et/ou des caractères spéciaux
    specials = re.search("\d", décryptage)
    if (specials):
        if len(list(décryptage)) % 2 == 0:
            texte = alphabet(décryptage)
            print(texte)
 #      elif (morse):
