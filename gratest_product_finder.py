
# function to get the greatest product of four elements per rows or per columns
# or per diagonals


class GreatesValueinArray:

    def getGreatestVertical(ListofNum_arg, size):
        """
        get the greatest product from 4 combination of adjacent elemnets
        in the columns

        param  ListofNum_arg  this hold the list containing the n x n matrix
        param  size           the size of the matrix (n)

        return greateVert      return the greates value from the product of
                              four adjacent vertical elemnts
        """
        
        columns = []
        product = 1
        greatestVertcl = 0

        combination = get_Combination(size)

        print(ListofNum_arg)
    
        for col in range(size):
            columns = []
            print("column #: ",col)
            for row in range(size):
                print("row #: ",row)
                print(ListofNum_arg[col][row])
                columns.append(ListofNum_arg[col][row])
                print("row #: ",row)
            print(columns)
            greatestinCol = find_Greatest(columns,combination)

                if greatestinCol > greatestVerticl:
                    greatestVerticl = product

        return greatestrow_num
      
    
    


    def getGreatestHorizontal(ListofNum_arg, size):
        """
        get the greatest product from 4 combination of adjacent elemenets
        in the rows

        param  ListofNum_arg  this hold the list containing the n x n matrix
        param  size           the size of the matrix (n)

        return greatHorznt    return the greates value from the product of
                              four adjacent vertical elemnts
        """
        combination = get_Combination(size)
        greatestHorzntl = 0
        
        for row in ListofNum_arg:
            greatestinRow = find_Greatest(row,combination)

            if greatestinRow >= greatestHorzntl:
                greatestHorzntl = product
                    
        return  greatestHorzntl
        

 
    def getGreatestDiagnl(ListofNum_arg, size):

        """
        get the greatest product from 4 combination of adjacent elemnets
        in the diagonals

        param  ListofNum_arg  this hold the list containing the n x n matrix
        param  size           the size of the matrix (n)

        return greatDiagnl    return the greates value from the product of
                              four adjacent diagonal elemnts
        """

        diagonal = []
        lower = []
        upperTriangle = []
        greatestDiagonal = 0

        combination = get_Combination(size)

        for j in range(size):
            diagonal.append(ListofNum_arg[j][j])
        greatestDiagonal = find_Greatest(diagonal,combination)

        if size > 4:
            init_comb = combination - 1
            for row_offset in range(1,size-2):
                for times in range(init_comb):
                    for i in range(4):
                        row = i + row_offset
                        lower.append(ListofNum_arg[row+times][i+times]
                init_comb -= 1


def get_Combination(size):
    """
    each rows,diagonal,columns have K - 3 sets of possible combination
    K is the size of the matrix
        
    calulate the posible combination per colums, rows,and diagonals
        
    param    size    the size of the square array
        
    return           give the maximum posible combination per column,
                         row,and diagonal
                         return 0 if invalid
    """
        
        if size >= 4:
            return size - 3
        else:
            return 0


        
def find_Greatest(Array, combination):
    columns = Array
    greatest_num = 0
        
    for times in range(combination):
        product = 1
        for i in range(4):
            product *= columns[i + times]
        if product >= greatest_num:
            greatest_num = product

    return greatest_num
