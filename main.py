
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
    text=lib.passage(),
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


#! Controls

frm_ctrl = tk.Frame(
    root,
    bg="lightgreen",
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
    background="#2E8B57",   # sea green
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
btn_quit  = ttk.Button(frm_ctrl, text="Quit",  style="Ctrl.TButton")

btn_start.grid(row=0, column=0, padx=10, pady=20, sticky="nsew")
btn_stop.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")
btn_reset.grid(row=0, column=2, padx=10, pady=20, sticky="nsew")
btn_quit.grid(row=0, column=3, padx=10, pady=20, sticky="nsew")

for col in range(4):
    frm_ctrl.grid_columnconfigure(col, weight=1)















root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
root.mainloop()                 # the loop to display and respond to events 






