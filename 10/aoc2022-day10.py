# encoding: utf-8

def is_special_cycle(cycle):
    return cycle == 20 or (cycle - 20) % 40 == 0
def set_sign(field, i, j, x):
    if(j-1 <= x and x <= j+1):
        field[i].append('I')
    else:
        field[i].append(' ')

def main():
    with open('input.txt') as file:
        lines = file.read().split('\n')


    strength_sum = 0
    x = 1
    cycle = 1
    i = 0
    j = 0
    display = [[]]
    for line in lines:
        if 'addx' in line:
            set_sign(display, i, j, x)
            value = int(line.split(' ')[1])
            cycle += 1
            j += 1
            if(is_special_cycle(cycle)):
                print(cycle)
                strength_sum += cycle * x
            if(j % 40 == 0):
                j = 0
                i += 1
                display.append([])
            set_sign(display, i, j, x)
            x += value
            cycle += 1
            j += 1
            if(j % 40 == 0):
                j = 0
                i += 1
                display.append([])

        else:
            set_sign(display, i, j, x)
            j += 1
            cycle += 1
            if(j % 40 == 0):
                j = 0
                i += 1
                display.append([])

        if(is_special_cycle(cycle)):
            strength_sum += cycle * x

    print(strength_sum)
    for i in range(len(display)):
        for j in range(len(display[i])):
            print(display[i][j], end='')
        print()
if(__name__ == "__main__"):
    main()
    # for i in range(2000):
    #     print(i, chr(i))