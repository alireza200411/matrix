import random
def matrix(rows : int , culomns:int) -> list :
    """This function takes the number of columns and rows from the user and produces a single line matrix."""

    mainlist = []
    for i in range(1 , rows+1) :
        destroy_list = []
        for j in range(1 , culomns+1) :
            ran = random.randint(0 , 10) 
            destroy_list.append(ran)
        else:
            mainlist.append(destroy_list)
    return(mainlist)      