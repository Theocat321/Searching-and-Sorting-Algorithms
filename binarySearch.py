#---------------------------------------------------------------------#
# File: c:\Adam\coding\1. VC Coding projects\school-work\Creating Algorithms\binarySearch.py
# Project: c:\Adam\coding\1. VC Coding projects\school-work\Creating Algorithms
# Created Date: Friday, December 31st 2021, 12:24:27 pm
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
# 2021-12-31	AO	After some testing strings can be searched for too!
# 2021-12-31	AO	Created a working binary search for numbers
#---------------------------------------------------------------------#

#Only works for sorted lists

numData = [5,7,8,12,15,24,56,78,79,80,84,90,99]
strData = ["adam","bella","cat","james"]

def findMidPoint(array):
    lenArray = len(array)
    mp = lenArray // 2
    real = array[mp-1]
    return mp,real

def binarySearch(userNum,array):
    mp, mpReal = findMidPoint(array)
    if array[mp-1] == userNum:
        print("Found")
        exit
    elif array[mp-1] < userNum:
        binarySearch(userNum,array[mp:])
    elif array[mp-1] > userNum:
        binarySearch(userNum,array[:mp])

def main():
    try:
        binarySearch("james",strData)
    except:
        print("Not in array")

main()