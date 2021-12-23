#Ayesha Saiyed - Fairfax High School

from tkinter import *

def letter_grade(number_score):
    grade = ""
    if 92.5 <= number_score <= 100:
        grade = "A"
    elif 90<= number_score < 92.5:
        grade = "A-"
    elif 87<= number_score < 90:
        grade = "B+"
    elif 83<= number_score < 87:
        grade = "B"
    elif 80<= number_score < 83:
        grade = "B-"
    elif 77<= number_score < 80:
        grade = "C+"
    elif 73<= number_score < 77:
        grade = "C"
    elif 70<= number_score < 73:
        grade = "C-"
    elif 67<= number_score < 70:
        grade = "D+"
    elif 63<= number_score < 67:
        grade = "D"
    elif 60<= number_score < 63:
        grade = "D-"
    elif number_score < 60:
        grade = "F"
    return(grade)

root = Tk()
root.geometry("600x600")
root.title("Grade Calculator")
root['background'] = '#99ccff'

canvas = Canvas(root, width = 600, height = 110,highlightthickness = 0)
canvas.pack()
canvas['background'] = '#99ccff'

img = PhotoImage(file="clubLogo.png")
img = img.subsample(12, 12)
canvas.create_image(15, 10, anchor=NW, image=img)

img2 = PhotoImage(file="fhsLogo.png")
img2 = img2.subsample(3, 3)
canvas.create_image(450, 3, anchor=NW, image=img2)

img3 = PhotoImage(file="gradeLogo.png")
img3 = img3.subsample(3, 3)
canvas.create_image(380, 3, anchor=NE, image=img3)



title = Label(text = "Grade Calculator", font ='Futura 20 bold', bg = "#99ccff")
title.pack()

l0 = Label(text = "Class Name", font ='Helvetica 13 bold', bg = "#99ccff")
l0.pack()

e0 = Entry(root, width=20)
e0.pack()

l1 = Label(text = "Test Weight", font ='Helvetica 12 bold', bg = "#99ccff")
l1.pack()

e1 = Entry(root, width=20)
e1.pack()

l2 = Label(text = "HW Weight", font ='Helvetica 12 bold', bg = "#99ccff")
l2.pack()

e2 = Entry(root, width=20)
e2.pack()

l3 = Label(text = "Test Percentage", font ='Helvetica 12 bold', bg = "#99ccff")
l3.pack()

e3 = Entry(root, width=20)
e3.pack()

l4 = Label(text = "HW Percentage", font ='Helvetica 12 bold', bg = "#99ccff")
l4.pack()

e4 = Entry(root, width=20)
e4.pack()

def myClick():

    test = float(e3.get())
    testWeight = float(e1.get())
    homework = float(e4.get())
    hwWeight = float(e2.get())
    score = (test/100)*testWeight + (homework/100)*hwWeight

    #Grade weights must add up to 100
    #Test and homework scores can be greater than 100
    if testWeight + hwWeight != 100:
        output = "Make sure weights add up to 100"
        myLabel = Label(root, text=output,fg="red",bg = "#99ccff", font = "Helvetica 14 bold")
    elif test <0 or homework<0:
        output = "Scores cannot be less than 0"
        myLabel = Label(root, text=output, fg="red", bg="#99ccff", font="Helvetica 14 bold")
    else:
        output = e0.get() + " score is: " + str(score) + ", " + letter_grade(score)
        myLabel = Label(root, text=output)

    myLabel.pack()
    e0.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)


spacer = Label(text = "", bg = "#99ccff")
spacer.pack()

myButton0 = Button(root, text="Submit", command=myClick)
myButton0.pack()

spacer2 = Label(text = "", bg = "#99ccff")
spacer2.pack()

root.mainloop()