import random

from .fic_ressources import *

####################### QUEENIE
def word_remove(string):
    string = string.split()
    string.remove(random.choice(string))
    newstr = string[0]
    for bit in string:
        if bit != string[0]:
            newstr = newstr + " " + bit
    return newstr

def missingletter(string):
    i = 0
    j = random.randint(0, len(string))
    newstr = ""
    for letter in string:
        i += 1
        if i == j:
            continue
        else:
            newstr = newstr + letter
    return newstr

def toolate(string):
    newstr = ""
    i = 0
    length = len(string) - 1
    j = random.randint(0, length)
    k = random.randint(0, length)

    while k == j:
        k = random.randint(0, len(string))

    for letter in string:
        i = i + 1
        if i == j:
            letter = string[k]
            newstr = newstr + letter
        if i == k:
            letter = string[j]
            newstr = newstr + letter
        else:
            newstr = newstr + letter
    return newstr

def switchedletter(string):
    newstr = ""
    i = 0
    length = len(string) - 1
    j = random.randint(0, length)
    k = random.randint(0, length)
    if k == j:
        k = random.randint(0, length)

    for letter in string:
        if i == j:
            newstr = newstr + string[k]
        elif i == k:
            newstr = newstr + string[j]
        else:
            newstr = newstr + letter
        i = i + 1

    return newstr

def queenize(texte):
    chlist = ["manquemot", "missingletter", "switchedletter", "toolate"]
    final = ""
    listchoice = []

    nbchoice = random.randint(1, 2)
    length = len(texte)- 1
    length = int(length/3)

    if len(texte.split()) < 7:
        listchoice = ["missingletter", "switchedletter", "toolate"]
        if nbchoice == 1:
            i = random.randint(0, 2)
            listchoice = listchoice[i]
        elif nbchoice == 2:
           i = random.randint(0, 2)
           j = random.randint(0, 2)
           listchoice = [listchoice[i], listchoice[j]]

    elif len(texte) > 250:
        nb = int(len(texte)/63.0)
        i = 0
        while i < nb:
            listchoice.append(chlist[random.randint(0, 3)])
            i = i + 1

    else:
        listchoice = ["manquemot", "missingletter", "switchedletter", "toolate"]
        i = random.randint(0, 3)
        j = random.randint(0, 2)
        if nbchoice == 2:
            listchoice == listchoice.pop(i)
            listchoice == listchoice.pop(j)

        else:
            listchoice == listchoice.pop(i)

    if type(listchoice) == str:
        if listchoice == chlist[1]:
            final = missingletter(texte)
        elif listchoice == chlist[2]:
            final = switchedletter(texte)
        elif listchoice == chlist[3]:
            final = toolate(texte)
    else:
        final = texte
        for element in listchoice:
            if element == "manquemot":
                final = word_remove(final)
            if element == "missingletter":
                final = missingletter(final)
            if element == "switchedletter":
                final = switchedletter(final)
            if element == "toolate":
                final = toolate(final)
            final = final


    return final

################ FANFIC IT
def fanfic_it(text):
    text = text.split(",")
    genrenb = random.randint(1, 2)
    warning = random.randint(1, 3)
    clichenb = random.randint(1, 2)

    if genrenb == 1:
        genre_final = random.choice(genre)
    else:
        genre1 = random.choice(genre)
        genre2 = random.choice(genre)
        while genre1 == genre2:
            genre2 = random.choice(genre)
        genre_final = f"{genre1} et {genre2}"
    if clichenb == 1:
        cliche_fic = f"Elle contient l'archétype suivant : {random.choice(cliche)}"
    else:
        cliche_fic = "Elle ne contient aucun archétype particulier."

    if warning < 3:
        warning = "et ne nécessite aucun avertissement quant à son contenu."
    else:
        warning = f"et nécessite un avertissement pour le contenu suivant : {random.choice(warning)}"

    if len(text) == 2:
        pairingz = f"{text[0]} et {text[1].strip()}"
    else:
        pairingz = f"{text[0]}, {text[1].strip()} et {text[2].strip()}"

    result = f"""Mon algorythme a déterminé la fic optimale à écrire pour {pairingz} !
Elle est de genre {genre_final} {warning}.
{cliche_fic}
Sa longueur est {random.choice(longueur)}.
L'écrire{random.choice(whywrite)}."""

    return result