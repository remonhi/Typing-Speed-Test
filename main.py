
# - Import modules to follow my CONVENTIONS 

from cProfile import label
import art               # ASCII art
import os                # OS commands to clear the screen
import sys               # System-specific parameters and functions
import requests          # Making HTTP requests
import random            # Random number generation
import time              # Time-related functions

import lib               # My library of functions and variables

from PIL import Image, ImageFilter, ImageTk    # Image processing
import tkinter as tk                  # GUI library


# - Define "global" variables and functions.

title = "Image Watermarking Desktop App"
SCREEN_SIZE = 600                   
OFFSETX = 100
OFFSETY = 50

# - Set up APIs

# - Start with my CONVENTION of introductory information  

lib.clear_screen()
#print(art.text2art(title, font='medium'))

# - Setup APPLICATION LOGIC "layer" for business logic, routing, templates, etc. 

 #! Started with Pillow tutorial, https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

#- Loading the original file from command line

if len(sys.argv) < 2:
    print("Usage: python main.py <image_path>")
    sys.exit(1)

infile = sys.argv[1]

try:
    img = Image.open(infile)
    print(f"Image load → '{infile}' Successful!")
    print(f"Image format → {img.format}")
    print(f"Image size → {img.size}")
    print(f"Image mode → {img.mode}")

except FileNotFoundError:
    print("Error: Image file not found at that path.")

except OSError:
    print("Error: File exists but is not a valid image.")

except Exception as e:
    print(f"Unexpected error: {e}")

#-  Loading original image from command line, making Pillow work with Tkinter, and displaying with Tkinter 

win_og = tk.Tk()                              # setting up TKinter window 
img_og = ImageTk.PhotoImage(img)              # making Pillow work with Tkinter

w, h = img.size                               # getting the image size 
scr_w = win_og.winfo_screenwidth()            # getting screen size 
scr_h = win_og.winfo_screenheight()           # also, getting screen size 
sex = (scr_w - w) // 2                          # settting the X
sey = (scr_h - h) // 2                          # setting the Y 
win_og.geometry(f"{w}x{h}+{sex}+{sey}")           # centering the image 

win_og.title("Original Image")                # giving the window a title 
label_og = tk.Label(win_og, image=img_og)     # creating a reference to window and relating the Pillow image 
label_og.pack()                               # displaying the window 
label_og.image = img_og                       # saving the refernce to prevent gargage collection 

#- Converting to B&W with Pillow and displayign with Tkinter 

bw = img.convert("L")                                    # convert to black and white
name, ext = os.path.splitext(os.path.basename(infile))   # get name and extension of original file
bw.save(f"{name}-bw{ext}")                               # not needed but saving the B&W image 

img_bw = ImageTk.PhotoImage(bw)                          # taking the Pillow image into Tkinter 
win_bw = tk.Toplevel()                                   # making window for B&W work in same loop 
win_bw.title("Black & White Image")                      # yes, give the TKinter window a title 
label_bw = tk.Label(win_bw, image=img_bw)                # creating a reference to window  
win_bw.geometry(f"{w}x{h}+{sex + OFFSETX}+{sey + OFFSETY}")  # positing the image 
label_bw.pack()                                          # pack it for display
label_bw.image = img_bw                                  # keep the reference to prevent garbage collection 

#- Adding the watermark with Pillow, saving, and then displaying with Tkinker 

wm = img.copy()                                                       # make copy of original image 
logo = Image.open("static/images/logoloremipsum.png").convert("RGBA") # load the watermark image
logo = logo.resize((100,100))                                         # make it smaller 
w, h = wm.size                                                        # getting the image size
r, s = logo.size                                                      # getting the logo size
x = 20                                                                # the left side
y = h - s - 20                                                        # the bottom 
wm.paste(logo, (x, y), mask=logo)                                     # positioning the logo 
wm.save(f"{name}-wm{ext}")

img_wm = ImageTk.PhotoImage(wm)                          # make it a Tkinter image 
win_wm = tk.Toplevel()                                   # making window work in same loop 
win_wm.title("Watermark Image")                          # yes, give the TKinter window a title 
label_wm = tk.Label(win_wm, image=img_wm)                # creating a reference Pillow image   
win_wm.geometry(f"{w}x{h}+{sex - OFFSETX*2}+{sey + OFFSETY*2}")  # positing the image 
label_wm.pack()                                          # pack it for display
label_wm.image = img_wm                                  # keep the reference to prevent garbage collection 

#- The essential/primary Tkinter loop

win_og.mainloop()                    



