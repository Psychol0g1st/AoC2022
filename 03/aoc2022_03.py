# encoding: utf-8

def find_duplicate(p1, p2):
    for char in p1:
        if char in p2:
            return get_priority(char)
def get_priority(char):
    if (ord(char) >= ord('a') and ord(char) <= ord('z')):
        return ord(char)-ord('a')+1
    else:
        return ord(char)-ord('A')+26+1

def find_common(l):
    l = [''.join(item) for item in l]
    for char in l[0]:
        if char in l[1] and char in l[2]:
            return get_priority(char)
    return 0
def main():
     with open('input.txt') as file:
        lines = file.readlines()
        rucksacks = []
        for line in lines:
            line = line.strip()
            rucksacks.append([line[0:len(line)//2],line[len(line)//2:]])
        points = 0
        group_points = 0
        group = []
        for index,rucksack in enumerate(rucksacks):
            group.append(rucksack)
            if(len(group) % 3 == 0):
                group_points += find_common(group)
                group = []

            points += find_duplicate(rucksack[0], rucksack[1])
        print(points)
        print(group_points)

if(__name__ == "__main__"):
    main()