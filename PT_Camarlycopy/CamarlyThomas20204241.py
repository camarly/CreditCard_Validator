# Program created by Camarly Thomas April 2021.

# Programming Techniques - PT103 - UCC

# You are required to develop a menu program in python.
# As a bonus, you can implement this using a full or partial interactive graphical user interface(NOT REQUIRED).



#importing required libraries
import tkinter
from tkinter import StringVar, messagebox, END, IntVar
import random

#generates 16digit code used as ID for each user account.
import secrets
#This is needed for the file functions present in the code.
import os

from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText

#functions 
global helpMenu,donate,creditCardApp, gameApp

def helpMenu():
    tkinter.messagebox.showinfo('HELP', message="Register for an account, then login to access member's area!")

def donate():
    tkinter.messagebox.showinfo('Donate', message="You have donated - ABOSLUTELY NO REFUNDS!")
    return

def friendRequest():
    tkinter.messagebox.showwarning(message="NOBODY WANTS TO BE YOUR FRIEND RIGHT NOW!")
    return

def creditCardApp():
    creditCardBounty()
    return

def gameApp():
    gameBounty()
    return

def quitprogram():
    messagebox.showinfo("Exit", "program window will close")
    exit()

#details about the login platform
def aboutus():
    aboutWindow = tkinter.Tk()
    
    # specify size of window.
    aboutWindow.geometry("440x300")
      
    # Create text widget and specify size.
    aboutMessage = tkinter.Text(aboutWindow, height = 15, width = 280)
      
    # Create label and visuals
    label = tkinter.Label(aboutWindow, text = "About US")
    label.config(font =("Impact", 35, "italic"),fg="#6162FF", bg="white")
    aboutMessage.config(font =("Helvetica", 15, "italic"), bg="White", fg="#6162FF")
      
    label.pack()
    aboutMessage.pack()

      
    # Insert The Fact.
    aboutMessage.insert(tkinter.END, "\t\tMARKSMAN 1800\nA Secret-Service serving public Justice and World Peace.\nEstablished in 1788 by retired International Special OPS: Camarly Thomas GN, Q  C, QVV, BA, SN-ELITE.\nThe group works with; trains and provides SPECIAL OPS services to many nations.\nMEMBERSHIP is by INVITE ONLY.\nUpon successful completion of trials, a rifleman gets inducted into the MARKSMAN guild.\nAgents who DEFECT or go ROGUE are terminated.\n\bMARKSMAN is a Lifetime, Lifestyle and Family.\nMARKSMAN - Saving lives, One BOLT-AT-A-TIME."
)
      
    tkinter.mainloop()

######################################## GAMES-AREA ##############################################################################################

def gameBounty():
    # Create object
    splash_root = tkinter.Toplevel()
    splash_root.title("Game Window")

    bg = tkinter.PhotoImage(file="assets/img/sniper.png")
    game = tkinter.PhotoImage(file="assets/img/gamed.png")

    # Adjust size
    splash_root.geometry("1199x700+100+50")
    
    # Set Label
    splash_label = tkinter.Label(splash_root, text="Splash Screen", font=18, image=bg)

    splash_label.pack()

    def main():
        # destory splash window
        splash_root.destroy()
        tkinter.messagebox.showinfo("Console Game", "This is a console/command line game, please view and play game in the console/terminal/commandline! - Press OKAY to load game")
        hangman()

    #command line hangman game 
    def hangman():
        import random
        gameWindow = tkinter.Toplevel()
        gameWindow.title("Sniper's Hangman")
        gameWindow.geometry("1199x700+100+50")
        gameWindow.resizable(0, 0)
        gameWindow.configure(bg="#F5E6E8")


        tkinter.Label(gameWindow, text="This is a command line game. Please view game in command section to play", font=("Impact", 35, "italic"),fg="#6162FF", bg="white", bd=0).place(x=20, y=220, height=60, width=150)

        #load objectives so that the user has backstory about game
        with open('assets/words/objectives.txt', 'r') as objective:
            objectives = objective.readlines()
         
        objective = random.choice(objectives)
        print("\n")
        print(objective)
        print("\n")

        #load words as targets to use in game
        with open('assets/words/targets.txt', 'r') as target:
            words = target.readlines()

        word = random.choice(words)[:-1]
        attempts = []

        # number of incorrect attempts
        ammo = 2  # total bullet capacity for entire 3 level game
        shots = 2
        reload = 1  # given for successfully completing each round

        empty = False

        #display rules and spaces for hangman word on screen/console
        print("Type a character to guess the apprioriate word, character guesses count as shots from your Marksman Rifle.\n")
        print("Incorrect guesses are counted as missed shots\nCorrect guesses are hits and refill your ammo.\n")
        while not empty:
            for letter in word:
                if letter.lower() in attempts:
                    print(letter, end=" ")             
                else:
                    print("_", end=" ")
            print("\n")

            #store users guess
            guess = input(f"\n^---You have {ammo} bullets remaining, do not miss!---^ \n")
            
            attempts.append(guess.lower())

            if guess.lower() not in word.lower():
                ammo -= 1
                shots -=1
                print("You missed a shot!")
                if (shots == 0):
                    print("You missed the target, you were killed by enemy Marksman")
                    break
                if (ammo == 0):
                    print("You are are out of ammo, you were discovered and killed by enemy Marksman")
                    break
            else:
                ammo += 1
                shots += 1
                print("\n")
                print("\n..Reloading Weapon")
                print("\nyour ammunitions were replenished. Your have "+str(ammo) + " bullets remaining")

            empty = True
            for letter in word:
                if letter.lower() not in attempts:
                    empty = False
        #notification for status of game completion
        if empty:
            print("Mission Report:\nSTATE: CLASSIFIED\nSTATUS: TARGETS NEUTRALIZED")
            print("Closed Mission Target:" + word)
            #print("\nWould you like to go on another Mission?")
            choice = input("\nWould you like to go on another Mission?\n")
            if choice.lower() == "y" or choice.lower() == "yes":
                hangman()
            else:
                #destory window if user does not want to play again.
                gameWindow.destroy()
        
        else:
            print("Mission Report:\nSTATE: CLASSIFIED\nSTATUS: Agent M.I.A")
            print("Failed Mission Target:" + word)
            print("\nSELF-DESTRUCT SEQUENCE STARTED. Agent COMMUNICATION AND TRACKING TERMINATED.\n")
            gameWindow.destroy()


        gameWindow.mainloop()
    #hangman()
    splash_root.after(1800, main)
    tkinter.mainloop()
