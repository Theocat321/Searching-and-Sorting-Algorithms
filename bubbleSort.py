#---------------------------------------------------------------------#
# File: c:\Adam\coding\1. VC Coding projects\Searching-and-Sorting-Algorithms\bubbleSort.py
# Project: c:\Adam\coding\1. VC Coding projects\Searching-and-Sorting-Algorithms
# Created Date: Friday, December 31st 2021, 1:07:45 pm
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
# 2021-12-31	AO	Created a working bubble sort
#---------------------------------------------------------------------#

numData = [5,1,6,3,10,82,54,67,23,143,49,1245,4,7,4]

def bubbleSort(array):
    sorted = False
    while sorted == False:
        sortedElements = 0    
        for x in range(len(array)-1):
            if array[x] > array[x+1]:
                temp = array[x+1]
                array[x+1] = array[x]
                array[x] = temp
            #This section is a part of checking if the list is sorted
            elif array[x] <= array[x+1]:
                sortedElements += 1 
            if sortedElements == len(array)-1:
                sorted = True
            
    print(array)
            


def main():
    bubbleSort(numData)


main()