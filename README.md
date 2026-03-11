## Day 86 - Typing Speed Test

## Requirements

A Tkinter GUI desktop application that tests your typing speed.

Using Tkinter and what you have learnt about building GUI applications with Python, build a desktop app that assesses your typing speed. Give the user some sample text and detect how many words they can type per minute.
The average typing speed is 40 words per minute. But with practice, you can speed up to 100 words per minute.

You can try out a web version here:
https://typing-speed-test.aoeu.eu/

If you have more time, you can build your typing speed test into a typing trainer, with high scores and more text samples. You can design your program any way you want.

## My Notes

1/18/26, Getting Organized ✅

    Copied over from previous project → cp -R 'Day 85' 'Day 86' ✔️
    Removed old virtual environment → rm -rf venv ✔️
    Removed the old git tracking → rm -rf .git ✔️
    Initialized the virtual environment → python -m venv venv ✔️
    Activated the virtual environemtn → source venv/bin/activate ✔️
    Initlaized a new repo → ✔️
        git init
        git add .
        git commit -m "initial commit"
    Noted old Git Ignore still there → cat .gitignore ✔️
    Set branch name → git branch -M main ✔️
    Created new repo at Gig Hub → https://github.com/remonhi/Typing-Speed-Test ✔️
    Connected to net repo → git remote add origin git@github.com:remonhi/Typing-Speed-Test.git ✔️


    1. Check out provided example at https://typing-speed-test.aoeu.eu/ ✅
        a. Learned about
            i. Corrected Characters Per Minute (CPM)
            ii. Words Per Minute (CPM)
            iii. Raw versus Corrected
        b. Like the idea of real time feedback, and also a timed test.
        c. Last, an option to restar the test

    2. Research the topic of typing test (from the old days) ✅
        a. Words Per Minute (WPM) - dividing the total characters tyhped by 5 (a word) and test duratiaon adjusted for errors.
        b. Accuracy - ( Correct Characters / Total Characters ) * 100%
        c. Test Format - Involve typing passages of text (not random words)
        d. Standards/Benchmarks

            - Learning < 30
            - General Office/Admin: 40-60 WPM (e.g., handling emails, notes).
            - Customer Support/Management: 60-80 WPM (for efficient communication).
            - Content Writing/Marketing: 70-90 WPM (for longer content).
            - Data Entry/Transcription: 80-100+ WPM (high volume, high accuracy needed).
            - 911 Operator: 80-85 WPM (critical speed/accuracy).

1/19/25, More Research 

    1. Come up with apporoach (using an API) for obtaining text for testing. ✅
        a. Okay, going with Gutenberg
        b. Pick out a random exerpt
        c. Clean up the "try" for the request
        d. Test it a little bit

    2. Regrouped here. ✅
        a. Had to stop in middle of all this to deal with a network issue.
        b. Then, made plans for next day.

1/21/26-3/4/26, Understanding Tkinter ✅

    1. Setup the windows (game board)...

        a. Go look at ScoreBoard for Snake game ✔️
            i. This was just manage the tracking the score and managing the "Turtle" 🐢
            ii. Thus, this is useless. 🙁
        
        b. Again, "life," computer problems, etc. ✔️
            i. Yes, my PC is virtually useless...thought I had it fixed and decided it was time to move on (without loosing data) 🙁
            ii. Yet, the coding most go on to decided to move back to my Raspberry Pi for development until my PC is fixed 🙁
            iii. First, I reconnected my Raspberry Pi to network and worked on getting the latest updates to it. ⬅️
            iv. Second, confirmed everything workign with current code. 🤷🏽‍♀️
        
        c. Regroup again. ☹️
            i. Draw on paper how I want it to look. 🗒️
            ii. Figure out how to make these distint areas 🤬
                - Overall application window → win_app
                - Statistics/Score window → win_stats
                - Test content window → win_content
                - Feedback (what user is doing) window → win_feedback


                    ~ Yes, tried to do this without AI 🤖
                    ~ Found tutorial at https://docs.python.org/3/library/tkinter.html 🚌
                    ~ Okay, that docuemntation sucks so started over with some prevous code 👎🏾
                    ~ Figured out that creating Frames was solution to sections 😁
                    ~ Test with statistics frame making it have the window be the "border" ✔️
                    ~ Move the logic and formatting to the other frames ❌
                    ~ Don't forget to make the root window stretch to widegets ❌
                    ~ Also, don't forget to add the title to the root window ❌
                    ~ Before parking this, put buttons in the control frame ❌
            


        d. Getting Back ⬅️
            i. Well, "life interrupted" and finally getting back into this. 🫀
            ii. First, I ended up "rebuilding" my development desktop....
                a. Wipped out and renstalled MacMini 🖥️
                b. First, with OneDrive setup the 'Day 86' to 'Always Keep on This Device' 📁
                c. While waiting for OneDrive, followed guidelines from Copilot to install via Homebrew (recommended for development)...🐍
                    - installed at /opt/homebrew/bin/python3
                    - confirmed version 3.14.3
                d. Rebuilt virtual Python environment 😊
                e. Looks like install did not have TKinter, and had to fix that.  😐
                f. Shit this turned out to be a long "night", so decided to continue tomorrw. ☹️
                g. Reconnect to GitHub 😃
                h. Intall VS Code 😃
                    - Find my old notes for extensions

                        · autoDocstring - Python Docstring Generator
                        · autopep8
                        · Better Comments
                        · GitHub Copilot Chat
                        · GitHub Copilot
                        · Inline Python Package Installer
                        · Live Preview
                        · Prettier - Code formatter
                        · Prettify JSON
                        · Pylance
                        · Python Debugger
                        · Python Environments
                        · Python
                        · REST Client
                        · vscode-icons
                                            
                    - Install the application
                    - Make sure code looks good
                    
                 
            iii. Second, regrouping from where I left off in January...
                1. Draw on paper how I want it to look. - Did not have picture, but have the app working. ✔️
                2. Refresh on how these sections are configured (and named) ✔️
                    - Overall application window → root
                    - Statistics/Score window → frm_stat
                    - Test content window → frm_pasg
                    - Feedback (what user is doing) window → frm_feed
                    - Control pantel → frm_ctrl

                 3. Yes, tried to do this without AI 
                    - Test with statistics frame making it have the window be the "border" ✔️
                    - Move the logic and formatting to the other frames ✔️
                    - Don't forget to make the root window stretch to widgets ✔️
                    - Also, don't forget to add the title to the root window ✔️
                    - Before parking this, put buttons in the control frame ✔️
                        1. Start
                        2. Stop
                        3. Reset
                        4. Exit

                ...got this done with "help" searching internet. 

        2. Just for sanity...
            a. Display content (from API call) in passage frame
                i. First, could not find all my work
                ii. Now, the famous time that OneDrive saved me.
                iii. Cleaned it up and got to display.


