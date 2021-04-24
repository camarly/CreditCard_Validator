
# March 2021
# Author: Camarly Thomas
# Programming Techniques-UCC, PT103
# Individual Assignment #2

#GUI Application.
#You are required to create a GUI application for assignment #2 using colours, entry boxes and buttons.




import tkinter
import time
from tkinter import LEFT,W,E,S,N
from tkinter import messagebox,StringVar,END


# Create object splash screen on startup
splash_root = tkinter.Tk() 
splash_root.title("Welcome Screen")

bg = tkinter.PhotoImage(file="assets/img/bg.png")

# Adjust size 
splash_root.geometry("450x600")
  
# Set Label
splash_label = tkinter.Label(splash_root,text="Splash Screen",font=18, image=bg)
splash_label.pack()



#define functions

def main():  
    # destory splash window
    splash_root.destroy()
  
    #clearing the entry field 
    def clearScr():
        entry.delete(0, END)
        return None
        
    def cardNOT():
        response = messagebox.showinfo(title="No Matching Selection", message="Error 141: Credit Card selection and number do not match.")
        display['text'] = "Error 999: Invalid! - No Matching Selection"
        tkinter.Label(output_frame, text=response).grid()
        return None


    def warning():
        #response = messagebox.showwarning(title="Invalid", message="Error 007: The credit card number provided is invalid.")
        #root1.title("Invalid")
        display['text'] = ("INVALID: The credit card number: " + str(entry.get())+ " is invalid.")
        return None


    def NoEntry():
        #add isdigit() check
        #response = messagebox.showinfo(title="No input!", message="You must enter a card number between 13 - 16 digits!")
