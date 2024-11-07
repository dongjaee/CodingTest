num = input().strip() 
dic = dict()

for i in num:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

six_nine_count = dic.get('6', 0) + dic.get('9', 0)
dic['6'] = (six_nine_count + 1) // 2  
if '9' in dic:
    del dic['9']  

max_set_count = max(dic.values())
print(max_set_count)