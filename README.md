## Day 86 - Typing Speed Test

## Requirements

A Tkinter GUI desktop application that tests your typing speed.

Using Tkinter and what you have learnt about building GUI applications with Python, build a desktop app that assesses your typing speed. Give the user some sample text and detect how many words they can type per minute.
The average typing speed is 40 words per minute. But with practice, you can speed up to 100 words per minute.

You can try out a web version here:
https://typing-speed-test.aoeu.eu/

If you have more time, you can build your typing speed test into a typing trainer, with high scores and more text samples. You can design your program any way you want.

## My Notes

1/18/26, Getting Organized

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

1/21/25-, Understanding Tkinter

    1. Setup the windows (game board)...

        a. Go look at ScoreBoard for Snake game ✔️
            i. This was just manage the tracking the score and managing the "Turtle" 🐢
            ii. Thus, this is useless. 🙁
        b. Again, "life," computer problems, etc.
            i. Yes, my PC is virtually useless...thought I had it fixed and decided it was time to move on (without loosing data) 
            ii. Yet, the coding most go on to decided to move back to my Raspberry Pi for development until my PC is fixed
            iii. 
        
        c. Regroup again.
            i. Draw on paper how I want it to look. 🗒️
            ii. Figure out how to make these distint areas
                - Overall application window → win_app
                - Statistics/Score window → win_stats
                - Test content window → win_content
                - Feedback (what user is doing) window → win_feedback


                    ~ Yes, tried to do this without AI 🤖
                    ~ Found tutorial at https://docs.python.org/3/library/tkinter.html 🚌
                    ~ Okay, that docuemntation sucks so started over with some prevous code 👎🏾
                    ~ Figured out that creating Frames was solution to sections 😁
                    ~ Test with statistics frame making it have the window be the "border" ✔️
                    ~ Move the logic and formatting to the other frames
                    ~ Don't forget to make the root window stretch to widegets
                    ~ Also, don't forget to add the title to the root window
                    ~ Before parking this, put buttons in the control frame
                        1. Start
                        2. Stop
                        3. Reset
                        4. Exit

    3. Make sure to address scoring based on the number of error (Corrected CPM).
        a. Instead of computer solution, search Internet to get equations for CPM, WPM and accuracy
        b. Then, stand back for the moment

    2. Experiment with reading from keyboard.
        a. First, just reading the keybooard
        b. Then, evaluate if any speed options (might be an Internet search)

    7. Reevaluate plans on how to...
        a. Start the test.
        b. Analzye the test.
        c. Report back to test subject.




TBD, Wraping Up

    3. Clean up (and test) the code.

    2. Create a requirements.txt file

    3. Push to Git Hub

    4. Post assignment.

        a. Layout top line approach
        b. Note lesson learned
        c. Share code via Git Hub

Whew, this lesson here was just is becoming evident with all these projects. First, I have to reserach to get familiar with topic. Most of these projects are not something new, but have established CONVENTIONS. Yet, the research can be a little overwhelming and in someways feels like slowing down process. In the end, the research allows for comining up with strategy. The initial startegy is a "what is computers did not exist" approach. Then, start to figure out how to make the computer do these things. Last, have to make it pretty. Second, I am still finding myself very curious about using Tkinter and thus find myself taking more time than necessary. At highlevel, my appraoch was...

1. Understand the requirements
2. Look at examples.
3. Reserach history of typing tests
4. Decide on layout
5. Refresh Tkinter knowledge
6. Build out the "layout" with Tkinter windows, frames, and buttons
7. Looked for equations to evaluate WPM, CPM and

...BTW, I tried very hard to avoid using an LMM and that meant quiclly scrolling down the page after a Google search. In many cases, the original documentation was horrible but found good exmamples. In the end, the joy was seeing an idea slowly come to life. You start off saying, "I don't know how to do that." Then, from brainstorming, experiment, and just "doing the work" it all comes together.
