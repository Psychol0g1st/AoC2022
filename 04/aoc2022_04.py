#!/usr/bin/env python3
# encoding: utf-8

def checkForFullyContain(a, b):
    first = [int(section) for section in a.split('-')]
    second = [int(section) for section in b.split('-')]
    if first[0] <= second[0] and first[1] >= second[1]:
        return True
    elif second[0] <= first[0] and second[1] >= first[1]:
        return True
    return False

def isOverlap(a, b):
    first = [int(section) for section in a.split('-')]
    second = [int(section) for section in b.split('-')]
    set1 = set(range(first[0], first[1]+1))
    set2 = set(range(second[0], second[1]+1))
    return len(set1.intersection(set2)) > 0



def main():
    with open('input.txt') as file:
        lines = file.readlines()
        assignments = [ line.strip().split(',') for line in lines ]
        quantityOfFullyContain = 0
        quantityOfOverlapedAssignments = 0
        for assignment in assignments:
            if checkForFullyContain(assignment[0], assignment[1]):
                quantityOfFullyContain += 1
            if isOverlap(assignment[0], assignment[1]):
                quantityOfOverlapedAssignments += 1
                
        print(quantityOfFullyContain)
        print(quantityOfOverlapedAssignments)
if(__name__ == "__main__"):
    main()