def separation(text):
    samogloski = ('a', 'e', 'i', 'y', 'o', 'u')
    sylaby = []
    sylaba = ""
    slowo = text
    wyjatki = ("ch", "rz", "sz", "dz")
    inne = ("ą","ę","ć", "ś", "ż", "ź", "ń", "ó")
    for znak in slowo:
        if znak in samogloski:
            sylaba += znak
            sylaby.append(sylaba)
            sylaba = ""
        else:
            sylaba += znak
    for wyjatki in slowo:
        sylaba = znak
    
    return sylaby


if __name__ == '__main__':
    text = input()
    print(separation(text))