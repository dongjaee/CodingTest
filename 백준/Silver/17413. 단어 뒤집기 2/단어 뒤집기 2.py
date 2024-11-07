s=input()
result=[]
temp=""
is_tag=False

for char in s:
    if char=='<':
        result.append(temp[::-1])
        temp=""
        is_tag=True
        temp+=char
    elif char=='>':
        temp+=char
        result.append(temp)
        temp=""
        is_tag=False
    elif is_tag:
        temp+=char
    elif char==' ':
        result.append(temp[::-1]+' ')
        temp=''
    else:
        temp+=char
        
result.append(temp[::-1])
print(''.join(result))