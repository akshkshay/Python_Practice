"""
Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
For e.g. if a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".
Note : Consecutive count of every character in input string is less than equal to 9.
Input Format :
Input string S
Output Format :
Compressed string 
Sample Input:
aaabbccdsa
Sample Output:
a3b2c2dsa
"""


s=input()
i=0
ans=''
while i<len(s)-1:
  if s[i]==s[i+1]:
    count=1
    j=i 
    while j<len(s)-1 and s[j]==s[j+1]:
      count=count+1
      j=j+1
    ans=ans+s[i]+str(count)
    i=j+1
  else:
    ans=ans+s[i]
    i=i+1
if (len(s)>=2 and s[len(s)-1]!=s[len(s)-2]):
  ans=ans+s[len(s)-1]
print(ans)  