3/5/26, No Time ✅
    
    1. Well, not much time today but just for shits wanted to make the 'quit' button work. 🤪
        - Yeah, that was pretty easy.
        - Then, used page https://www.plus2net.com/python/tkinter-colors.php?utm_source=copilot.com to play around with colors

    2. Then, a little research on reading in from keyboard.
        - Started with https://www.pythontutorial.net/tkinter/tkinter-event-binding/ that confused me more.
        - Ended up getting some "help"
        - It is ugly, but got the feedback frame working now.


3/11/26, Comparing Text ✅

    1. Figure how to how make this work... 🛏️
        i. First, had to fix the doublging of text.
        ii. Did some more research, and came up with approach.
        iii. noting formulas for speed...

            Gross WPM (GWPM): (Total Characters / 5) / Time in Minutes.
            Net WPM (NWPM): (Gross WPM) - (Errors / Time in Minutes).

            ...these simply came from internet searches.
            
    2. Doing the work (with some help)
    
        i. Started timer on first key
            a. Setup variables to measure
            b. Had to put the passage into a variable 
            c. Then, worked on modyfing on_key() function to measure.
            d. Thoughts and questions...
                - How the index is used
                - When does it stop measuring. 

        ii. Analyzed the "raw" run and then addressed next steps.


3/12/26-, Owning It

    1. Get rid of START & STOP buttons.
    2. Use GWPM and NWPM instead
    3. Put the results in the statistics frame 
    4. Provide live statistics while typing
    5. Make the reset button work.
    6. Implement color-coded feedback (green/red)
    7. Highlight passage as the user types (definitely required help)
    8. Clean up the look and feel...
        a. Colors
        b. Sizing
    9. Decide on max and minimum passage sizes (and pull another if necessary)



TBD, Wraping Up

    1. Do more testing.
    
    2. Create a requirements.txt file

    3. Push to Git Hub

    4. Post assignment.

        a. Layout top line approach
        b. Note lesson learned
        c. Share code via Git Hub

Whew, working with Tkinter is not one of my favorite projects; however, the real lessons here was about working with the “characters” of the passage to be evaluated and what was typed by the “end user.”  Beyond the intricates of the Tkinter library, first the real work is about researching the requirements. What is great is much data and information that is developed prior to computers being a tool.  For example, the measurement and the applicable formula for ‘Words Per Minute’ came before computers.   In the beginning the research seems like it is slowing down the development, but once development start it all makes sense.  Second, some testing if concepts required.  Last, can finally clean up and make the program usable.  Thus, these major steps have become my CONVENTIONS for development.  To outline, my approach was…

    1. Understand the requirements
    2. Look at examples.
    3. Research history of typing tests
    4. Decide on layout (actually drew on paper)
    5. Refresh Tkinter knowledge
    6. Build out the "layout" with Tkinter windows, frames, and buttons
    7. Looked for equations to evaluate WPM, CPM and

...BTW, I tried very hard to avoid using an LMM and that meant quickly scrolling down the page after a Google search. In many cases, the original documentation was horrible but found good examples. Yes, I did use an LMM for some of the work; however, did not just have it write code and copy it over.  In the end, the joy was seeing an idea slowly come to life. You start off saying, "I don't know how to do that." Then, from brainstorming, experiment, and just "doing the work" it all comes together.

