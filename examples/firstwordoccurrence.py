data = open("content.txt","r")
read_data = data.readlines()
word_found = False
line_number = 1
count = 0

for read in read_data:
    if("learning" in read.lower()):
        if(count == 0):
            print("Line number: ", line_number)
            word_found = True
            count+=1
        else:
            continue
    elif("learning" in read.lower() == -1):
        word_found = False    
    line_number+=1

if not word_found:
    print("Word not found: ", -1)