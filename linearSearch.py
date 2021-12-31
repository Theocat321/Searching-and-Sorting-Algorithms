#---------------------------------------------------------------------#
# File: c:\Adam\coding\1. VC Coding projects\Searching-and-Sorting-Algorithms\linearSearch.py
# Project: c:\Adam\coding\1. VC Coding projects\Searching-and-Sorting-Algorithms
# Created Date: Friday, December 31st 2021, 1:01:26 pm
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
# 2021-12-31	AO	Quickly made a linear search for the sake of including all searching alogrithms
#---------------------------------------------------------------------#


numData = [5,7,8,12,15,24,56,78,79,80,84,90,99]
strData = ["adam","bella","cat","james"]

def linearSearch(userData,array):
    foundbool = False
    for element in array:
        if element == userData:
            print("found")
            foundbool = True
            break
    if foundbool == False:
        print("Not in array")        
        
def main():
    linearSearch(78,numData)

main()