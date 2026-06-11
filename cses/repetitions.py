string = str(input("")).strip()
mx = 1
counter = 0
for i in range(len(string)):
    if string[i-1] == string[i]:
        counter += 1
    elif string[i-1] != string[i]:
        if counter > mx: 
            mx = counter 
        counter = 1
if counter > mx:
    mx = counter
print(mx)