

from typing import List


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{str(self.x)}, {str(self.y)}'
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def is_touch(self, other):
        distance = abs(self.x - other.x) + abs(self.y - other.y)
        same_line = self.x == other.x or self.y == other.y
        if same_line and distance<=1:
            return True
        elif same_line and distance ==2:
            return False
        elif not same_line and distance == 2:
            return True
        else: 
            return False



def move_tail(head:Position, prev_head: Position, tail:Position, field: List[List[int]]):
    if not head.is_touch(tail):
        tail.x = prev_head.x
        tail.y = prev_head.y
        
    prev_head.x = head.x
    prev_head.y = head.y
    field[tail.x][tail.y] = 1

def move_tail_list(head:Position, prev_head: Position, tails:List[Position], field: List[List[int]]):
    for i in range(len(tails)):
        temp = Position(tails[i].x, tails[i].y)
        if(i==0):
            if(not head.is_touch(tails[i])):
                tails[i].x = prev_head.x
                tails[i].y = prev_head.y
        else:
            if(not tails[i-1].is_touch(tails[i])):
                tails[i].x = prev_head.x
                tails[i].y = prev_head.y
        prev_head.x = temp.x
        prev_head.y = temp.y
        
    prev_head.x = head.x
    prev_head.y = head.y
    field[tails[-1].x][tails[-1].y] = 1
        


def generate_field(field: List[List[int]], start: Position, steps: List[str]):
    actual: Position = Position(start.x, start.y)
    for step in steps:
        dir,count=step.split(' ')
        if dir=='R':
            for i in range(int(count)):
                actual.y += 1
                if(actual.y) == len(field[actual.x]):
                    for i in range(len(field)):
                        field[i].append(0)
        elif dir=='D':
            for i in range(int(count)):
                actual.x += 1
                if(actual.x) == len(field):
                    field.append([0 for j in range(len(field[actual.x-1]))])
        elif dir=='U':
            for i in range(int(count)):
                actual.x -= 1
                if(actual.x) == -1:
                    field.insert(0,[0 for j in range(len(field[actual.x+1]))])
                    actual.x =0
                    start.x+=1
        elif dir=='L':
            for i in range(int(count)):
                actual.y -= 1
                if(actual.y) == -1:
                    for i in range(len(field)):
                        field[i].insert(0,0)
                    start.y+=1
                    actual.y=0

        # print_field(field, start)
        # print("-"*20)



def print_field(field : List[List[int]], start: Position):
    for i in range(len(field)):
            for j in range(len(field[i])):
                if Position(i,j) == start:
                    print('S', end=' ')
                else:
                    print(field[i][j], end=' ')
            print()
def count_steps(field : List[List[int]]):
    quantity = 0
    for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j] == 1:
                    quantity+=1
    return quantity

def main():
    with open('input.txt') as file:
        input=file.read().split('\n')
        print(input)
        field = [[0]]
        start = Position(0,0)
        generate_field(field, start, input)
        # print_field(field, start)
    H: Position=Position(start.x, start.y)
    T: Position=Position(start.x, start.y)
    H_prev: Position=Position(start.x, start.y)
    for step in input:
        dir,count=step.split(' ')
        if dir=='R':
            for i in range(int(count)):
                H.y += 1
                move_tail(H, H_prev, T, field)
        elif dir=='D':
            for i in range(int(count)):
                H.x += 1
                move_tail(H, H_prev, T, field)
        elif dir=='U':
            for i in range(int(count)):
                H.x -= 1
                move_tail(H, H_prev, T, field)
        elif dir=='L':
            for i in range(int(count)):
                H.y -= 1
                move_tail(H, H_prev, T, field)
        
        # print("-"*20)
    # print_field(field, start)
    print(count_steps(field))
    print("-"*20)
    #part 2 
    H = Position(start.x, start.y)
    T_list = [Position(start.x, start.y) for i in range(9)]
    H_prev = Position(start.x, start.y)
    for i in range(len(field)):
            for j in range(len(field[i])):
                field[i][j] = 0
                
    for step in input:
        dir,count=step.split(' ')
        if dir=='R':
            for i in range(int(count)):
                H.y += 1
                move_tail_list(H, H_prev, T_list, field)
        elif dir=='D':
            for i in range(int(count)):
                H.x += 1
                move_tail_list(H, H_prev, T_list, field)
        elif dir=='U':
            for i in range(int(count)):
                H.x -= 1
                move_tail_list(H, H_prev, T_list, field)
        elif dir=='L':
            for i in range(int(count)):
                H.y -= 1
                move_tail_list(H, H_prev, T_list, field)
    # print_field(field, start)
    print(count_steps(field))

if __name__=='__main__':
    main()