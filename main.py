
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
import tkinter.font as tkfont  # Font handling in Tkinter





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

font_title = ("Segoe UI", 16, "bold")
font_body  = ("Segoe UI", 12)
font_stat  = ("Segoe UI", 14, "bold")



def on_key(event):
    global start_time, elapsed_time, typed_chars, correct_chars, test_status

    if test_status:
        return
    
    if typed_chars >= len(passage_text):                                                        # prevent typing beyond passage length
        return

    key = event.char

    if start_time is None:                                                                      # start timer on first keystroke
        start_time = time.time()
  
    if event.keysym == "BackSpace":                                                             # handle backspace
        if typed_chars > 0:
            typed_chars -= 1
        txt_feed.config(state="normal")
        txt_feed.delete("end-2c", "end-1c")
        txt_feed.config(state="disabled")
        update_live_stats()   
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

        update_live_stats()

        if typed_chars >= len(passage_text):                                                    # end test if finished
            test_status = True
            end_test()
            return


def update_live_stats():
    if start_time is None:
        return

    elapsed = time.time() - start_time
    minutes = elapsed / 60 if elapsed > 0 else 1e-9

    errors = typed_chars - correct_chars

    gwpm = (typed_chars / 5) / minutes
    nwpm = gwpm - (errors / minutes)
    nwpm = max(nwpm, 0)

    accuracy = (correct_chars / typed_chars) * 100 if typed_chars > 0 else 0

    lbl_gwpm.config(text=f"GWPM: {gwpm:.1f}")
    lbl_nwpm.config(text=f"NWPM: {nwpm:.1f}")
    lbl_acc.config(text=f"Accuracy: {accuracy:.1f}%")
    lbl_err.config(text=f"Errors: {errors}")


def end_test():
    global start_time, typed_chars, correct_chars

    elapsed = time.time() - start_time
    minutes = elapsed / 60

    wpm = (typed_chars / 5) / minutes if minutes > 0 else 0.                                    # WPM calculation

    accuracy = (correct_chars / typed_chars) * 100 if typed_chars > 0 else 0                    # Accuracy calculation

    errors = typed_chars - correct_chars                                                        # Error count

    gwpm = (correct_chars / 5) / minutes if minutes > 0 else 0                                  # Gross WPM calculation

    nwpm = gwpm - (errors / minutes) if minutes > 0 else 0                                      # Net WPM calculation

  # Update statistics frame


    lbl_gwpm.config(text=f"GWPM: {gwpm:.1f}")
    lbl_nwpm.config(text=f"NWPM: {nwpm:.1f}")
    lbl_acc.config(text=f"Accuracy: {accuracy:.1f}%")
    lbl_err.config(text=f"Errors: {errors}")







def get_valid_passage():
    min_len = 150
    max_len = 350

    for _ in range(10):
        text = lib.passage()
        if min_len <= len(text) <= max_len:
            return text
    
    return "Error: Could not fetch a passage of acceptable length."


def reset_test():
    global start_time, elapsed_time, typed_chars, correct_chars, test_status, passage_text

    # Reset state
    start_time = None
    elapsed_time = 0
    typed_chars = 0
    correct_chars = 0
    test_status = False

    # Fetch a new passage
    passage_text = get_valid_passage()

    # Clear the feed window
    txt_feed.config(state="normal")
    txt_feed.delete("1.0", "end")
    txt_feed.config(state="disabled")

    # Display the new passage
    lbl_pasg.config(state="normal")
    lbl_pasg.config(text=passage_text)

    # Reset statistics labels
    lbl_gwpm.config(text="GWPM: 0")
    lbl_nwpm.config(text="NWPM: 0")
    lbl_acc.config(text="Accuracy: 0%")
    lbl_err.config(text="Errors: 0")




#- Set up APIs

#- Start with my CONVENTION of introductory information  

lib.clear_screen()

#print(art.text2art(title, font='medium'))

#- Setup APPLICATION LOGIC "layer" for business logic, routing, templates, etc. 

#- Working on finding an excerpt for the test

# print(lib.passage())



#- Working on setting up application space

root = tk.Tk()                  # setting up TKinter window 
root.configure(bg="#F5F7FA")  # set background color 
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
    bg="#F0F2F5",          # soft modern gray
    height=80,
    bd=2,
    relief="solid"
)
frm_stat.pack(
    fill="x", 
    padx=20, 
    pady=10
    )

frm_stat.pack_propagate(False)

# Modern font for stats
font_stat = ("Segoe UI", 14, "bold")

