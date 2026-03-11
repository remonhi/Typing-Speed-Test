
#- Import modules to follow my CONVENTIONS 

import art                      # ASCII art
import os                       # OS commands to clear the screen
import sys                      # System-specific parameters and functions
import requests                 # Making HTTP requests
import random                   # Random number generation
import time                     # Time-related functions

import lib                      # My library of functions and variables

import tkinter as tk            # Tcl/Tk library 
from tkinter import ttk         # Themed Tkinter widgets


#- Define "global" variables and functions.

title = "Typing Speed Test"

APP_WIDTH = 600
APP_HEIGHT = 600                    
OFFSETX = 100
OFFSETY = 50

start_time = None
elapsed_time = 0
typed_chars = 0
correct_chars = 0
test_status = False
passage_text = lib.passage()


def on_key(event):
    global start_time, elapsed_time, typed_chars, correct_chars, test_status

    if test_status:
        return

    key = event.char

    if start_time is None:                                                                      # start timer on first keystroke
        start_time = time.time()
  
    if event.keysym == "BackSpace":                                                             # handle Backspace
        if typed_chars > 0:
            typed_chars -= 1
        txt_feed.config(state="normal")
        txt_feed.delete("end-2c", "end-1c")
        txt_feed.config(state="disabled")
        return

    if event.keysym in ("Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R"):      # ignore modifier keys
        return


    if key:                                                                                     # normal characters
        index = typed_chars                                                                     # index used to compare with passage 
        typed_chars += 1

        if index < len(passage_text) and key == passage_text[index]:                            # check correctness
            correct_chars += 1

        txt_feed.config(state="normal")                                                         # insert into feed
        txt_feed.insert("end", key)
        txt_feed.config(state="disabled")
        txt_feed.see("end")

        if typed_chars == len(passage_text):                                                    # end test if finished
            test_status = True
            end_test()


def end_test():
    global start_time, typed_chars, correct_chars

    elapsed = time.time() - start_time
    minutes = elapsed / 60

    wpm = (typed_chars / 5) / minutes if minutes > 0 else 0.                                    # WPM calculation

    accuracy = (correct_chars / typed_chars) * 100 if typed_chars > 0 else 0                    # Accuracy calculation

    result = f"\nWPM: {wpm:.1f}    Accuracy: {accuracy:.1f}%\n"

    txt_feed.config(state="normal")
    txt_feed.insert("end", result)
    txt_feed.config(state="disabled")
    txt_feed.see("end")




#- Set up APIs

#- Start with my CONVENTION of introductory information  

lib.clear_screen()

#print(art.text2art(title, font='medium'))

#- Setup APPLICATION LOGIC "layer" for business logic, routing, templates, etc. 

#- Working on finding an excerpt for the test

# print(lib.passage())

#- Working on setting up application space

root = tk.Tk()                  # setting up TKinter window 
sw = root.winfo_screenwidth()   # to center on screen 
sh = root.winfo_screenheight()
x = (sw - APP_WIDTH) // 2
y = (sh - APP_HEIGHT) // 2
root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{x}+{y}")
root.resizable(False, True)     # allow resizing only for height 
root.title(title)               # set the title of the window

#- Setting up Frames for each section

#! Statistics 

frm_stat = tk.Frame(                                       
    root,    
    bg="lightyellow", 
    height=100, 
    bd=2, 
    relief="solid"
    )     

frm_stat.pack(
    fill="both",
    expand=True,
    padx=5,
    pady=5, 
    )                                                   

#! Passage 

frm_pasg = tk.Frame(                                        
    root, 
    bg="lightblue", 
    height=100,
    bd=2, 
    relief="solid"
    )       

frm_pasg.pack(
    fill="both",
    expand=True,
    padx=5,
    pady=5, 
    ) 


lbl_pasg = tk.Label(
    frm_pasg,
    text=passage_text,
    font=("Arial", 16),
    justify="left",
    bg="lightblue",
    )

lbl_pasg.pack(fill="both", expand=True, padx=20, pady=20)




#! Feedback

frm_feed = tk.Frame(
    root, 
    bg="black", 
    height=200,
    bd=2, 
    relief="solid"
    )       

frm_feed.pack(
    fill="both",
    expand=True,
    padx=5,
    pady=5, 
    ) 

txt_feed = tk.Text(
    frm_feed,
    font=("Arial", 14),
    bg="white",
    height=2,
    wrap="word"
    )

txt_feed.configure(state="disabled")  # to stop the doubleing 

txt_feed.pack(fill="both", expand=True, padx=10, pady=10)


#! Controls

frm_ctrl = tk.Frame(
    root,
    bg="#A9A9A9",
    height=100,
    bd=2,
    relief="solid"
    )

frm_ctrl.pack(fill="x", padx=5, pady=5)

frm_ctrl.pack_propagate(False)

style = ttk.Style()         # Style setup (macOS needs this to allow colors) & got "help" here
style.theme_use("clam")     # enables custom colors on macOS
style.configure(
    "Ctrl.TButton",
    background="#1e90ff", 
    foreground="white",
    font=("Arial", 14),
    padding=10
    )

style.map(
    "Ctrl.TButton",
    background=[("active", "#3CB371")]  # lighter green on hover
    )

btn_start = ttk.Button(frm_ctrl, text="Start", style="Ctrl.TButton")
btn_stop  = ttk.Button(frm_ctrl, text="Stop",  style="Ctrl.TButton")
btn_reset = ttk.Button(frm_ctrl, text="Reset", style="Ctrl.TButton")
btn_quit  = ttk.Button(
    frm_ctrl, 
    text="Quit",  
    style="Ctrl.TButton",
    command=root.destroy
    )

btn_start.grid(row=0, column=0, padx=10, pady=20, sticky="nsew")
btn_stop.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")
btn_reset.grid(row=0, column=2, padx=10, pady=20, sticky="nsew")
btn_quit.grid(row=0, column=3, padx=10, pady=20, sticky="nsew")

for col in range(4):
    frm_ctrl.grid_columnconfigure(col, weight=1)


#! The main loop to display the window and respond to events

root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
root.bind("<Key>", on_key)      # bind key events to the on_key function
root.mainloop()                 # the loop to display and respond to events 