#gameBounty()


######################################## GAMES-AREA ##############################################################################################

######################################## Credit Card-AREA ##############################################################################################

def creditCardBounty():
    # March 2021
    # Author: Camarly Thomas
    # Programming Techniques-UCC, PT103
    # Individual Assignment #2

    # GUI Application.
    # You are required to create a GUI application for assignment #2 using colours, entry boxes and buttons.

    import tkinter
    import time
    from tkinter import LEFT, W, E, S, N
    from tkinter import messagebox, StringVar, END

    # Create object
    splash_root = tkinter.Toplevel()
    splash_root.title("Welcome Screen")

    bg = tkinter.PhotoImage(file="assets/img/bg.png")

    # Adjust size
    splash_root.geometry("450x600")

    # Set Label
    splash_label = tkinter.Label(splash_root, text="Splash Screen", font=18, image=bg)
    splash_label.pack()

    # define functions

    def main():
        # destory splash window
        splash_root.destroy()

        def clearScr():
            entry.delete(0, END)
            return None

        def cardNOT():
            response = messagebox.showinfo(title="No Matching Selection",
                                           message="Error 141: Credit Card selection and number do not match.")
            display['text'] = "Error 999: Invalid! - No Matching Selection"
            tkinter.Label(output_frame, text=response).grid()
            return None

        def warning():
            # response = messagebox.showwarning(title="Invalid", message="Error 007: The credit card number provided is invalid.")
            # root1.title("Invalid")
            display['text'] = ("INVALID: The credit card number: " + str(entry.get()) + " is invalid.")
            return None

        def NoEntry():
            # add isdigit() check
            # response = messagebox.showinfo(title="No input!", message="You must enter a card number between 13 - 16 digits!")
            #         if entry.get() =='' or len(entry.get()) == '' or len(entry.get()) > 16 or len(entry.get()) < 13:
            #             response = messagebox.showinfo(title="No input!", message="You must enter a card number between 13 - 16 digits!")
            display['text'] = "You must enter a card number between 13 - 16 digits!"
            response = messagebox.showinfo(title="No Matching Selection",
                                           message="Error 141: Credit Card selection and number do not match.")
            return None

        def cancel():
            status = messagebox.askyesno(title='Question', message="Are you sure you want to close this application?")
            if status == True:
                window.destroy()
            else:
                messagebox.showwarning(title='information', message="You will be returned to the mainwidnow.")
            return None

        def check():
            text = entry.get()
            while len(text) == 0:
                display['text'] = ("Error 311: The Credit Card number field cannot be empty!")
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
                    display['text'] = ("Error 104: You must select a cardtype!")
                elif selection.get() == False and len(text) != 0:
                    display['text'] = ("Error 307: Invalid inputs")
                else:
                    display['text'] = ("Error 301: Invalid Card type and Number.")
            return None
        
        #luhn algorithm to validate if a number is a valid credit card number 
        def luhn():
            digitsEven = []
            digitsOdd = []
            text = list(entry.get())
            new_text = text[-2::-2]
            for index, number in reversed(list(enumerate(new_text))):
                cardNumEven = int(number) * 2
                if int(number) * 2 >= 10:
                    cardNumEven = (int(number) * 2) - 9
                digitsEven.append(cardNumEven)
            sum1 = sum(digitsEven)

            new_textOdd = text[-1::-2]
            for index, number in reversed(list(enumerate(new_textOdd))):
                cardNumOdd = int(number)
                digitsOdd.append(cardNumOdd)
            sum2 = sum(digitsOdd)

            digitsSum = sum1 + sum2

            if (((digitsSum % 10) == 0) and (digitsSum != 0)):
                display['text'] = ("SUCCESS: The credit card number: " + str(entry.get()) + " is valid.")
                response = messagebox.showinfo(title="SUCCESS!", message="SUCCESS.")
            else:
                warning()

            return

        window = tkinter.Toplevel()
        window.title("Credit Card Checker v1.0")
        window.geometry('450x600')
        window.resizable(0, 0)
        window.iconbitmap(r"assets/img/cff.ico")
        window.configure(bg="#F5E6E8")

        # define colours
        colour1 = '#030b07'
        colour2 = '#3CB371'
        colour3 = '#00FF7F'
        colour4 = '#00FF00'
        colour6 = '#d6ecd2'

        # define images
        photo = tkinter.PhotoImage(file="assets/img/visa.png")
        photo1 = tkinter.PhotoImage(file="assets/img/mastercard.png")
        photo2 = tkinter.PhotoImage(file="assets/img/ae.png")
        photo3 = tkinter.PhotoImage(file="assets/img/discover.png")
        photo4 = tkinter.PhotoImage(file="assets/img/check.png")
        photo5 = tkinter.PhotoImage(file="assets/img/cancel.png")

        # define globals
        digitsEven = []
        digitsOdd = []

        selection = StringVar()
        selection.set(0)

        # define layout
        head_frame = tkinter.LabelFrame(window, borderwidth=2, text='Disclaimer', bg="#F5E6E8")
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

        ccright = tkinter.Label(head_frame2, text="Copyright © 2021 Camarly Thomas. All rights reserved.\nI do not own or claim to own any of the images used in this application. \nImages were taken from freeicons.org & https://www.pexels.com.\nUnder the Fair Use guidelines of Section 107 of the Copyright and Fair Usage Act.\nFor the purpose of education, research, testing and commenting.\nAll images used have rights reserved to the image copyright owners.", justify=LEFT, font=('Helvetica', 12), bg="#A1FCDF")
        ccright.grid(row=0, column=0, sticky=W + E + N + S)

        # labels
        label2 = tkinter.Label(entry_frame, text="Enter Credit Card Number Below", bg="#F5E6E8")

        # buttons
        button1 = tkinter.Radiobutton(t_frame, text='Visa', image=photo, variable=selection, value='Visa Card', bg="#F5E6E8")
        button2 = tkinter.Radiobutton(th_frame, text='Mastercard', image=photo1, variable=selection, value='Mastercard', bg="#F5E6E8")
        button3 = tkinter.Radiobutton(f_frame, text='Amex', image=photo2, variable=selection, value='American Express', bg="#F5E6E8")
        button4 = tkinter.Radiobutton(fi_frame, text='Discover', image=photo3, variable=selection, value='Discover Card', bg="#F5E6E8")

        button5 = tkinter.Button(action_frame, text='clear', command=clearScr, borderwidth=2, font=('Helvetica', 14), bg="#F5E6E8")
        button6 = tkinter.Button(action_frame, text='submit', command=check, borderwidth=2, font=('Helvetica', 14), bg="#F5E6E8")
        button7 = tkinter.Button(action_frame, text='exit', command=cancel, borderwidth=2, font=('Helvetica', 14), bg="#F5E6E8")

        button1.grid(row=0, column=0)
        button2.grid(row=0, column=0)
        button3.grid(row=0, column=0)
        button4.grid(row=0, column=0)

        # Entry box
        entry = tkinter.Entry(entry_frame)
        label2.grid(row=8, column=0)
        entry.grid(row=9, column=0)

        # buttoncheckers
        button5.grid(row=11, column=0, padx=3, pady=3)
        button6.grid(row=11, column=1, padx=3, pady=3)
        button7.grid(row=11, column=2, padx=3, pady=3)

        # finals
        display = tkinter.Label(output_frame, text="Ready when you are!", image='', font=("Helvetica", 16))
        display.grid(row=0, column=0, columnspan=2, sticky="ew")

        # run main loop
        window.mainloop()

    splash_root.after(1800, main)

    tkinter.mainloop()


