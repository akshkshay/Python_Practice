"""
Given a string and a character x. Write a function to remove all occurrences of x character from the given string.
Leave the string as it is, if the given character is not present in the string.
Input format :

Line 1 : Input string

Line 2 : Character x

Sample Input :
welcome to coding ninjas
o
Sample Output :
welcme t cding ninjas
"""

## Read input as specified in the question.
## Print output as specified in the question.
str1=input()
char2=input()

li=[]
li=str1.split(" ")

li2=[]
lst1=""
lst2=""
li3=[]
for i in range(0,len(li)):
    if char2 in li[i]:
        li3=li[i]
        # print(li3,"==>li3")
        for k in range(0,len(li3)):
            li2.append(li3[k])
        # print(li2,"==>li2")

        for j in range(0,len(li3)):
            if char2==li3[j]:
                li2.remove(char2)
        # print(li2,"==>after pop li2")
        lst1=li2
        # print(lst1)
        lst2+="".join(lst1)+" "
        # print(lst2,"--> ls2 in")
        li2=[]
        li3=[]
        lst1=""
    else:
        lst2+=li[i]

# print(*li2)
print(lst2)
