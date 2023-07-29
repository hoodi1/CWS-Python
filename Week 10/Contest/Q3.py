''' Implement a function to find the longest common prefix
among an list of strings.'''

a=["flow","flight","flower"]
char=''
current_pos=0
while True:
    flag=True
    current_char=a[0][current_pos]  
    for word in a:
        if word[current_pos]!=current_char:
            flag=False
            break
    else:
        char+=current_char
        current_pos+=1
    for word in a:
        if len(word)==current_pos:
            flag=False
            break
    if not flag:
        break

print(char)
