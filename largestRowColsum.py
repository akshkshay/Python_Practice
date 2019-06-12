"""
Given an NxM 2D array, you need to find out which row or column has largest sum (sum of its elements) overall amongst all rows and columns.
Input Format :
 Line 1 : 2 integers N and M respectively, separated by space 
 Line 2: Single line having N*M elements entered in row wise manner, each separated by space.
Output Format :
 If row sum is maximum then - "row" row_num max_sum
 If column sum is maximum then - "column" col_num max_sum
Note : If there are more than one rows/columns with maximum sum consider the row/column that comes first. And if ith row and jth column has same sum (which is largest), consider the ith row as answer.
Sample Input 1 :
2 2 
1 1 1 1
Sample Output 1 :
row 0 2
Sample Input 2 :
3 3
3 6 9 1 4 7 2 8 9
Sample Output 2 :
column 2 25
"""

def largestRowCol(arr):
    # Please add your code here
    
    #ROW_SUM
    rowsum=0
    prowsum=0
    rval=0
    rc = 0
    for row in range(len(arr)):

        for ele in range(len(arr[0])):
            prowsum+=arr[row][ele]
        if prowsum>rowsum:
            rowsum=prowsum
            rval=rc
            # print(rc)
        prowsum=0
        rc+=1
      
    # COLUMN_SUM
    colsum=0
    prcolsum=0
    cval=0
    cc=0

    for j in range(len(arr[0])):

        for ele in range(len(arr)):
            prcolsum+=arr[ele][j]

        if prcolsum>colsum:
            colsum=prcolsum
            cval=cc
        prcolsum=0
        cc+=1

    # print(colsum)
    
    #COMPARISION

    if rowsum>colsum:
        return "row",rval,rowsum
    elif rowsum==colsum:
        return "row",rval,rowsum
    else:
        return "column",cval,colsum



#Main
m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]

l=largestRowCol(arr)
print(*l)
