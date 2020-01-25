indices = open("MESSAGE.txt", "r")
base_text = open("source.txt", "r").read()
output = ""
count = 0
for line in indices:  
    location = line.split()
    current_paragraph = base_text.split("\n\n")[int(location[0])]
    current_line = current_paragraph.split("\n")[int(location[1])]
    output = output + current_line[int(location[2])]
print(output)
