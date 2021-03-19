from tkinter import *

import werewolf_run# this contains the pygame code
from PIL import Image,ImageTk #this is necessary for adding background to the toplevel widget
import tkinter.ttk as ttk

import pygame
import random
import math

window = Tk() #creation of window
pygame.mixer.init()#sound
window.title("Werewolf Run")#window title
window.geometry('1024x768')#size of the window

#these three lines will add background image to our main window
icon =PhotoImage(file="wolf_yellow_resize_text.png")#background image
label=Label(window,image=icon)#making it a default background image
label.place(x=0,y=0)#placing of bckground image

#find it out??? dont know the use... let it be
frame=Frame(window)
frame.place(x=100,y=100)

#to destroy the window we created this close button
Close= lambda:window.destroy()#exit button

#this will create the instructions text window... also will remove the instructions tile and place another tile named clear_instruction
def visible():
    tinst.place(x=600, y=640)  # placing the instructions button
    instruction.place_forget()
    clear_instruction.place(x=700, y=310)

#this will close the instructions text window... also will remove the clear_instructions tile and place again the other tile named instructions
def display():
    tinst.place_forget()
    clear_instruction.place_forget()
    instruction.place(x=700, y=310)

#this function when called will play our main menu music
def play_menu_bgm():
	pygame.mixer.music.load("music/choice2.wav")
	pygame.mixer.music.play(-1) #passing value -1 to make the music run infinitely

def stop_music():
    pygame.mixer.music.stop()

def story():
    tstory.place(x=600, y=520)  # placing the instructions button
    story.place_forget()
    close_story.place(x=700, y=240)

def close_story():
    tstory.place_forget()
    close_story.place_forget()
    story.place(x=700, y=240)

bg_end_game = PhotoImage(file='end_rock_hit.png')

def end_game(score):

    end_window = Toplevel()
    stop_music()


    def exit_end_game():
        stop_music()
        play_menu_bgm()
        pygame.display.quit()
        end_window.destroy()# this will destroy the window

    def replay():
        exit_end_game()
        The_game_loop()

    def complete_exit():
        exit_end_game()
        window.destroy()

    #play_game_music()
    end_window.title("Werewolf Run")  # window title
    end_window.geometry('1024x768')  # size of the window

    my_img = ImageTk.PhotoImage(Image.open('end_screen.jpg')) # death by wolf bite


    my_label = Label(end_window,image=my_img).pack() 
    frame_new = Frame(end_window)
    frame_new.place(x=300, y=100)

    main_menu = Button(end_window, text=" Main Menu ", font=("Forte", 20), fg="white", bg="black", command=exit_end_game)
    main_menu.place(x=700, y=550)

    play_again = Button(end_window,text=" Play Again ", font=("Forte",20), fg="white", bg="black", command=replay)
    play_again.place(x=700,y=450)

    game_exit = Button(end_window,text="End Game",font=("Forte",20), fg="white", bg="black", command=complete_exit)
    game_exit.place(x=700,y=650)

    final_score = Label(end_window, text="You survived: "+str(math.trunc(score)/10)+" m", font=('Forte', 50), foreground="white", background="#708892")
    final_score.place(x=300,y=250)

    end_window.mainloop()


def The_game_loop():
    end_game(werewolf_run.main())

play_menu_bgm()

start = Button(window,            text="      Start       ", font=("Forte",20), fg="white", bg="black", command=The_game_loop)
exit_button = Button(window,      text="      Exit       ", font=("Forte",20), fg="white", bg="black", command=Close)
instruction = Button(window,      text="Instructions", font=("Forte",20), fg="white", bg="black", command=visible)
clear_instruction = Button(window,text="Clear Instructions", font=("Forte",20), fg="white", bg="black", command=display)
story = Button(window,            text="      Story      ", font=("Forte",20), fg="white", bg="black", command=story)
close_story = Button(window,      text=" Close Story ", font=("Forte",20), fg="white", bg="black",command=close_story)
#this contains the story
ts='As you attempt to run away from the wolves,\ndodge all the obstacles in time to avoid being the\nwolves dinner.\nIt\'s a full moon night\nMake sure you watch your back,because\nNOBODY HAS EVER COME BACK ALIVE OUT OF THE FOREST!!'
scrollbar = Scrollbar(window) # this is one is scrollbar for instructions
tstory = Text(window,height=6,width=55,yscrollcommand=scrollbar.set,bd=2)
scrollbar.config(command=tstory.yview())
scrollbar.pack(side=LEFT,fill=Y)

tstory.insert(END,ts)#this will insert data in the instructions window

tstory.place_forget()#will collapse the instructions button
tstory.configure(state='disabled')


scrollbar = Scrollbar(window) # this is one is scrollbar for instructions
tinst = Text(window,height=3,width=30,yscrollcommand=scrollbar.set,bd=2)
scrollbar.config(command=tinst.yview())
scrollbar.pack(side=LEFT,fill=Y)
ti='''Use Spacebar to jump.
Down arrow key to roll.   
Just don't die.'''
tinst.insert(END,ti)#this will insert data in the instructions window

tinst.place_forget()#will collapse the instructions button
tinst.configure(state='disabled')

start.place(x=700,y=170)
story.place(x=700,y=240)
instruction.place(x=700,y=310)
exit_button.place(x=700,y=380)

window.mainloop() #whatever written till now will be implemented in the game window
