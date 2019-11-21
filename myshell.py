#Michael Lawrence
#CS 350
#Professor Lund



def shell_gap(array, gap):
    for i in range(gap, len(array)):
        #make a hole at the first gap item
        temp = array[i]
        j = i
        while(j >= gap and array[j - gap] >= array[j]):
            #insertion short by the gap size
            array[j] = array[j - gap]
            j -= gap
        #fill the final hole
        array[j] = temp

def shell_sort(array):
    #for short arrays start with smaller gaps
    if(len(array) < 9):
        c = len(array) - 1
    #otherwise start with the max gap of 8
    else:
        c = 8
    while(c > 0):
        #move gap size backwards to zero
        shell_gap(array, c)
        c -= 1

