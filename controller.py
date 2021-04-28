#Geoffrey McGlinn
#MAT320
#twelveTone main

#importing necessary modules
import random


outputs = open("outputs.txt", "w")


#Randomly decides the order of randomization for tone rows
def randomizer(prime = [], *args):
    randval = random.randint(0, 5)
    toneRow = []
    if randval == 0:#Transposes up randint semitones from 1 to 11, converts to LY
        inpoot = {'k' : random.randint(1,11)}
        return convertToLY(transpose(prime, **inpoot))
    elif randval == 1:#Inverts prime and converts to LY format
        return convertToLY(invert(prime))
    elif randval == 2:#Retrogrades prime and converts to LY format
        return convertToLY(retrograde(prime))
    elif randval == 3:#cycliclly shifts prime and converts to LY format
        return convertToLY(cyclicShift(prime))
    elif randval == 4:#inverts and retrogrades prime, then converts to LY format
        return convertToLY(invertedRetrograde(prime))
    else:
        return convertToLY(prime)

#Transposes tones up by k semitones
def transpose(prime = [], *args, k):
    outputs.write("Transposed Up " + str(k) + " Semitones")
    transposed = prime
    count = 0
    while count < k:
        temp = transposed.pop()
        transposed.insert(0, temp)
        count += 1
    return transposed

#Inverts tones: "Flips" tones ie highest becomes lowest etc
def invert(prime = [], *args):
    outputs.write("Inverted ")
    convert = {
                'C ':'B ',
                'C#':'A#',
                'D ':'A ',
                'D#':'G#',
                'E ':'G ',
                'F ':'F#',
                'F#':'F ',
                'G ':'E ',
                'G#':'D#',
                'A ':'D ',
                'A#':'C#',
                'B ':'C '
                }
    inverted = []
    for i in prime:
        inverted.append(convert[i])
    return inverted


#Retrogrades tones ie: reverses order of tones
def retrograde(prime =[], *args):
    outputs.write("Retrograde")
    retrograded = [
                    prime[11],
                    prime[10],
                    prime[9],
                    prime[8],
                    prime[7],
                    prime[6],
                    prime[5],
                    prime[4],
                    prime[3],
                    prime[2],
                    prime[1],
                    prime[0]
                    ]
    return retrograded

#nth tone moves to n+1 spot, index 11 moves to index 0
def cyclicShift(prime = [], *args):
    outputs.write("Cyclic Shift")
    shifted = [
                prime[11],
                prime[0],
                prime[1],
                prime[2],
                prime[3],
                prime[4],
                prime[5],
                prime[6],
                prime[7],
                prime[8],
                prime[9],
                prime[10]
                ]
    return shifted

#It's a twoefer, does both retrograding and inverting of the tone rows
def invertedRetrograde(prime = [], *args):
    converted = retrograde(invert(prime))
    return converted


#Taking the user input and making it into a use-able string for lilypond
def bpmTrans(bpm):
    if bpm == "Allegro (140)":
        return "\"Allego\" 4 = 140"
    if bpm == "Moderato (112)":
        return "\"Moderato\" 4 = 112"
    if bpm == "Andante (84)":
        return "\"Andante\" 4 = 84"
    if bpm == "Adagio (72)":
        return "\"Adagio\" 4 = 72"
    if bpm == "Largo (56)":
        return "\"Largo\" 4 = 56"

#Changing from input style of "C " and "C#" to "C" and "Cis". This allows me
#to add position of tone now directly onto the end of each tone
def convertToLY(prime = [], *args):
    convert = {
                'C ':'c',
                'C#':'cis',
                'D ':'d',
                'D#':'dis',
                'E ':'e',
                'F ':'f',
                'F#':'fis',
                'G ':'g',
                'G#':'gis',
                'A ':'a',
                'A#':'ais',
                'B ':'b'
                }
    converted = []
    for i in prime:
        converted.append(convert[i])
    return converted

#Receives the original tone row, title of song to open file, and instrument type
def createInstr(prime = [], *args, title, instType, time):
    file = open(title + ".ly", "a")
    if instType == 0: #V1
        toneRange = ["''", "''"]
        header = "violinOne = \\new Voice { \\relative c''\n  \\set Staff.instrumentName = #\"Violin 1 \"\n\n  "

    elif instType == 1: #V2
        toneRange = ["'", "''"]
        header = "violinTwo = \\new Voice {\n  \\set Staff.instrumentName = #\"Violin 2 \"\n\n  "

    elif instType == 2: #Vla
        toneRange = ["", ""]
        header = "viola = \\new Voice {\n  \\set Staff.instrumentName = #\"Viola \"\n  \\clef alto\n\n  "

    elif instType == 3: #Cello
        toneRange = ["", ""]
        header = "cello = \\new Voice {\n  \\set Staff.instrumentName = #\"Cello \"\n  \\clef bass\n\n  "


    file.write(header)

    if time == "3/4":
        x = 3
    else:
        x = 4

    count = 0
    while count < 8:
        outputs.write("Tone row transformation #" + str(count) + "\n")
        randomized = randomizer(prime)
        outputs.write("\n This results in a transformed tone row of:\n")
        for i in randomized:
            outputs.write(i + " ")
        outputs.write("\n")
        while randomized:
            count2 = 0
            while count2 < x:
                toneRangeChooser = random.randint(0,1)
                toneRangeChoice = toneRange[toneRangeChooser]
#                if count2 == 0:
                file.write(randomized[0] + toneRangeChoice + " ")
#                else:
#                file.write(randomized[0] + " ")
                randomized.pop(0)
                count2 += 1
            file.write("\n  ")
        count += 1



    file.write("\n  \\bar \"|.\"\n}\n\n")


    file.close()


#Creates a 108 (9 iterations of the 12 note tone row) length note piece
def master(tones = [], *args, bpm, time, v1, v2, vla, cllo, title):
    outputs.write("MAT320 Discrete Math Final Project Outputs\n\nOriginal Input Tone Row:\n")
    for i in tones:
        outputs.write(i + " ")
    outputs.write("\n")
    #Creating file to be worked with on Lilypond
    file = open(title + ".ly", "w")
    #Header for Lilypond
    file.write("\\version \"2.18.2\"\n\\header {\n  title = \"" + title + "\"\n  composer = \"Geoff's Python Program\"\n}\n\nglobal= {\n  \\time " + time + "\n  \\key c \\major\n  \\tempo " + bpmTrans(bpm) + "\n}\n\n")
    file.close()
    score = "\\score {\n  \\new StaffGroup <<\n"
    if v1 == 1:
        input = {'title' : title, 'instType' : 0, 'time' : time}
        createInstr(tones, **input)
        score = score + "    \\new Staff << \\global \\violinOne >>\n"
    if v2 == 1:
        input = {'title' : title, 'instType' : 1, 'time' : time}
        createInstr(tones, **input)
        score = score + "    \\new Staff << \\global \\violinTwo >>\n"
    if vla == 1:
        input = {'title' : title, 'instType' : 2, 'time' : time}
        createInstr(tones, **input)
        score = score + "    \\new Staff << \\global \\viola >>\n"
    if cllo == 1:
        input = {'title' : title, 'instType' : 3, 'time' : time}
        createInstr(tones, **input)
        score = score + "    \\new Staff << \\global \\cello >>\n"

    file = open(title + ".ly", "a")
    file.write(score + "  >>\n  \\layout { }\n \n}")


    file.close()
    outputs.close()
