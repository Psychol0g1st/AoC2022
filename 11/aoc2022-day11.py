# encoding: utf-8

from typing import List

class Monkey:
    def __init__(self):
        self.items: List[int] = []
        self.operation: str = ''
        self.operation_value = 0
        self.test_value: int = 1
        self.monkey_id_if_true: int = -1
        self.monkey_id_if_false: int = -1

def get_starting_items(line: str):
    nums = [int(num) for num in line.replace('Starting items: ', '').strip().split(', ')]
    print(nums)



def main():
    with open('test-input.txt') as file:
        lines = [line for line in file.read().split('\n') if line != '']
        monkeys: List[Monkey] = []
        i = 0
        current_monkey = None
        for line in lines:
            if(i % 6 == 0):
                current_monkey = Monkey()
            elif(i % 6 == 1):
                current_monkey.items = get_starting_items(line)
            

            i+=1

if(__name__ == "__main__"):
    main()
    # for i in range(2000):
    #     print(i, chr(i))