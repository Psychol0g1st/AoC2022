#!/usr/bin/env python3
# encoding: utf-8


def is_all_different(s: str):
    flag = True
    for c in s:
        splitted = s.split(c)
        if len(splitted) > 2:
            flag = False
            break
    return flag


def main():
    with open("input.txt") as file:
        line = file.read().strip()
        print(line)
        index = 0
        for i in range(len(line) - 14):
            if is_all_different(line[i : 14 + i]):
                index = i + 14
                break
        print(index)


if __name__ == "__main__":
    main()
