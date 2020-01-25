FBI
-------------------------------------------

Happy MLK day! (January 20th for y'alls non-American folk).

-------------------------------------------
Hints
-------------------------------------------
What's does the challenge name have to do with its theme?
Flag format is rtcp(...) not rtcp{}
The text you use to solve this challenge may slightly vary by a few characters, spacing etc. If these exists, correct them to make it a valid string of english words separated by -s

# WRITEUP

After a little googling the keywords "FBI" and "MLK", I found a letter from the FBI to MLK telling him to commit suicide. I then transcribed the letter into a text document without the KING,\n\n part because the MESSAGE.txt contained that as well.
I then discovered that the numbers in MESSAGE.txt represent a kind of cipher where the first number is the paragraph number, the second number is the line number in the paragraph, and the third number is the character number in the line.
I wrote a python script, which is included in this directory, to decode the flag.

# rtcp(happy-fiftieth-mlk-day-america-has-come-a-long-way)