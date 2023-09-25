''' 
Return a string that contains non turkish letters.
NewLines parameter is a list. You need to send a string list.
'''
def findNonTurkishLetters(NewLines: list) -> str: 
    alphabet = "abcçdefgğhıijklmnoöprsştuüvyz\n"
    removableChars = ""

    for line in NewLines:
        for char in alphabet:
            line = line.replace(char, "")
        if "" != line:
            if len(line) > 1:
                for _char in line:
                    if _char not in removableChars:
                        removableChars+=_char
            else:
                if line not in removableChars:
                    removableChars+=line
    return removableChars

''' 
Return a number of non Turkish Words.
NewLines parameter is a list. You need to send a string list.
'''
def getCountOfNonTurkishWords(NewLines: list) -> int:
    count = 0
    nonTurkishLetters = findNonTurkishLetters(NewLines)
    for line in NewLines:
        for letter in nonTurkishLetters:
            if letter in line:
                print(line)
                count = count + 1
                break
    return count

'''
Creating min 3 letter and no combined words (not including special words) .
Return a string list.
removeNonTurkishWords must be true or false.
'''

def createNewWordList(Lines: list) -> list:
    NewLines = []

    for line in Lines:
        newline = line.lstrip()
        newline = newline.rstrip()
        firstLetter = newline[0]
        if not firstLetter.isupper():
            if len(newline) >= 3:
                if " " not in newline:
                    newline += "\n"
                    NewLines.append(newline)
    return NewLines

def createNewWordListDeleteNonTurkishWords(Lines: list, nonTurkishLetters: str) -> list:
    NewLines = []
    print(nonTurkishLetters)
    for line in Lines:
        isTurkish = True
        for letter in nonTurkishLetters:
            if letter in line:
                isTurkish = False
                break
        if isTurkish == True:
            NewLines.append(line)
    return NewLines

''' --------- ------MAIN------- ---------'''

fileRead = open("original/turkce_kelime_listesi.txt", "r", encoding="utf-8")
fileWrite = open("new/turkce_kelime_listesi.txt", "w+", encoding="utf-8")

Lines = fileRead.readlines()
NewLines = createNewWordList(Lines)
''' IF YOU WANT TO USE ONLY 29 LETTER FOR TURKSIH WORD DONT ACTIVE BELLOW COMMENT LINES '''

'''
nonTurkishLetters = findNonTurkishLetters(NewLines)
print(f'{getCountOfNonTurkishWords(NewLines)} Non Turkish Word')
NewLines = createNewWordListDeleteNonTurkishWords(NewLines, nonTurkishLetters)
'''

fileWrite.writelines(NewLines)
fileRead.close()
fileWrite.close()


''' CREATE INDEX FILE TO SEARCH QUICKLY '''

''''''
