def addition(a,b):                                                                    #Addition Function
    print("The required answer for addition is: ")
    result=0
    for i in range(len(a)):
        for j in range(len(b[0])):
            result=(int(a[ i ][ j ])+int(b[ i ][ j ]))
            print("\t",result,end=" ")
        print()        
def subtraction(a,b):                                                           #Subtraction Function
    print("The required answer for subtraction is: ")
    result=0
    for i in range(len(a)):
        for j in range(len(b[0])):
            result=(int(a[ i ][ j ])-int(b[ i ][ j ]))
            print("\t",result,end=" ")
        print()        
def multiplication(a,b):                                                       #Multiplication Function
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
def square(a):                                                                 #Square Function(only for square matrix)
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
def transpose(a):                                                           #Tranpose Function
    print("The required answer for transpose is: ")
    for j in range(len(a[0])):
        for i in range(len(a)):
            rows=a[i]
            columns=a[i][j]
            rows=columns
            print("\t",rows,end="  ")
        print()
        
while True:
    print("\t\tTypes of Matrix Operations")             # MENU
    print("\t\t\t(1.)Square Matrix""\n\t\t\t(2.)Rectangular Matrix""\n\t\t\t(3.)One square matrix and the other rectangular")
    print("\t",("-")*100)
    flag=0
    Matrix_1=[ ]     # making 2 variables with empty list for 2 matrices
    Matrix_2=[ ]
    print("\t\t{OPERATIONS MENU} : ")          # OPERATIONS MENU
    print("\t\t\t(1.)Addition""\n\t\t{Size of Matrix must be same}""\n\t\t\t(2.)Subtraction""\n\t\t\t(3.)Multiplication""\n\t\t{Column of first Matrix should be equal to row of second Matrix}")
    print("\t\t\t(4.)Square""\n\t\t{Only for Square Matrix}""\n\t\t\t(5.)Transpose""\n\t\t\t(6.)Exit")
    print("\t",("-")*100)
    choice=int(input("Enter choice of operation: "))
    if choice==6:
        print("Exiting\n**{Thank You For Using Matrix Calculator}**")     # Exiting condition i.e choice=6
        print("\t",("-")*100)
        break
    if 5>=choice>=1:             # if correct choice is entered only then it will enter for loop
        for i in range(1,3):       # taking separate values for rows and columns for both matrices
            print("Enter number of rows  for square/rectangular matrix number""{",i,"}"": ",end=" ")       
            rows=int(input())
            print("Enter number of columns  for square/rectangular matrix number""{",i,"}"": ",end=" " )
            columns=int(input())
            print("\t",("-")*100)
            for j in range(1,rows+1):
                if i==1:                              #For Matrix 1
                    print("Enter values for matrix no",i,"row number",j,"separated by comma: ",end="")         # Separate row inputs 
                    value_1=input()
                    val=value_1.split(",")
                    if len(val)==columns:           # checking if user entered correct columns values
                        Matrix_1.append(val)
                        if rows==columns:             # if rows==columns then it is a square matrix then flag==1 we will use later to print a message
                            flag=1
                        elif rows!=columns:           # if rows!=columns then it is a rectangular matrix then flag==2 we will use later to print a message
                            flag=2
                    elif len(val)!=columns:          #if the length of the entered value is not equal to the value of columns then the inputed values are not correct
                        print("Entered values are not correct""\nTry Again")
                        flag=10                                    #entered values are not correct so we incremented flag to use this to break out of the outer for loop, and telling user to enter values again
                        break
                if i==2:                             #For Matrix 2
                    print("Enter values for matrix no",i,"row number",j,"separated by comma: ",end="")   # Separate row inputs
                    value_2=input() 
                    val=value_2.split(",")
                    if len(val)==columns:
                        Matrix_2.append(val)
                        if rows==columns:          # if rows==columns then it is a square matrix then flag==3 we will use later to print a message
                            flag=3
                        elif rows!=columns:        # if rows!=columns then it is a rectangular matrix then flag==4 we will use later to print a message
                            flag=4
                    elif len(val)!=columns:        #if the length of the entered value is not equal to the value of columns then the inputed values are not correct
                        print("Entered values are not correct""\nTry Again")
                        flag=10                       #entered values are not correct so we incremented flag to use this to break out of the outer for loop, and telling user to enter values again
                        break
            if flag==10:              # if flag==10 then it means value of flag was incremented and incorrect values were entered, here we break out of outer most for loop
                break
            if flag==1:   #flag=1?, then a/c to above code we incremented flag for iteration i==1 if the rows and columns were equal
                print("**{Matrix 1 is a square matrix}**")
                print("\t",("-")*100)
            elif flag==2:  #flag=2?, then a/c to above code we incremented flag for iteration i==1 if the rows and columns were unequal
                print("**{Matrix 1 is a rectangular matrix}**")
                print("\t",("-")*100)
            if flag==3:     #flag=3?,then a/c to above code we incremented flag for iteration i==2 if rows and columns were equal
                print("**{Matrix 2 is a square matrix}**")
                print("\t",("-")*100)
            if  flag==4:     #flag=4?, then a/c to above code we incremented flag for iteration i==2 if rows and columns were unequal
                print("**{Matrix 2 is a rectangular matrix}**")
                print("\t",("-")*100)
        if flag!=10:          # flag is unequal to 10 then correct values were entered and we show the user the matrices with the values he entered
            print("Matrix 1 is: ")
            for ROW in Matrix_1:
                print("\t",ROW)
            print("Matrix 2 is: ")
            for ROW in Matrix_2:
                print("\t",ROW)
    elif choice>5 or choice<1: #here we checked if choice of operations was entered incorrect for e.g if user enters any value out of range of operations, it will print some msg and ask again
        print("Enter correct choice number""\nTry Again")
        print("\t",("-")*100)
    if choice==1 and flag!=10:      # user selected choice=1 i.e of addition and flag!=10 shows that loop wasnt break and correct values were entered
        if len(Matrix_1)==len(Matrix_2) and len(Matrix_1[0])==len(Matrix_2[0]):     #here we check if rows and columns of both matrices are equal which is the condition for addition of matrices
            addition(Matrix_1,Matrix_2)
            print("\t",("-")*100)
        elif len(Matrix_1)!=len(Matrix_2) and len(Matrix_1[0])!=len(Matrix_2[0]):    #if rows and columns of both matrices are different to each other then they cant be added
            print("Dimensions of Matrix must be equal")
            print("\t",("-")*100)
            
    if choice==2 and flag!=10:  # user seleceted choice=2 i.e of subtraction and flag!=10 shows that loop wasnt break and correct values were entered
        if len(Matrix_1)==len (Matrix_2) and len(Matrix_1[0])==len(Matrix_2[0]):  # here again we check if rows and columns of both are equal which is also the condition for subtraction
            print("\t\tTypes of Subtraction: ")
            print("\t\t\t(1.)Subtract Matrix 2 from Matrix 1""\n\t\t\t(2.)Subtract Matrix 1 from Matrix 2")
            subtr_choice=int(input("Enter subtraction choice number: "))  # here i am giving the user the choice to either subtract matrix 2 from 1 or subract matrix 1 from 2
            print("\t",("-")*100)  
            if subtr_choice==1:
                subtraction(Matrix_1,Matrix_2)   #if s/he wants to subract matrix 2 from 1 then a/c to our SUBTRACTION FUNCTION, first arguement must be of Matrix 1
                print("\t",("-")*100)        
            if subtr_choice==2:                           #if s/he wants to subract matrix 1 from 2 then a/c to our SUBTRACTION FUNCTION, first arguement must be of Matrix 2
                subtraction(Matrix_2,Matrix_1)
                print("\t",("-")*100)
        elif len(Matrix_1)!=len(Matrix_2) and len(Matrix_1[0])!=len(Matrix_2[0]):     #here if rows and columns of both matrices are different then subtraction of matrices is not possible
            print("Dimensions of Matrix must be equal")
            print("\t",("-")*100)    
    if choice==3 and flag!=10:     #user selected choice=3 i.e of multiplication and flag!=10 indicates that loop didnt break and correct values were entered
        print("\t\tTypes of Multiplication: ")
        print("\t\t\t(1.)Multiply Matrix 1 with Matrix 2""\n\t\t\t(2.)Multiply Matrix 2 with Matrix 1")
        multiply_choice=int(input("Enter multiplication choice number: "))  #here i gave user the freedom if he/she wants to multiply matrix 1 with 2 or matrix 2 with 1 (bcz results are different)
        print("\t",("-")*100)        
        if multiply_choice==1:   # user wants to multiply matrix 1 with matrix 2
            if len(Matrix_1[0])==len(Matrix_2):     #so if columns of first matrix i.e(Matrix1) is equal to rows of second matrix i.e(Matrix2) only then is multiplication possible
                multiplication(Matrix_1,Matrix_2)
                print("\t",("-")*100)
            else:                           # if column of first matrix is not equal to the rows of second matrix then multiplication is not possible
                print("Multiplication is not possible, since column of first Matrix is not equal to the row of second Matrix")            
        if multiply_choice==2: # user wants to multiply matrix 2 with 1
            if len(Matrix_2[0])==len(Matrix_1):  # so if columns of first matrix i.e(Matrix 2) is equal to rows of second matrix i.e(Matrix1) only then multiplication is possible
                multiplication(Matrix_2,Matrix_1)
                print("\t",("-")*100)
            else:                             #if column of first matrix is not equal to rows of second one then mulitplication is not possible
                print("Multiplication is not possible, since column of first Matrix is not equal to the row of second Matrix")
                print("\t",("-")*100)
            
    if choice==4 and flag!=10: #user selected choice=4 i.e of squaring of matrix and flag!=10 indicates that loop didnt break and correct values were entered
        print("\t\t\t(1.)Square of Matrix 1""\n\t\t\t(2.)Square of Matrix 2")
        square_choice=int(input("Enter one of the above choice "))        #asking if he/she wants to have a square of Matrix 1 or Matrix 2
        if square_choice==1 and len(Matrix_1)==len(Matrix_1[0]):
                square(Matrix_1)
                print("\t",("-")*100)
        elif len(Matrix_1)!=len(Matrix_1[0]): #made a condition that squaring is only possible for square matrix, bcz squaring is simple multiplication with the matrix itself for which the condition,
            print("Squaring not possible of a rectangular matrix")          # column of first==rows of second , which is only possible for a square matrix  
        if square_choice==2 and len(Matrix_2)==len(Matrix_2[0]):            # the square of a rectangular matrix is not possible 
                square(Matrix_2)                     # for e.g if a rectangular matrix has rows=2 and columns=3 (assume it matrix1)and we want to square it then we multiply it with itself
                print("\t",("-")*100)                   # i.e we multiply it with the same matrix having rows=2 and columns =3(assume it matrix2), here it shows that since the column of matrix1 is not 
        elif not(len(Matrix_2)==len(Matrix_2[0])):               # equal to the rows of matrix2 , it proves that squaring of rectangular matrix is not possible
            print("Squaring not possible of a rectangular matrix")
            print("\t",("-")*100)
            
    if choice==5 and flag!=10:     # user selected choice=5 i.e of transpose and flat!=10 shows that loop didnt break and correct values were entered
        print("\t\t\t(1.)Transpose Matrix Number 1""\n\t\t\t(2.)Transpose Matrix Number 2")
        transpose_choice=int(input("Select choice from above mentioned choices: ")) #giving user the freedom to select the matrix he/she wants to transpose
        print("\t",("-")*100)        
        if transpose_choice==1:
            transpose(Matrix_1)
            print("\t",("-")*100)            
        if transpose_choice==2:
            transpose(Matrix_2)
            print("\t",("-")*100)
            


