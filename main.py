
#- Import modules to follow my CONVENTIONS 

# THE LATESTEST MARCH 3, 2026 


import art                      # ASCII art
import os                       # OS commands to clear the screen
import sys                      # System-specific parameters and functions
import requests                 # Making HTTP requests
import random                   # Random number generation
import time                     # Time-related functions

import lib                      # My library of functions and variables

import tkinter as tk            # Tcl/Tk library 


#- Define "global" variables and functions.

title = "Typing Speed Test"
APP_WIDTH = 600
APP_HEIGHT = 600                    
OFFSETX = 100
OFFSETY = 50

#- Set up APIs

#- Start with my CONVENTION of introductory information  

lib.clear_screen()
#print(art.text2art(title, font='medium'))

#- Setup APPLICATION LOGIC "layer" for business logic, routing, templates, etc. 

#- Working on finding an excerpt for the test

#print(lib.passage())

#- Working on setting up application space

root = tk.Tk()                  # setting up TKinter window 
sw = root.winfo_screenwidth()   # to center on screen 
sh = root.winfo_screenheight()
x = (sw - APP_WIDTH) // 2
y = (sh - APP_HEIGHT) // 2
root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{x}+{y}")
root.resizable(False, True)      # allow resizing only for height 

#- Setting up Frames for each section

frm_stat = tk.Frame(               # the statistics frame
    root,    
    bg="lightyellow", 
    height=100, bd=2, 
    relief="solid"
    )     
frm_stat.pack(
    fill="x",
    padx=20,
    pady=20, 
    )                                     # fill horizontally 

frm_pasg = tk.Frame(root, bg="lightblue", height=100)       # the passage frame 
frm_pasg.pack(fill="both", expand=True)                     # fill in both diretions

frm_feed = tk.Frame(root, bg="black", height=200)           # the feedback frame 
frm_feed.pack(fill="x")                                     # fill horizontally 

frm_ctrl = tk.Frame(root, bg="lightyellow", height=100)     # the control panel 
frm_ctrl.pack(fill="x")                                     # fill horizontally













root.mainloop()                 # the loop to display and respond to events 






