#Michael Lawrence
#timing shell vs insertion sort.

import random
import time
import string
from myshell import shell_sort
from myshell import shell_gap
from myinsertion import insertion

def generate_list(array, length):
    #generates a random array
    random.seed(None)
    for i in range(0, length):
        array.append(random.randint(0, 10000))

def generate_reverse(array, length):
    c = length
    while(c > 0):
        array.append(c)
        c -= 1

def time_shell(array):
    start = time.time()
    shell_sort(array)
    return time.time() - start

def time_insertion(array):
    start = time.time()
    insertion(array)
    return time.time() - start

def time_race():
    #first we will time a shuffled array.
    #insertion sort vs shell sort
    #Shell sort should be faster.
    print("timing shell sort.\n")
    array = [];
    array2 = []
    length = [500, 1000, 1500, 2000]
    for i in range(0, len(length)):
        #time every size
        totals = 0
        totali = 0
        totals_sorted = 0
        totali_sorted = 0
        for j in range(0, 10):
            #times the sorting of a shuffled and already
            #sorted array with the two algorithms
            generate_list(array, length[i])
            generate_list(array2, length[i])
            totals += time_shell(array)
            totali += time_insertion(array2)
            totals_sorted += time_shell(array)
            totali_sorted += time_insertion(array)
            array.clear()
            array2.clear()
            #time it ten times and take the average.
        print("The time average time to shell sort an array of {} items was {} seconds.\n".format(length[i], (totals/10.0)/(i + 1))) 
        print("The time average time to insertion sort an array of {} items was {} seconds.\n".format(length[i], (totali/10.0)/(i + 1)))
        print("The time average time to shell sort a sorted array of {} items was {} seconds.\n".format(length[i], (totals_sorted/10.0)/(i + 1)))
        print("The time average time to insertion sort a sorted array of {} items was {} seconds.\n".format(length[i], (totali_sorted/10.0)/(i + 1)))
        for j in range(0, 10):
            #reverse array race
            generate_list(array, length[i])
            generate_list(array2, length[i])
            totals += time_shell(array)
            totali += time_insertion(array2)
            array.clear()
            array2.clear()
            #time it ten times and take the average.
        print("The time average time to shell sort a reversed array of {} items was {} seconds.\n".format(length[i], (totals/10.0)/(i + 1))) 
        print("The time average time to insertion sort a reversed array of {} items was {} seconds.\n".format(length[i], (totali/10.0)/(i + 1)))
        
def shell_check():
    #checks the validity of sorts by sorting small
    #numbers
    print("checking validity of shell sort.\n")
    array = []
    length = [3, 5, 10, 20]
    for i in range(0, len(length)):
        generate_list(array, length[i])
        shell_sort(array)
        print(array)
        array.clear()
    print("checking validity of insertion sort.\n")
    for i in range(0, len(length)):
        generate_list(array, length[i])
        insertion(array)
        print(array)
        array.clear()

def main():
    if __debug__:
        shell_check()
    else:
        time_race()

if __name__ == '__main__':
    main();
