from tkinter import*
import random
window=Tk()
window.title("Guess Game")
window.geometry("600x400")
number = random.randint(0,100)
logoup = PhotoImage(file="upvote.png")
logodown = PhotoImage(file="downvote.png")
logobingo = PhotoImage(file="bingo.png")
logoup = logoup.subsample(2)
logodown = logodown.subsample(2)
logobingo = logobingo.subsample(2)

def restart():
    global number
    txt1.delete(0, END)
    lbl5.configure(image= "")
    number = random.randint(0,100)
    txt1.configure(state='normal')

def start(event):
    global guess, number, lbl5
    guess = txt1.get()
    lbl4.configure(text= "")
    if int(guess) == number :
        lbl5.configure(image= logobingo)
        txt1.delete(0, END)
        txt1.configure(state='disabled')
    elif int(guess) > 100:
        lbl5.configure(image=logodown)
        txt1.delete(0, END)
    elif int(guess) > number:
        lbl5.configure(image=logodown)
        txt1.delete(0, END)
    elif int(guess) < number:
        lbl5.configure(image=logoup)
        txt1.delete(0, END)







lbl1=Label(window,text="Guess the number",fg="#D1D4FF",bg="#7479C0",font=("Times New Roman",40),cursor="heart")
lbl1.grid(column= 0,columnspan=2, row=0, rowspan= 5)
lbl2=Label(window,text="Make guesses until you find the number I have thought of (0-100)", fg="#7479C0",font=("Times New Roman",20),cursor="heart")
lbl2.grid(column=0, columnspan=2, row=5 ,rowspan=2)
lbl3=Label(window,text=" I will be telling you if you need to go up or down",fg="#7479C0",font=("Times New Roman",20),cursor="heart")
lbl3.grid(column=0, columnspan=2,row=7, rowspan=2)
lbl4=Label(window,text="enter your guess here and press enter",fg="black",font=("Times New Roman",15),cursor="heart")
lbl4.grid(column=0, columnspan=2,row=9,  rowspan= 2)
txt1=Entry(window,fg="#D1D4FF",bg="#7479C0",cursor="heart",  font=("Times New Roman",25), width=5)
txt1.grid(column=0,  row=11,rowspan=2,pady=16)
lbl5=Label(window,text="",fg="#7479C0",cursor="heart",justify=CENTER)
lbl5.grid(column=1, row=11,rowspan=8, pady=16)
btn1=Button(window,text="Exit",fg="#7479C0",bg="#7479C0", font=("Times New Roman",30),  command=quit,cursor="heart")
btn1.grid(column=0, row=19)
btn2=Button(window,text="Restart",fg="#7479C0",bg="#7479C0", font=("Times New Roman",30), command= restart, cursor="heart")
btn2.grid(column=1,row=19, rowspan=2)

window.bind('<Return>', start)



window['cursor'] = "heart"
window.mainloop()