# creditCardBounty()
######################################## Credit Card-AREA ##############################################################################################


######################################## MEMBERS-ARE A##################################################################################################

#This is the area to display after a registered user successfully logs into the sytem.
def membersArea():
    import tkinter
    from tkinter import StringVar, messagebox, END, IntVar, LEFT
    import random
    import secrets

    # window specififications
    # membersWindow = tkinter.Tk()
    membersWindow = tkinter.Toplevel()
    membersWindow.title("Marksman - Guild Lounge")
    membersWindow.geometry("1199x700+100+50")
    membersWindow.resizable(0, 0)


    def bounties():
        tkinter.messagebox.showwarning(message="Relax!, You are still in training!")
        return

    #help feature for users when they select the help button or use the file menu help option.
    def membersHelp():
        aboutWindow = tkinter.Tk()
        
        # specify size of window.
        aboutWindow.geometry("500x420")
          
        # Create text widget and specify size.
        aboutMessage = tkinter.Text(aboutWindow, height = 18, width = 300)
          
        # Create label and visuals.
        label = tkinter.Label(aboutWindow, text = "HELP")
        label.config(font =("Impact", 35, "italic"),fg="#6162FF", bg="white")
        aboutMessage.config(font =("Helvetica", 13), bg="White", fg="#6162FF")
          
        label.pack()
        aboutMessage.pack()

          
        # Insert the about-us text.
        aboutMessage.insert(tkinter.END, "\t\tMARKSMAN 1800\nWELCOME TO MARKSMAN.\nRegister for an account by filling out the registration form, then proceed to login and access the members area. In the members area you have a profile section on the left, displaying the demographics provided during registration.\nTo access registered user content: .\n\t\t*You can either use the file menu option located at the top or,\n\t\t*click the buttons corresponding to the desired application or functions to launch.\nThere are three main functions in this program:.\n1. Game (This is a console/command line only game - There is no GUI).\n\t*This is a simple hangman game that registered users can play.\n2. The credit card application.\n\t*Here you can validate your credit card.\n3. A Donate button - registered users can make a donation to MARKSMAN."
    )
          
        tkinter.mainloop()

        

    #Details about the Marksman system - This function runs when the user selects the aboutus option or button.
    def aboutus():
        aboutWindow = tkinter.Tk()
        
        # specify size of window.
        aboutWindow.geometry("440x300")
          
        # Create text widget and specify size.
        aboutMessage = tkinter.Text(aboutWindow, height = 15, width = 280)
          
        # Create label and visuals.
        label = tkinter.Label(aboutWindow, text = "About US")
        label.config(font =("Impact", 35, "italic"),fg="#6162FF", bg="white")
        aboutMessage.config(font =("Helvetica", 15, "italic"), bg="White", fg="#6162FF")
          
        label.pack()
        aboutMessage.pack()

          
        # Insert the about-us text.
        aboutMessage.insert(tkinter.END, "\t\tMARKSMAN 1800\nA Secret-Service serving public Justice and World Peace.\nEstablished in 1788 by retired International Special OPS: Camarly Thomas GN, Q  C, QVV, BA, SN-ELITE.\nThe group works with; trains and provides SPECIAL OPS services to many nations.\nMEMBERSHIP is by INVITE ONLY.\nUpon successful completion of trials, a rifleman gets inducted into the MARKSMAN guild.\nAgents who DEFECT or go ROGUE are terminated.\n\bMARKSMAN is a Lifetime, Lifestyle and Family.\nMARKSMAN - Saving lives, One BOLT-AT-A-TIME."
    )
          
        tkinter.mainloop()



    #put logged in user demographic information on the second window so that the user can see it.
    def profileInfo():
        file = open(loginName, 'r')
        y = 150
        item = 0
        demographics = [ "NAME: ","EMAIL: ","PASSWORD: ","PHONE: ","GENDER: " ,"ADDRESS: " , "MEMBERSHIP: ", "USERNAME: ", "MARKSMANID: "]
        for line in file:
            detail = tkinter.Label(profile, text=demographics[item] + line + "\n", font=("Tahoma", 14, "bold"), fg="#6162FF", bg="white").place(
                x=90, y=y + 10, height=80, width=250, anchor='w')
            y += 40
            item+=1
            
    global helpMenu,donate,creditCardApp, gameApp
    

    def donate():
        tkinter.messagebox.showinfo('Donate', message="You have donated - ABOSLUTELY NO REFUNDS!")
        return

    def friendRequest():
        tkinter.messagebox.showwarning(message="NOBODY WANTS TO BE YOUR FRIEND RIGHT NOW!")
        return

    def creditCardApp():
        creditCardBounty()
        return

    def gameApp():
        gameBounty()
        return


    #menu file option available at login and member windows. Users should be able to use these options to launch game or credit card application.
    menubar = tkinter.Menu(membersWindow, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
    file = tkinter.Menu(menubar, tearoff=1, background='#ffcc99', foreground='black')
    file.add_command(label="New")
    file.add_command(label="Open")
    file.add_command(label="Save")
    file.add_command(label="Save as")
    file.add_separator()
    file.add_command(label="Exit", command=quitprogram)
    menubar.add_cascade(label="File", menu=file)

    options = tkinter.Menu(menubar, tearoff=1, background='#ffcc99', foreground='black')
    options.add_command(label="Game", command=gameApp)
    options.add_command(label="Credit Card Check", command=creditCardApp)
    options.add_command(label="Bounties", command=bounties)
    options.add_command(label="Donate", command=donate)
    options.add_separator()
    options.add_command(label="Exit", command=quitprogram)
    menubar.add_cascade(label="Options", menu=options)

    edit = tkinter.Menu(menubar, tearoff=0)
    edit.add_command(label="Undo")
    edit.add_separator()
    edit.add_command(label="Cut")
    edit.add_command(label="Copy")
    edit.add_command(label="Paste")
    menubar.add_cascade(label="Edit", menu=edit)

    help = tkinter.Menu(menubar, tearoff=0)
    help.add_command(label="About", command=aboutus)
    help.add_command(label="Help", command=membersHelp)
    menubar.add_cascade(label="Help", menu=help)

    # display menubar
    membersWindow.config(menu=menubar)

    # images
    global gbgg
    gbgg = tkinter.PhotoImage(file="assets/img/gbgg.png")
    donateimg = tkinter.PhotoImage(file="assets/img/donate.png")
    game = tkinter.PhotoImage(file="assets/img/gamed.png")
    creditcardgame = tkinter.PhotoImage(file="assets/img/ccgame.png")



    # FRAMES
    # Welcome Frame
    welcomepage = tkinter.Frame(membersWindow, bg="white")
    welcomepage.place(x=0, y=30, width=1200, height=120)

    # LABELS
    welcomelabel = tkinter.Label(welcomepage, text="Welcome  " + loginName + "\nCheck out the Bounty Board for JOBS", font=("Impact", 22, "bold"), fg="#6162FF", bg="white")
    welcomelabel.place(x=220, y=30, width=700)

    # BUTTONS
    # about = tkinter.Button(welcomepage, text="ABOUT US", command=aboutus, font=("Impact", 15, "bold"), bd=0,highlightbackground="#6162FF",bg="#6162FF", fg="white").place(x=0, y=0, anchor='nw')

    # FRAMES
    # profile Frame
    profile = tkinter.Frame(membersWindow, bg="white")
    profile.place(x=0, y=150, width=370, height=600)

    # Display Profile info
    tkinter.Label(profile, text="AGENT PROFILE", font=("IMPACT", 35, "bold"), fg="#6162FF", bg="white").place(x=90, y=0,
                                                                                                        height=80,
                                                                                                        width=300)
    #tkinter.Label(profile).place(x=90, y=100, height=80, width=240, anchor='w')
    profileInfo()

    # BountBOARD - displays options available to user such as game, credit card and a donate button.
    # Frame
    bountyB = tkinter.Frame(membersWindow)
    bountyB.place(x=500, y=150, width=700, height=600)

    # LABELS &BUTTONS
    #buttonLabels to play game
    job1 = tkinter.Label(bountyB, text="BOUNTIES - Select ONE", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=80, y=20)
    tkinter.Label(bountyB, text="Game", font=("Impact", 15, "bold"), fg="#6162FF", bg="white", bd=0).place(x=20, y=60)
    yolo = tkinter.Button(bountyB, text="Game", image=game, command=gameApp, font=("Impact", 15, "bold"), bd=0).place(x=40, y=80, height=140, width=300)
    
    #button to check credit card
    tkinter.Label(bountyB, text="Check Credit Card", font=("Impact", 15, "italic"),fg="#6162FF", bg="white", bd=0).place(x=20, y=220, height=60, width=150)
    yolo2 = tkinter.Button(bountyB, text="Credit Card Application", image=creditcardgame, command=creditCardApp, font=("Impact", 15, "bold"), bd=0,).place(x=40, y=260, height=100, width=340)

    #button to make a donation
    tkinter.Label(bountyB, text="Donate to MARKSMAN", font=("Impact", 15, "italic"),fg="#6162FF", bg="white", bd=0).place(x=10, y=360, height=50, width=150)
    yolo3 = tkinter.Button(bountyB, text="DONATE", command=donate, image=donateimg, font=("Impact", 15, "bold"), bd=0).place(x=20, y=390, height=70, width=280)

    helpMenu = tkinter.Button(bountyB, text="HELP", command=membersHelp, font=("Impact", 15, "bold"), bd=0, highlightbackground="#6162FF", bg="#6162FF", fg="white").place(x=300, y=390, height=70, width=90)

    # helpReg = tkinter.Button(bountyB, text="HELP",command=helpMenu, font=("Impact", 15, "bold"), bd=0, highlightbackground="#6162FF", fg="white").place(x=290,y=390,height=40, width=180)

    membersWindow.mainloop()
    tkinter.mainloop()


# membersArea()

######################################## MEMBERS-AREA ##############################################################################################


def mainWindow():
    # Mainwindow
    # window specififications
    # menu = Menu(window)
    window = tkinter.Tk()
    window.title("Marksman - Demilitarised Zone")
    window.geometry("1199x700+100+50")
    window.resizable(0, 0)

    def aboutus():
        aboutWindow = tkinter.Tk()
        
        # specify size of window.
        aboutWindow.geometry("440x300")
          
        # Create text widget and specify size.
        aboutMessage = tkinter.Text(aboutWindow, height = 15, width = 280)
          
        # Create label and visuals
        label = tkinter.Label(aboutWindow, text = "About US")
        label.config(font =("Impact", 35, "italic"),fg="#6162FF", bg="white")
        aboutMessage.config(font =("Helvetica", 15, "italic"), bg="White", fg="#6162FF")
          
        label.pack()
        aboutMessage.pack()

          
        # Insert The about us message.
        aboutMessage.insert(tkinter.END, "\t\tMARKSMAN 1800\nA Secret-Service serving public Justice and World Peace.\nEstablished in 1788 by retired International Special OPS: Camarly Thomas GN, Q  C, QVV, BA, SN-ELITE.\nThe group works with; trains and provides SPECIAL OPS services to many nations.\nMEMBERSHIP is by INVITE ONLY.\nUpon successful completion of trials, a rifleman gets inducted into the MARKSMAN guild.\nAgents who DEFECT or go ROGUE are terminated.\n\bMARKSMAN is a Lifetime, Lifestyle and Family.\nMARKSMAN - Saving lives, One BOLT-AT-A-TIME."
    )
          
        tkinter.mainloop()
    
    #menu bar     
    menubar = tkinter.Menu(window, background='#ff8000', foreground='black', activebackground='white',
                           activeforeground='black')
    file = tkinter.Menu(menubar, tearoff=1, background='#ffcc99', foreground='black')
    file.add_command(label="New")
    file.add_command(label="Open")
    file.add_command(label="Save")
    file.add_command(label="Save as")
    file.add_separator()
    file.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=file)

    edit = tkinter.Menu(menubar, tearoff=0)
    edit.add_command(label="Undo")
    edit.add_separator()
    edit.add_command(label="Cut")
    edit.add_command(label="Copy")
    edit.add_command(label="Paste")
    menubar.add_cascade(label="Edit", menu=edit)

    help = tkinter.Menu(menubar, tearoff=0)
    help.add_command(label="About", command=aboutus)
    menubar.add_cascade(label="Help", menu=help)

    # display menubar
    window.config(menu=menubar)

    # background images
    # windowbg = PhotoImage()

    # variables
    nameValue = StringVar()
    emailValue = StringVar()
    usernameValue = StringVar()
    passwordValue = StringVar()
    confirmedPass = StringVar()
    genderValue = StringVar()
    membershipValue = StringVar()
    addressValue = StringVar()
    phoneValue = IntVar()
    genderValue.set(0)
    membershipValue.set(0)

    # Functions for login verification
    def loginWindow():
        pass
    

    def OpenFile():
        name = askopenfilename()
        print(name)

    def failToAuthenticate():
        attempt = 2
        if attempt < 3:
            tkinter.messagebox.showerror('Authentication Error! Marksman Password Not Recognized',
                                         'Marksman Password Not Recognized\nFinal attempt remaining!')
            attempt += attempt
        else:
            tkinter.messagebox.showerror('Authentication Error! Marksman Password Not Recognized',
                                         'Marksman Password Not Recognized\nProgram Terminated!')
            mainWindow.destroy()

    def noMarksman():
        tkinter.messagebox.showerror('Security Alert!\n',
                                     "Marksman Not Found - Your location has been sent to the Marksman database.\nYou will be tracked and monitored!")

    def loginSuccess():
        tkinter.messagebox.showinfo(message="Agent ID verified. Login Successful")
        window.withdraw()
        membersArea()



    def clearScr():
        usernameRegEnt.delete(0, END)
        passwordRegEnt.delete(0, END)
        confirmedPassRegEnt.delete(0, END)
        emailRegEnt.delete(0, END)
        phoneRegEnt.delete(0, END)
        addressRegEnt.delete(0, END)
        nameRegEnt.delete(0, END)
        # entry.delete(0, END)

    def genIdNo():
        idNo = secrets.token_hex(8)
        return idNo

    idNo = genIdNo()

    global username
    #registering the user and saving their details
    def registerAgent():
        global username
        global password
        try:
            fullName = str(nameValue.get())
            email = str(emailValue.get())
            username = str(usernameValue.get())
            password = str(passwordValue.get())
            gender = str(genderValue.get())
            membership = str(membershipValue.get())
            address = str(addressValue.get())
            phone = str(phoneValue.get())
            idNo = str(genIdNo())

            file = open(username, "w")
            # file.write("Name: " + fullName + "\n")
            # file.write("Email: " + email + "\n")
            # file.write("Password: " + password + "\n")
            # file.write("Phone: " + phone + "\n")
            # file.write("Gender: " + gender + "\n")
            # file.write("Country: " + country + "\n")
            # file.write("Membership: " + membership + "\n")
            # file.write("username: " + username + "\n")
            # file.write("MarksmanID: " + idNo + "\n")
            file.write(fullName + "\n")
            file.write(email + "\n")
            file.write(password + "\n")
            file.write(phone + "\n")
            file.write(gender + "\n")
            file.write(address + "\n")
            file.write(membership + "\n")
            file.write(username + "\n")
            file.write(idNo + "\n")
            file.close()

            tkinter.messagebox.showinfo('Registration Successful', 'Registration Successful')
            clearScr()
        except FileNotFoundError:
            tkinter.messagebox.showerror('Registration', 'No Field Should Be Empty')
        return True

    def aboutus():
        aboutWindow = tkinter.Tk()
        
        # specify size of window.
        aboutWindow.geometry("440x300")
          
        # Create text widget and specify size.
        aboutMessage = tkinter.Text(aboutWindow, height = 15, width = 280)
          
        # Create label and visuals
        label = tkinter.Label(aboutWindow, text = "About US")
        label.config(font =("Impact", 35, "italic"),fg="#6162FF", bg="white")
        aboutMessage.config(font =("Helvetica", 15, "italic"), bg="White", fg="#6162FF")
          
        label.pack()
        aboutMessage.pack()

          
        # Insert The Fact.
        aboutMessage.insert(tkinter.END, "\t\tMARKSMAN 1800\nA Secret-Service serving public Justice and World Peace.\nEstablished in 1788 by retired International Special OPS: Camarly Thomas GN, Q  C, QVV, BA, SN-ELITE.\nThe group works with; trains and provides SPECIAL OPS services to many nations.\nMEMBERSHIP is by INVITE ONLY.\nUpon successful completion of trials, a rifleman gets inducted into the MARKSMAN guild.\nAgents who DEFECT or go ROGUE are terminated.\n\bMARKSMAN is a Lifetime, Lifestyle and Family.\nMARKSMAN - Saving lives, One BOLT-AT-A-TIME."
    )
          
        tkinter.mainloop()

    #reset user password option    
    def resetPassword():
        try:
            username = str(usernameValue.get())
            password = str(passwordValue.get())

            file = open(username, "w")
            for lines in username:
                file.write("Password: " + password + "\n")
                file.close()

                tkinter.messagebox.showinfo('Password Change Successful', 'Password Change Successful')
                clearScr()
        except FileNotFoundError:
            tkinter.messagebox.showerror('Marksman not found', 'Marksman Agent not found')
        return True

    def maleFemale():
        pass

    def male():
        pass

    def female():
        pass

    def rifle():
        pass

    def sniper():
        pass

    def boltAction():
        pass
    
    #getting registration details from new user 
    def memberAdd():
        database = os.listdir()
    
        if usernameValue.get() == "":
            messagebox.showinfo(message='Username is required')
        elif usernameValue.get() in database:
            messagebox.showinfo(message='Threat Attempt Detected: Marksman Account already exist!')        
        elif nameValue.get() == "":
            messagebox.showinfo(message='Name is required')
        elif (phoneValue.get()) == "":
            messagebox.showinfo(message='Phone Number is required')
        elif len(str(phoneValue.get())) != 10:
            messagebox.showinfo(message='Phone Number must be 10 digits')
        elif emailValue.get() == "":
            messagebox.showinfo(message='Email Address is required')
        elif emailValue.get() == "":
            messagebox.showinfo(message='Email Address is valid')
        elif addressValue.get() == "":
            messagebox.showinfo(message='Address is required')
        elif genderValue.get() == "":
            messagebox.showinfo(message='Gender is required')
        elif passwordValue.get() == "":
            messagebox.showinfo(message='Password is required')
        elif confirmedPass.get() == "":
            messagebox.showinfo(message='Password is required')
        elif membershipValue.get() == "":
            messagebox.showinfo(message='Membership is required')
        elif passwordValue.get() != confirmedPass.get():
            messagebox.showinfo(message='Membership is required')
        else:
            registerAgent()
            messagebox.showwarning(message="New Agent Registered, your ID number is: " + idNo)

    def verifyLogin():
        global loginName
        loginName = userNameEN.get()
        loginPassword = passWordEN.get()

        userNameEN.delete(0, END)
        passWordEN.delete(0, END)
        
        #check all files in the directory for a file with the name that matches the one entered in the username login field.
        allFilesInDirectory = os.listdir()

        if loginName in allFilesInDirectory:
            userFile = open(loginName, "r")
            verifyLinesInFiles = userFile.read().splitlines()
            if loginPassword in verifyLinesInFiles:
                loginSuccess()
            else:
                failToAuthenticate()
        else:
            noMarksman()


    ####################################################################################################
    # FRAMES
    # Welcome Frame
    welcomepage = tkinter.Frame(window, bg="white")
    welcomepage.place(x=0, y=30, width=1200, height=120)

    """ Menu Bar - Displaying options available to user"""

    # LABELS
    welcomelabel = tkinter.Label(welcomepage,
                                 text="Welcome to MARKSMAN. \n Login with your MID or Register for Access to Marksman !",
                                 font=("Impact", 22, "bold"), fg="#6162FF", bg="white")
    welcomelabel.place(x=220, y=30, width=700)

    # ENTRIES

    # BUTTONS
    # about = tkinter.Button(welcomepage, text="ABOUT US", command=aboutus, font=("Impact", 15, "bold"), bd=0, highlightbackground="#6162FF", fg="white").place(x=0,y=0, anchor='nw')

    ####################################################################################################

    ####################################################################################################
    # FRAMES
    # Login Frame
    login = tkinter.Frame(window, bg="white")
    login.place(x=0, y=150, width=700, height=600)

    # LABELS
    loginlabel = tkinter.Label(login, text="LOGIN", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90,
                                                                                                                 y=30)
    onlyPatreons = tkinter.Label(login, text="MARKSMAN ONLY!", font=("Tahoma", 16, "bold"), fg="#1d1d1d",
                                 bg="white").place(x=90, y=90)
    userNameLabel = tkinter.Label(login, text="USERNAME", font=("Trebuchet", 15, "bold"), fg="#6162FF",
                                  bg="white").place(x=90, y=130)
    passWordLabel = tkinter.Label(login, text="PASSWORD", font=("Trebuchet", 15, "bold"), fg="#6162FF",
                                  bg="white").place(x=90, y=200)

    # ENTRIES
    userNameEN = tkinter.Entry(login, fg="#6162FF", bg="#E7E6E6")
    userNameEN.place(x=90, y=150, height=35, width=320)
    passWordEN = tkinter.Entry(login, fg="#6162FF", bg="#E7E6E6")
    passWordEN.place(x=90, y=220, height=35, width=320)

    # BUTTONS
    submit = tkinter.Button(login, text="SUBMIT", command=verifyLogin, font=("Impact", 15, "bold"), bd=0,
                            highlightbackground="#6162FF", bg="#6162FF", fg="white").place(x=90, y=260, height=40, width=80)
    forgetPassB = tkinter.Button(login, text="RESET PASSWORD", command=resetPassword, font=("Impact", 15, "bold"), bd=0,
                                 highlightbackground="#6162FF", bg="#6162FF", fg="white").place(x=190, y=260, height=40, width=130)

    ######################################################################################################

    # FRAMES
    # Registration Frame
    register = tkinter.Frame(window, bg="white")
    register.place(x=500, y=150, width=700, height=600)

    # LABELS and entry boxes for user registering.
    registerlabel = tkinter.Label(register, text="CREATE AN ACCOUNT", font=("Impact", 35, "bold"), fg="#6162FF",
                                  bg="white").place(x=90, y=30)
    onlyMarksman = tkinter.Label(register, text="Create your MARKSMAN Member Account", font=("Tahoma", 16, "bold"),
                                 fg="#1d1d1d", bg="white").place(x=90, y=90)
    nameReg = tkinter.Label(register, text="FULL NAME", font=("Trebuchet", 15, "bold"), fg="#6162FF", bg="white").place(
        x=90, y=130)
    nameRegEnt = tkinter.Entry(register, textvariable=nameValue, fg="#6162FF", bg="#E7E6E6")
    nameRegEnt.place(x=230, y=120, height=35, width=320)

    usernameReg = tkinter.Label(register, text="USERNAME", font=("Trebuchet", 15, "bold"), fg="#6162FF",
                                bg="white").place(x=90, y=165)
    usernameRegEnt = tkinter.Entry(register, textvariable=usernameValue, fg="#6162FF", bg="#E7E6E6")
    usernameRegEnt.place(x=230, y=155, height=35, width=320)

    emailReg = tkinter.Label(register, text="EMAIL ADDRESS", font=("Trebuchet", 15, "bold"), fg="#6162FF",
                             bg="white").place(x=90, y=195)
    emailRegEnt = tkinter.Entry(register, textvariable=emailValue, fg="#6162FF", bg="#E7E6E6")
    emailRegEnt.place(x=230, y=190, height=35, width=320)

    phoneReg = tkinter.Label(register, text="PHONE#", font=("Trebuchet", 15, "bold"), fg="#6162FF", bg="white").place(
        x=90, y=230)
    phoneRegEnt = tkinter.Entry(register, textvariable=phoneValue, fg="#6162FF", bg="#E7E6E6")
    phoneRegEnt.place(x=230, y=225, height=35, width=320)

    passwordReg = tkinter.Label(register, text="PASSWORD", font=("Trebuchet", 15, "bold"), fg="#6162FF",
                                bg="white").place(x=90, y=260)
    confirmPassReg = tkinter.Label(register, text="CONFIRM", font=("Trebuchet", 15, "bold"), fg="#6161FF").place(x=90,
                                                                                                                 y=300)
    passwordRegEnt = tkinter.Entry(register, textvariable=passwordValue, fg="#6162FF", bg="#E7E6E6")
    passwordRegEnt.place(x=230, y=260, height=35, width=320)
    confirmedPassRegEnt = tkinter.Entry(register, textvariable=confirmedPass, fg="#6162FF", bg="#E7E6E6")
    confirmedPassRegEnt.place(x=230, y=295, height=35, width=320)

    genderReg = tkinter.Label(register, text="GENDER", font=("Trebuchet", 15, "bold"), fg="#6162FF", bg="white").place(
        x=90, y=340)
    genderRegEntM = tkinter.Radiobutton(register, variable=genderValue, command=male, text="Male", value="Male",
                                        fg="#6162FF", bg="white", bd=0)
    genderRegEntF = tkinter.Radiobutton(register, variable=genderValue, command=female, text="Female", value="Female",
                                        fg="#6162FF", bg="white", bd=0)
    genderRegEntN = tkinter.Radiobutton(register, variable=genderValue, command=maleFemale, text="Genderless",
                                        value="Genderless", fg="#6162FF", bg="white", bd=0)
    genderRegEntM.place(x=240, y=340)
    genderRegEntF.place(x=300, y=340)
    genderRegEntN.place(x=375, y=340)

    addressReg = tkinter.Label(register, text="ADDRESS", font=("Trebuchet", 15, "bold"), fg="#6162FF",
                               bg="white").place(x=90, y=390)
    addressRegEnt = tkinter.Entry(register, fg="#6162FF", bg="#E7E6E6", textvariable=addressValue, bd=0)
    addressRegEnt.place(x=230, y=380, height=35, width=320)

    membershipPlan = tkinter.Label(register, text="CHOOSE MEMBERSHIP", font=("Trebuchet", 15, "bold"), fg="#6162FF",
                                   bg="white").place(x=200, y=420)
    membershipPlanEnt1 = tkinter.Radiobutton(register, variable=membershipValue, command=rifle,
                                             text="Rifle - Freeloader", fg="#6162FF", value="Rifle - Freeloader",
                                             bg="white", bd=0)
    membershipPlanEnt1.place(x=90, y=450)
    membershipPlanEnt2 = tkinter.Radiobutton(register, variable=membershipValue, command=sniper,
                                             text="Sniper - €9.99/Year", fg="#6162FF", value="Sniper - €9.99/Year",
                                             bg="white", bd=0)
    membershipPlanEnt2.place(x=228, y=450)
    membershipPlanEnt3 = tkinter.Radiobutton(register, variable=membershipValue, command=boltAction,
                                             text="Bolt-Action - €99.99/Year", value="Bolt-Action - €99.99/Year",
                                             fg="#6162FF", bg="white", bd=0)
    membershipPlanEnt3.place(x=380, y=450)

    # ENTRIES

    # BUTTONS
    registerB = tkinter.Button(register, text="REGISTER", command=memberAdd, font=("Impact", 15, "bold"), bd=0,
                               highlightbackground="#6162FF", bg="#6162FF", fg="white").place(x=90, y=480, height=40, width=80)
    helpHelp = tkinter.Button(register, text="HELP", command=helpMenu, font=("Impact", 15, "bold"), bd=0,
                              highlightbackground="#6162FF", bg="#6162FF", fg="white").place(x=190, y=480, height=40, width=80)
    clearScreen = tkinter.Button(register, text="CLEAR", command=clearScr, font=("Impact", 15, "bold"), bd=0,
                                 highlightbackground="#6162FF", bg="#6162FF", fg="white").place(x=290, y=480, height=40, width=80)

    ########################################################################################################

    # SecondWINDOW
    # SECOND Window FRAMES
    # CREDITCARD
    # GAME

    # mainloop
    tkinter.mainloop()


mainWindow()
