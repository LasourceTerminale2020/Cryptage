import re

# enlever la ponctuation

def specials (texte) :
    texte=texte.lower()
    specials = list(re.findall("\W", texte))
    texte=list(texte)
    for loop in range (len(specials)) :
        rang=texte.index(specials[loop])
        texte.remove(texte[rang])
    return texte

def cryptage_cesar(texte, key):
    crypted_text = specials(texte)
    for loop in range(len(crypted_text)):
        crypted_text[loop] = chr(ord(crypted_text[loop]) + key)
        if (ord(crypted_text[loop]) > 122):
            crypted_text[loop] = chr(ord(crypted_text[loop]) % 122)
    texte = "".join(crypted_text)
    return texte

#déterminer le coefficient directeur et l'ordonnée à l'origine & enlever les caractères spéciaux
def fonction (key) :
    liste_key = list(key)
    premiers = "".join(liste_key[:2])
    derniers = "".join(liste_key[-2:])
    coeff = re.search("x$", premiers)  # cas de ax+b
    coeff_bis = re.search("x$", derniers)  # cas de b+ax
    crypted_text = specials(texte)
    if (coeff):  # ax+b
        coefficient = int(liste_key[0])
        ordonnee = int(liste_key[3])
    elif (coeff_bis):  # b+ax
        coefficient = int(liste_key[2])
        ordonnee = int(liste_key[0])
    else:
        print("Veuillez réessayer : )   (en relançant le programme) ")
        print("N'oubliez pas que les chiffres doivent être compris entre 0 et 9")
    return coefficient, ordonnee, crypted_text
              
def cryptage_affine(texte, key):
    coefficient, ordonnee, crypted_text = fonction(key)
    for loop in range(len(crypted_text)):
        crypted_text[loop] = chr(ord(crypted_text[loop]) * coefficient + ordonnee)
        if ord(crypted_text[loop]) > 122:
            crypted_text[loop] = chr(ord(crypted_text[loop]) % 122)
    texte = "".join(crypted_text)
    return texte

def cryptage_vigenere(texte, key):
    crypted_text = lower(specials(texte))
    key = list(key)
    a = 0
    for loop in range(len(crypted_text)):
        while a < len(key):  # première occurence de la clé. Disons que len(key)=3
            key[a] = ord(key[a])
            crypted_text[a] = chr(ord(crypted_text[a]) + key[a])
            a = a+1
            if ord(crypted_text[a]) > 122:
                crypted_text[a] = chr(ord(crypted_text[a]) % 122)
        # 4/3 il reste 1 ==> il nous faut la première lettre de la clé
        crypted_text[a] = chr(ord(crypted_text[a]) + key[a % len(key)])
        if ord(crypted_text[a]) > 122:
            crypted_text[a] = chr(ord(crypted_text[a])-122)
        a = a+1
    texte = "".join(crypted_text)
    return texte



rep = input("Voulez-vous encrypter ou décrypter un texte ? ")
cryptage = re.search(r"\Bncrypt\B", rep)
decodage = re.search(r"\Bécod\B", rep)

if (cryptage):  # pour encoder un texte
    code = input("Quelle sorte de codage voulez-vous utiliser ? ")
    Cesar = re.search(r"sar\b", code)
    Affine = re.search(r"ffine\b", code)
    Vigenere = re.search(r"\Bigen\B", code)
    if (Cesar):
        texte = input(
            "Quel texte voulez-vous encrypter ? /!\ pas de nombre s'il vous plaît : ) ")
        key = int(input("De combien voulez-vous décaler votre texte ? "))
        texte = cesar(texte, key)
        print(texte)
    elif (Affine):
        texte = input(
            "Quel texte voulez-vous encrypter ? /!\ pas de nombre s'il vous plaît : ) ")
        key = input(
            "Quelle est la fonction de cryptage secrète ? /!\ mettre sous la forme d'une fonction ENTRE 0 ET 9 !! ")
        texte = affine(texte, key)
        print(texte)
    elif (Vigenere):
        texte = input(
            "Quel texte voulez-vous encrypter ? /!\ pas de nombre s'il vous plaît : ) ")
        key = input("Quelle est la clé de cryptage secrète ? ")
        texte = vigenere(texte, key)
        print(texte)
    else:
        print("Nous n'avons pas de correspondance pour ce type d'encryptage. Vérifiez l'orthographe et le nom de l'encryptage que vous souhaitez : )")

elif (decodage):  # pour décoder un texte
    decode = input("Quel est le texte à décoder ? ")
    # message encrypté avec des nombres et/ou des caractères spéciaux
    specials = re.search("\d", decode)
    
    if not(specials):
        # Ce serait possible de faire un oui/non dans l'interface graphique
        type = input("Avez-vous la clé de décodage ? Oui/Non  ")
        oui = re.search("oui" or "Oui", type)
        non = re.search("non" or "Non", type)
        if (oui):
            key= input("Alors, quelle est la clé ???")
        elif (non):
            print("analyse")
            # ANALYSE FRÉQUENTIELLE
            # Force brute

else:
    print("Vérifiez l'orthographe des mots saisis")
    print("Saisissez bien des mots de la famile d'encodage, encryptage, décodage ou décryptage")
