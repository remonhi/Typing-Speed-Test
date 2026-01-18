## Day 86 - Typing Speed Test

## Requirements

A Tkinter GUI desktop application that tests your typing speed.

Using Tkinter and what you have learnt about building GUI applications with Python, build a desktop app that assesses your typing speed. Give the user some sample text and detect how many words they can type per minute.
The average typing speed is 40 words per minute. But with practice, you can speed up to 100 words per minute.

You can try out a web version here:
https://typing-speed-test.aoeu.eu/

If you have more time, you can build your typing speed test into a typing trainer, with high scores and more text samples. You can design your program any way you want.

## My Notes

1/19/26-, Getting Organized

    Copied over from previous project → cp -R 'Day 85' 'Day 86' ✔️
    Removed old virtual environment → rm -rf venv ✔️
    Removed the old git tracking → rm -rf .git ✔️
    Initialized the virtual environment → python -m venv venv ✔️
    Activated the virtual environemtn → source venv/bin/activate ✔️
    Initlaized a new repo →
        git init
        git add .
        git commit -m "initial commit"
    Noted old Git Ignore still there → cat .gitignore
    Set branch name → git branch -M main
    Created new repo at Gig Hub → https://github.com/remonhi/Text-to-Morse-Code-Converter
    Connected to net repo → git remote add origin git@github.com:remonhi/Text-to-Morse-Code-Converter.git
    Pushed → git push -u origin main














    Copied over Git Ignore → cp ../'Day 84'/.gitignore .

Getting Organized

Okay, I just took this day to start getting organized. Having not used Tkinter in a while I decided to go back to Day 20 to look at teh projects there. I decided to refresh on my code for the 'Snake Game.' Also, it is using OOP that is great. So for today, I just copied all the code over and laid out plans for tomorrow.

    Initialized the virtual environment → python -m venv venv
        Activated the virtual environemtn → source venv/bin/activate
        Initlaized a new repo →
            git init
            git add .
            git commit -m "initial commit"
        Set branch name → git branch -M main
        Created new repo at Gig Hub → https://github.com/remonhi/Image-Watermarking-Desktop-App
        Connected to net repo → git remote add origin git@github.com:remonhi/Image-Watermarking-Desktop-App.git
        Pushed → git push -u origin main

    ...then, turned out the code I wanted use was a different module - 158.py. Thas had a module just for one class, so moved it into the "main."

        1. Moved Food() class ✔️
        2. Broke Snake() class 🥺
        3. Noted that ScoreBoard() class still needs to be moved 😐

1/7/26, Chasing Squirel

    1. Recover the Snake() and make it work.✅
    2. Move the ScoreBoard() class and make it work in same file...created lib.py. ✅
    3. Get rid of var.py refernce. ✅
    4. Get file cleaned up to match my CONVENTIONS.✅
    5. Figure out everything in program works.✅
    6. Review the service https://watermarkly.com/ - Hmmm, very nice...so why am I doing this. ✅
    7. Study https://pypi.org/project/Pillow/, https://docs.python.org/3/library/tkinter.html and little Googling. ✅
        a. Ran through the basic installation.
        b. Used the tutorial to get familar with the library
        c. Wow, converting files is simply changing the extention.
        d. Yeah, more than 90 minutes going through tutorial but gave me a lot understanding and ideas
        e. 'Image Enhancement' seems to be what this is all about...
            i. First, went down a rabbit hole for how to display image (had to use Tkinter)
            ii. PICK BACK UP AT 'Image Enhancement'

1/16/26, Regrouping Work & expereimenting

As the cliche goes, "life happens" but back on this now...

    1. Setup the "GUI Enviroment" with Tkinter ✅

    2. Read in file to be processed from command line (give it an FTP style...from and to) ✅
        a. If no arguemnts, have a default (find the Xolo dog).
        b. If something wrong with arguement, let the user know.

    3. Display the input file. ✅
        a. Using Tkinter documentation, it worked the first time.
        b. Yet, kept displaying a bottom of screen.
        c. Then, got centered but image cut off
        d. Search the "inter web" for solution and it was .geometry() method
        e. This was a "rabbit hole" but better to fix now than later.

    4. Create the output file. ✅
        a. First, just test the creation...going back to Pillow docuentation at https://pypi.org/project/Pillow/ ✔️
        b. Decided to use black and white as test.  ✔️
        c. Went down another rabbit hole to diplay both images at same time. ✔️

    5. Upgrade Python ✅
        a. Went down rabbit hole to upgrade version of Python 🐰
        b. Was running version 3.13.3 🐍
        c. The lastest is 3.14.2 from December 5, 2025 🗓️
        d. Downloaded and stalled via PKG 🍎
        e. Had to take a few more steps to get it working (rebuilding virtual environment). 👍🏾
        f. Saved the requirements.txt 💿

1/18/26, Finally getting this done

I have been trying to balance "life," today decided to wrp this up today...

    1. Process watermark ✅
        a. Come up with a generic graphic for the watemark. ✔️
        b. Place the watermark in bottom left corner. ✔️
        c. Use 'Lorem Ipsum' for text to display after image. ❌

    2. Don't get fancy here ✅
        a. Yes, for now just trying to figure this out.
        b. Later, can get fancy with my "real world" programs.

    3. Clean up (and test) the code. ✅

    2. Create a requirements.txt file ✅

    3. Push to Git Hub

    4. Post assignment.

        a. Layout top line approach
        b. Note lesson learned
        c. Share code via Git Hub
