#---------------------------------------------------------------------#
# File: c:\Adam\coding\1. VC Coding projects\Searching-and-Sorting-Algorithms\insersionSort.py
# Project: c:\Adam\coding\1. VC Coding projects\Searching-and-Sorting-Algorithms
# Created Date: Friday, December 31st 2021, 1:32:50 pm
# Description: 
# Author: Adam O'Neill
# Copyright (c) 2021 Adam O'Neill
# -----
# Last Modified: Fri Dec 31 2021
# Modified By: Adam O'Neill
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
# 2021-12-31	AO	My version of an inserion sort which is very messy
#---------------------------------------------------------------------#

numData = [1,5,4,6,4,3,10,82,54,67,23,143,49,1245,4,7]

def insertionSort(myArray):
    sortedArray = []

    # Move the first element into the sorted list as the sorted list is empty
    sortedArray.append(myArray[0])
    myArray.pop(0)

    # loops through the unsorted list
    for x in range(len(myArray)):
        # If the first list element is larger than the current sorted array it inserts into sorted list at the end
        if myArray[0] > sortedArray[x]:
            sortedArray.insert(x+1,myArray[0])

        # If the first element is smaller than the current sorted list
        elif myArray[0] < sortedArray[x]:
            # Loops through the sorted list to find where to insert the new element
            for i in range(len(sortedArray)-1):
                if sortedArray[i] <= myArray[0] and sortedArray[i+1] > myArray[0]:
                    sortedArray.insert(i+1,myArray[0])
                    break
        # Removes the first element from the unsorted list
        myArray.pop(0)
        
    print(sortedArray)


def main():
    insertionSort(numData)

main()