#         if entry.get() =='' or len(entry.get()) == '' or len(entry.get()) > 16 or len(entry.get()) < 13:
#             response = messagebox.showinfo(title="No input!", message="You must enter a card number between 13 - 16 digits!")
        display['text'] = "You must enter a card number between 13 - 16 digits!"
        response = messagebox.showinfo(title="No Matching Selection", message="Error 141: Credit Card selection and number do not match.")
        return None

    def cancel():
        status=messagebox.askyesno(title='Question', message="Are you sure you want to close this application?")
        if status == True:
            window.destroy()
        else:
            messagebox.showwarning(title='information',message="You will be returned to the mainwidnow.")
        return None
    
    #checking user entry
    def check():
        text = entry.get()
        while len(text) == 0:
            display['text']= ("Error 311: The Credit Card number field cannot be empty!")
            break
        else:
            if selection.get() == 'Visa Card' and text[0] == '4':
                luhn()
            elif selection.get() == 'Mastercard' and text[0] == '5':
                luhn()
            elif selection.get() == 'Discover Card' and text[0] == '6':
                luhn()
            elif selection.get() == 'American Express' and (text[0] == '3' and text[1] == '7'):
                luhn()
            elif selection.get() == "":
                display['text']= ("Error 104: You must select a cardtype!")
            elif selection.get() == False and len(text) != 0:
                display['text']= ("Error 307: Invalid inputs")
            else:
                display['text']= ("Error 301: Invalid Card type and Number.")
        return None

    #the luhn check method to validate card
    def luhn():
        digitsEven = []
        digitsOdd = []
        text = list(entry.get())
        new_text = text[-2::-2]
        for index,number in reversed(list(enumerate(new_text))):
            cardNumEven = int(number) *  2
            if int(number) * 2 >= 10:
                cardNumEven = (int(number) *  2) - 9
            digitsEven.append(cardNumEven)
        sum1 = sum(digitsEven)

        new_textOdd = text[-1::-2]
        for index,number in reversed(list(enumerate(new_textOdd))):
            cardNumOdd = int(number)
            digitsOdd.append(cardNumOdd)
        sum2 = sum(digitsOdd)
                
        digitsSum = sum1 + sum2

        if (((digitsSum % 10) == 0) and (digitsSum != 0)):
                display['text']= ("SUCCESS: The credit card number: " + str(entry.get())+ " is valid.")
                response = messagebox.showinfo(title="SUCCESS!", message="SUCCESS.")
        else:
            warning()

        return

    
    #creating the gui window
    window=tkinter.Tk()
    window.title("Credit Card Checker v1.0")
    window.geometry('450x600')
    window.resizable(0,0)
    window.iconbitmap(r"assets/img/cff.ico")
    window.configure(bg="#F5E6E8")

    #define colours
    colour1 = '#030b07'
    colour2 = '#3CB371'
    colour3 = '#00FF7F'
    colour4 = '#00FF00'
    colour6 = '#d6ecd2'

    #define images
    photo = tkinter.PhotoImage(file = "assets/img/visa.png")
    photo1 = tkinter.PhotoImage(file = "assets/img/mastercard.png")
    photo2 = tkinter.PhotoImage(file = "assets/img/ae.png")
    photo3 = tkinter.PhotoImage(file = "assets/img/discover.png")
    photo4 = tkinter.PhotoImage(file = "assets/img/check.png")
    photo5 = tkinter.PhotoImage(file = "assets/img/cancel.png")

    #define globals
    digitsEven = []
    digitsOdd = []

    selection = StringVar()
    selection.set(0)
    
    
    #define layout
    head_frame = tkinter.LabelFrame(window, borderwidth=2,text='Disclaimer', bg="#F5E6E8")
    head_frame2 = tkinter.Frame(head_frame, borderwidth=2, bg="#F5E6E8")
    card_frame = tkinter.LabelFrame(window, text='Select your Credit Card', bg="#F5E6E8")
    entry_frame = tkinter.Frame(window, borderwidth=2, relief='ridge', bg="#F5E6E8")
    output_frame = tkinter.Frame(window, borderwidth=2, relief='solid', bg="#F5E6E8")
    action_frame = tkinter.Frame(window, borderwidth=2, relief='ridge', bg="#F5E6E8")

    o_frame = tkinter.Frame(card_frame, borderwidth=2, bg="#F5E6E8")
    t_frame = tkinter.Frame(card_frame, borderwidth=2, bg="#F5E6E8")
    th_frame = tkinter.Frame(card_frame, borderwidth=2, bg="#F5E6E8")
    f_frame = tkinter.Frame(card_frame, borderwidth=2, bg="#F5E6E8")
    fi_frame = tkinter.Frame(card_frame, borderwidth=2, bg="#F5E6E8")

    head_frame.grid(row=0, column=0)
    head_frame2.grid(row=0, column=0)
    card_frame.grid(row=1, column=0)
    action_frame.grid(row=9, column=0)
    entry_frame.grid(row=7, column=0)
    output_frame.grid(row=10, column=0)

    o_frame.grid(row=3, column=0)
    t_frame.grid(row=4, column=0)
    th_frame.grid(row=5, column=1)
    f_frame.grid(row=4, column=1)
    fi_frame.grid(row=5, column=0)


    ccright = tkinter.Label(head_frame2,text="Copyright © 2021 Camarly Thomas. All rights reserved.\nI do not own or claim to own any of the images used in this application. \nImages were taken from freeicons.org & https://www.pexels.com.\nUnder the Fair Use guidelines of Section 107 of the Copyright and Fair Usage Act.\nFor the purpose of education, research, testing and commenting.\nAll images used have rights reserved to the image copyright owners.", justify=LEFT, font=('Helvetica', 12), bg="#A1FCDF")
    ccright.grid(row=0, column=0, sticky=W+E+N+S)

    #labels
    label2 = tkinter.Label(entry_frame, text="Enter Credit Card Number Below", bg="#F5E6E8")

    #buttons
    button1 = tkinter.Radiobutton(t_frame, text='Visa', image=photo, variable=selection, value='Visa Card', bg="#F5E6E8")
    button2 = tkinter.Radiobutton(th_frame, text='Mastercard' , image=photo1, variable=selection, value='Mastercard', bg="#F5E6E8")
    button3 = tkinter.Radiobutton(f_frame, text='Amex', image=photo2, variable=selection, value='American Express', bg="#F5E6E8")
    button4 = tkinter.Radiobutton(fi_frame, text='Discover', image=photo3, variable=selection, value='Discover Card', bg="#F5E6E8")

    button5 = tkinter.Button(action_frame, text='clear', command=clearScr, borderwidth=2, font=('Helvetica', 14), bg="#F5E6E8")
    button6 = tkinter.Button(action_frame, text='submit', command=check, borderwidth=2, font=('Helvetica', 14), bg="#F5E6E8")
    button7 = tkinter.Button(action_frame, text='exit', command=cancel, borderwidth=2, font=('Helvetica', 14), bg="#F5E6E8")

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=0)
    button3.grid(row=0, column=0)
    button4.grid(row=0, column=0)


    #Entry box
    entry = tkinter.Entry(entry_frame)
    label2.grid(row=8, column=0)
    entry.grid(row=9, column=0)

    #buttoncheckers
    button5.grid(row=11, column=0, padx=3, pady=3)
    button6.grid(row=11, column=1, padx=3, pady=3)
    button7.grid(row=11, column=2, padx=3, pady=3)


    #finals
    display = tkinter.Label(output_frame, text="Ready when you are!", image='', font=("Helvetica", 16))
    display.grid(row=0, column=0, columnspan=2, sticky="ew")
    
    #run main loop
    window.mainloop()

splash_root.after(1800,main)

tkinter.mainloop()


