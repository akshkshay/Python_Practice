"""
Given a two dimensional n*m array, print the array in a sine wave order. i.e. print the first column top to bottom, next column bottom to top and so on.
Note : Print the elements separated by space.
Input format :
n, m, array elements (separated by space)
Sample Input :
3 4 1  2  3  4 5  6  7  8 9 10 11 12
Sample Output :
1 5 9 10 6 2 3 7 11 12 8 4
"""
def wavePrint(arr):
    li=[]
    for i in range(n):

        if i%2==0:
            for row in arr:
                li.append(row[i])
                # print(row[i],"==>")
        else:
              for j in range(m-1,-1,-1):
                  li.append(arr[j][i])

    print(*li)


#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
wavePrint(arr)
