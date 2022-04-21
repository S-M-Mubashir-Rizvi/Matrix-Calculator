        # Defining Logics Of Functions Used In My Code #
 
def addition(a,b):                                                             
    print("The required answer for addition is: ")
    result=0
    for i in range(len(a)):
        for j in range(len(b[0])):
            result=(int(a[ i ][ j ])+int(b[ i ][ j ]))
            print("\t",result,end=" ")
        print()


 def subtraction(a,b):                                                      
    print("The required answer for subtraction is: ")
    result=0
    for i in range(len(a)):
        for j in range(len(b[0])):
            result=(int(a[ i ][ j ])-int(b[ i ][ j ]))
            print("\t",result,end=" ")
        print()


 # Logic of both addition and subtraction functions is same:
 
 # I inititalized a result variable with 0 then used nested loops, outer loop iterates the Number of Rows of Matrix 1 while the inner loop iterates the Number of Columns,
 # In statement a[ i ][ j ]+b[ i ][ j ], [ i ] is the index value for rows while [ j ] is the index value for columns, "a" is used for the first Matrix while "b" is used for the second Matrix,
 # After 1 iteration of inner loop, value of " j " is changed and when 1 iteration of outer loop value of " i " is changed, so rows 1st (i.e at 0th index)elements are added first and then second row and so on..
 # I used the print statement inside the inner loop because where an interation is completed it adds a value and stores it in "result" and i print the result,
 # Used end=" " so that all the values of first iteration of inner loop is printed in the same line, "\t" = so that equal space comes b/w the values,
 # Used a empty print() statement in the outer loop so that when one iteration is completed, it prints the values of next iteration in the next line,
 # print() is used also because we used end=" ", if I didnt used the empty print statement all values would have been printed in the same line.


 def multiplication(a,b):                                                       
    print("The required answer for multiplication is: ")
    result=0
    for i in range(len(a)):
        for j in range(len(b[0])):
            adding=0
            for k in range(len(b)):
                adding+=int(a[ i ][ k ])*int(b[ k ][ j ])
                result=adding
            print("\t",result,end="   ")
        print()

 # Logic for multiplication: (reference used from the net)
 
 # Initialized a result variable, used nested loops , the first loop iterates the Number of Rows of Matrix 1, second loop iterates Number of Columns of Matrix 2,
 # Third loop iterates the Number of Rows of Matrix 2, I initialized an "adding" variable after the second loop bcz in multiplication elements are multiplied and then added.
 # a[ i ][ k ] * b[ k ][ j ]:
 
 # in multiplication, we multiply elements of first row of matrix 1 with the elements of first column of matrix 2 and add them together, during this:
 # The Row of the first matrix remains same while its columns are being changed and in the second matrix the Column is fixed and its rows are changing.
 # a[ i ][ k ] = here [ i ] is the index for row and [ k ] is the index for columns, so during the first iteration the Row Number for matrix one remains same while its columns "k" are being changed
 # b[ k ][ j ]= [ k ] is the row index, and [ j ] is the column index, so the Row Number for matrix 2 changes when each iteration of the inner-most loop is completed,
 # while its columns changes when the first iteration of loop " j " is completed.
 
 # so for first iteration , for "a"(matrix 1) , first element: row=0,column=0 , second element: row=0,column=1 and so on.......
 # for "b"(matrix 2), first element: row=0,column=0 , second element: row=1,column=0 and so on......
 # in each iteration the elements are multiplied and keeps adding in the "adding" variable until one iteration of loop "k" is completed, and then stored that value in result,
 # the first print statement is then in " j " loop, cz after 1 iteration of "k" the result for multiplication of first row of matrix 1 and first column of matrix 2 is computed and printed.


 def square(a):                                                                 
    print("The required answer for squaring is: ")
    result=0
    for i in range(len(a)):
        for j in range(len(a[0])):
            adding=0
            for k in range(len(a)):
                adding+=int(a[ i ][ k ])*int(a[ k ][ j ])
                result=adding
            print("\t",adding,end="   ")
        print()

 # Logic is the same as multiplication code, only difference is that the matrix is being multiplied by iteself, thats why the function takes only 1 argument.
 # It is only valid for square matrices.


 def transpose(a):                                                         
    print("The required answer for transpose is: ")
    for j in range(len(a[0])):
        for i in range(len(a)):
            rows=a[i]
            columns=a[i][j]
            rows=columns
            print("\t",rows,end="  ")
        print()

 # Logic for transpose:
 # used nested loops , outer loop iterates the columns for the matrix while the inner loop iterates the rows of the matrix,
 # I stored whatever the value was for Rows in a variable "rows", similarly i stored the values of Column in a variable "columns",
 # and simply just changed the values for "rows" and stored in it the values of "columns", after that i printed the "rows", used the end=" " so that,
 # when the next iteration comes it is printed in the same line, used an empty print statement in the outer loop so that after one iteration the result is printed in the next line.
 
