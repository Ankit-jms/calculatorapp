# import re
import math
# word= "a123bc34d8ef34"
# s=re.sub('[^0-9]',' ', word)
# d=s.replace(" ", ",")
# print(d)
# # for i in word:
# #     if i.isalpha():
# #         word.replace('i',' ')
# # # # print(s)
# # # s=set(s)
# # print(word) 
s ="a11111"
arr=[]  
for i in s:
    if i.isnumeric():
        arr.append(i)
# arr=set(arr)
# print(s)
# s=s.remove(' ')
# print(arr)

arr=set(arr)
if len(set(arr))>1:


    arr.remove(max(arr))
    d=max(arr)
else:
    print(-1)

