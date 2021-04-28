#Geoffrey McGlinn
#MAT320
#twelveTone GUI


#Importing python3 GUI
from tkinter import *
from tkinter import messagebox

#Module that handles all calculations
import controller


#Gathering data from GUI and running into imported module
def testButton():

    #"Prime" Tone Row
    original = [
                note0.get(),
                note1.get(),
                note2.get(),
                note3.get(),
                note4.get(),
                note5.get(),
                note6.get(),
                note7.get(),
                note8.get(),
                note9.get(),
                note10.get(),
                note11.get()
                ]
    #All other inputs handled within dictionary
    inputs = {
                'bpm' : optionBPM.get(),
                'time' : optionTime.get(),
                'v1' : violinOne.get(),
                'v2' : violinTwo.get(),
                'vla' : viola.get(),
                'cllo' : cello.get(),
                'title' : pieceName.get()
                }

    #Passing values into module function
    controller.master(original, **inputs)

    #Outputting an info box to the user notifying sheet music was created
    messagebox.showinfo(title="Notice",message="Lilypond Compatible File Created, run command 'lilypond " + inputs['title'] + ".ly'")



#Creating TKinter Window
root = Tk()
root.title('12 Tone Quartet')

#Possible tone row notes
notes = [
    "C ",
    "C#",
    "D ",
    "D#",
    "E ",
    "F ",
    "F#",
    "G ",
    "G#",
    "A ",
    "A#",
    "B "
]


#Variable Declarations
violinOne = IntVar()
violinTwo = IntVar()
viola = IntVar()
cello = IntVar()
optionBPM = StringVar()
optionTime = StringVar()

#Tone Row Variables, this could've been significantly shortened with a loop
#that I didn't get around to write
note0 = StringVar()
note1 = StringVar()
note2 = StringVar()
note3 = StringVar()
note4 = StringVar()
note5 = StringVar()
note6 = StringVar()
note7 = StringVar()
note8 = StringVar()
note9 = StringVar()
note10 = StringVar()
note11 = StringVar()

#Setting Default Values
optionBPM.set("Andante (84)")
optionTime.set("4/4")

#Tone Row Variables, also could have been shortened into 3 lines
note0.set(notes[0])
note1.set(notes[1])
note2.set(notes[2])
note3.set(notes[3])
note4.set(notes[4])
note5.set(notes[5])
note6.set(notes[6])
note7.set(notes[7])
note8.set(notes[8])
note9.set(notes[9])
note10.set(notes[10])
note11.set(notes[11])


#Placing GUI Frames
toneRow = Frame(height = 1, bd=1)
menu1 = Frame(height = 6, bd = 1)
menu2 = Frame(height = 1, bd = 1)


#Inserting into frames
titleLabel = Label(root, text = "Twelve-Tone Quartet")
nameLabel = Label(menu1, text = "Title of Piece: ")
bpmLabel = Label(menu1, text = "Piece Tempo: ")
timeLabel = Label(menu1, text = "Time Signature: ")
toneLabel = Label(menu1, text = "Original Tone Row:")

#Set of checkboxes
violinOneCheck = Checkbutton(menu1, text = "Violin 1", variable = violinOne)
violinTwoCheck = Checkbutton(menu1, text = "Violin 2", variable = violinTwo)
violaCheck = Checkbutton(menu1, text = "Viola", variable = viola)
celloCheck = Checkbutton(menu1, text = "Cello", variable = cello)

#Dropdown menus
bpm = OptionMenu(menu1, optionBPM, "Allegro (140)","Moderato (112)","Andante (84)","Adagio (72)","Largo (56)")
time = OptionMenu(menu1, optionTime, "4/4","3/4")

#Tone Rows
zero = OptionMenu(toneRow, note0, *notes)
one = OptionMenu(toneRow, note1, *notes)
two = OptionMenu(toneRow, note2, *notes)
three = OptionMenu(toneRow, note3, *notes)
four = OptionMenu(toneRow, note4, *notes)
five = OptionMenu(toneRow, note5, *notes)
six = OptionMenu(toneRow, note6, *notes)
seven = OptionMenu(toneRow, note7, *notes)
eight = OptionMenu(toneRow, note8, *notes)
nine = OptionMenu(toneRow, note9, *notes)
ten = OptionMenu(toneRow, note10, *notes)
eleven = OptionMenu(toneRow, note11, *notes)

#Additional insertion into frames
pieceName = Entry(menu1)
#pieceName.insert(0, "No Title")

finalizeButton = Button(menu2, text = "Generate Music", command=testButton)



#Root window placements
titleLabel.grid(row = 0, column = 0)
menu1.grid(row = 1, column = 0)
toneRow.grid(row = 2, column = 0)
menu2.grid(row = 3, column = 0)


#Menu 1 Placements
bpmLabel.grid(row = 2, column = 0)
timeLabel.grid(row = 3, column = 0)
nameLabel.grid(row = 4, column = 0)
toneLabel.grid(row = 5, column = 0)

pieceName.grid(row = 4, column = 1)

violinOneCheck.grid(row = 0, column = 0)
violinTwoCheck.grid(row = 0, column = 1)
violaCheck.grid(row = 1, column = 0)
celloCheck.grid(row = 1, column = 1)

bpm.grid(row = 2, column = 1)
time.grid(row = 3, column = 1)


#toneRow placements
zero.grid(row = 0, column = 0)
one.grid(row = 0, column = 1)
two.grid(row = 0, column = 2)
three.grid(row = 0, column = 3)
four.grid(row = 0, column = 4)
five.grid(row = 0, column = 5)
six.grid(row = 0, column = 6)
seven.grid(row = 0, column = 7)
eight.grid(row = 0, column = 8)
nine.grid(row = 0, column = 9)
ten.grid(row = 0, column = 10)
eleven.grid(row = 0, column = 11)



#Menu 2 Placements
finalizeButton.grid(row = 0, column = 0)

root.mainloop()
