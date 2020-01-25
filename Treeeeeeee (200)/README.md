Strong Password
-------------------------------------------

It appears that my cat has gotten itself stuck in a tree... It's really tall and I can't seem to reach it. Maybe you can throw a snake at the tree to find it?

Oh, you want to know what my cat looks like? I put a picture in the hints.

-------------------------------------------
Hints
-------------------------------------------
Here, my cat looks like this:

```#FFC90E#FFC90E#FFC90E#FFFFFF#FFFFFF#FFFFFF#FFFFFF#FFFFFF#FFC90E 
#FFC90E#000000#FFC90E#FFFFFF#FFFFFF#FFFFFF#FFFFFF#FFC90E#FFFFFF 
#FFC90E#FFC90E#FFC90E#FFC90E#FFC90E#FFC90E#FFC90E#FFFFFF#FFFFFF 
#FFFFFF#FFFFFF#FFC90E#FFC90E#FFC90E#FFC90E#FFC90E#FFFFFF#FFFFFF 
#FFFFFF#FFFFFF#FFC90E#FFC90E#FFC90E#FFC90E#FFC90E#FFFFFF#FFFFFF 
#FFFFFF#FFFFFF#FFFFFF#FFC90E#FFFFFF#FFC90E#FFFFFF#FFFFFF#FFFFFF```

# WRITEUP

After extracting the files from `treemycatisin.7z', we are greeted with a large folder full of files. AFter looking around, it is discovered that there are two types of image files that are not the flag that contain text. They are identical. In order to weed out those possibilities, I listed all the files with ls -lh -p -R which lists all the files recursively and gives the file sizes in the current directory and piped the output into a text file. I then wrote a python script (you can find this in the big tree directory) to parse the output and weed out any file that had the same size as the images that were not the flag. The image that was singled out contained the flag.

#RTCP{MEOW_SHARP_PIDGION_RICE_TREE}