#!/usr/bin/env python3
# encoding: utf-8
from collections import deque

def deserialize_movements(movements_input):
    movements = []
    for line in movements_input:
        movements.append([int(value) for value in line.split(' ') if value.isnumeric()])
    return movements

def deserialize_stacks(stacks_input):
    stacks = []
    for input in stacks_input[:-1]:
        row = []
        tmp = input.split(' ')
        j = 0
        while j < len(tmp):
            if(tmp[j] == ''):
                j += 4
                row.append('')
            else:
                row.append(tmp[j])
                j+=1
        if(len(stacks) == 0):
            stacks = [[] for i in range(len(row))]
        for i in range(len(row)):
            if(row[i] != ''):
                without_brackets = row[i][1:-1]
                stacks[i].insert(0,(without_brackets))
    return stacks
def rearrange_crane_9000(stacks, movements):
    for move in movements:
        if(len(move) == 3):
            for i in range(move[0]):
                    tmp = stacks[move[1]-1].pop()
                    stacks[move[2]-1].append(tmp)
    return stacks
def rearrange_crane_9001(stacks, movements):
    for move in movements:
        if(len(move) == 3):
            tmp = stacks[move[1]-1][-(move[0]):]
            stacks[move[1]-1] = stacks[move[1]-1][:-move[0]]
            stacks[move[2]-1].extend(tmp)
    return stacks

def main():
    with open('input.txt') as file:
        lines = file.read().split('\n')
        separator = lines.index('')
        stacks = deserialize_stacks(lines[:separator])
        movements = deserialize_movements(lines[separator+1:])

        stacks = rearrange_crane_9000(stacks, movements)
        answer1 = ''.join([stack.pop() for stack in stacks])
        print(answer1)
        
        stacks = deserialize_stacks(lines[:separator])
        stacks = rearrange_crane_9001(stacks, movements)
        answer2 = ''.join([stack.pop() for stack in stacks])
        print(answer2)

if(__name__ == "__main__"):
    main()