# --- CREATE LABELS ---
lbl_gwpm = tk.Label(frm_stat, text="GWPM: 0", font=font_stat, bg="#F0F2F5", fg="#111827")
lbl_nwpm = tk.Label(frm_stat, text="NWPM: 0", font=font_stat, bg="#F0F2F5", fg="#111827")
lbl_acc  = tk.Label(frm_stat, text="Accuracy: 0%", font=font_stat, bg="#F0F2F5", fg="#111827")
lbl_err  = tk.Label(frm_stat, text="Errors: 0", font=font_stat, bg="#F0F2F5", fg="#111827")

# --- GRID LAYOUT FOR PERFECT CENTERING ---
frm_stat.grid_columnconfigure(0, weight=1)
frm_stat.grid_columnconfigure(1, weight=1)
frm_stat.grid_columnconfigure(2, weight=1)
frm_stat.grid_columnconfigure(3, weight=1)

lbl_gwpm.grid(row=0, column=0, padx=10, pady=20, sticky="n")
lbl_nwpm.grid(row=0, column=1, padx=10, pady=20, sticky="n")
lbl_acc.grid(row=0, column=2, padx=10, pady=20, sticky="n")
lbl_err.grid(row=0, column=3, padx=10, pady=20, sticky="n")


#! Passage 

passage_text = get_valid_passage()

frm_pasg = tk.Frame(
    root,
    bg="#FFFFFF",
    highlightbackground="#D0D7DE",
    highlightthickness=1,
    bd=2,
    relief="solid"
)
frm_pasg.pack(fill="x", padx=20, pady=10)

# --- PASSAGE LABEL ---
lbl_pasg = tk.Label(
    frm_pasg,
    text=passage_text,
    font=("Arial", 16),
    justify="center",
    bg="#FFFFFF",
    fg="#111827",
    anchor="center",     
    padx=2,         
    pady=8
)
lbl_pasg.pack(fill="both", expand=True)




#! Feedback

frm_feed = tk.Frame(
    root,
    bg="#FFFFFF",
    bd=2,
    height=frm_pasg.winfo_reqheight(),  # match passage frame height
    relief="solid"
)
frm_feed.pack(
    fill="x", 
    padx=20, 
    pady=10)

txt_feed = tk.Text(
    frm_feed,
    bg="#FFFFFF",
    fg="#111827",
    font=("Consolas", 14),
    wrap="word",
    padx=10,
    pady=10,
    relief="flat"
)

root.update_idletasks()   # force Tkinter to calculate real sizes

label_width = lbl_pasg.winfo_width()
font = tkfont.Font(font=lbl_pasg["font"])
text = lbl_pasg.cget("text")
words = text.split()
lines = []
current = ""

for w in words:
    test = (current + " " + w).strip()
    if font.measure(test) <= label_width - 20:   # subtract padding
        current = test
    else:
        lines.append(current)
        current = w
lines.append(current)

passage_line_count = len(lines)
feedback_height = passage_line_count + 1
txt_feed.config(height=feedback_height)

txt_feed.pack(fill="both", expand=True)



#! Controls

frm_ctrl = tk.Frame(
    root,
    bg="#FFFFFF",
    height=70,          # smaller height
    bd=2,
    relief="solid"
)
frm_ctrl.pack(
    fill="x", 
    padx=20, 
    pady=10)   # matches feedback frame spacing

frm_ctrl.pack_propagate(False)

# --- BUTTON STYLE ---
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Ctrl.TButton",
    font=("Segoe UI", 12, "bold"),
    padding=8,          # smaller padding for tighter buttons
    foreground="white",
    background="#2563EB",
    borderwidth=0
)

style.map(
    "Ctrl.TButton",
    background=[("active", "#1E4FCF")],
    foreground=[("active", "white")]
)

# --- GRID LAYOUT ---
for col in range(6):
    frm_ctrl.grid_columnconfigure(col, weight=1)

# --- BUTTONS ---
btn_reset = ttk.Button(frm_ctrl, text="Reset", style="Ctrl.TButton", command=reset_test)
btn_quit  = ttk.Button(frm_ctrl, text="Quit",  style="Ctrl.TButton", command=root.quit)

btn_reset.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")   # reduced vertical padding
btn_quit.grid(row=0, column=3, padx=10, pady=5, sticky="nsew")





#! The main loop to display the window and respond to events

root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
root.bind("<Key>", on_key)      # bind key events to the on_key function
root.mainloop()                 # the loop to display and respond to events 






