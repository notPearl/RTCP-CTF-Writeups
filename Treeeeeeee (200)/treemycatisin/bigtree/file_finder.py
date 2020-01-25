f = open("files.txt","r")
for line in f:
    if line !="" and len(line.split())==9:
        if line.split()[4] != "1.7K" and line.split()[4] != "1.5K" and line.split()[4] != "4.0K":
            print(line)
