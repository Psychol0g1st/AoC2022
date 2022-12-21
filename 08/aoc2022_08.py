#!/usr/bin/env python3
# encoding: utf-8

def is_visible_top(forest, tree_i, tree_j):
    height = len(forest)
    width = len(forest[0])
    visible = True    
    #from top
    for i in range(0, tree_i):
        if forest[i][tree_j] >= forest[tree_i][tree_j]:
            visible = False
            break
    return visible
def is_visible_right(forest, tree_i, tree_j):
    height = len(forest)
    width = len(forest[0])
    visible = True
    #from right
    for j in range(tree_j + 1, width):
        if forest[tree_i][j] >= forest[tree_i][tree_j]:
            visible = False
            break
    return visible
def is_visible_bottom(forest, tree_i, tree_j):
    height = len(forest)
    width = len(forest[0])
    visible = True
    #from bottom
    for i in range(tree_i + 1, height):
        if forest[i][tree_j] >= forest[tree_i][tree_j]:
            visible = False
            break
    return visible

def is_visible_left(forest, tree_i, tree_j):
    height = len(forest)
    width = len(forest[0])
    visible = True

    #from left
    for j in range(0, tree_j):
        if forest[tree_i][j] >= forest[tree_i][tree_j]:
            visible = False
            break
    return visible


def scenic_score(forest, tree_i, tree_j):
    height = len(forest)
    width = len(forest[0])
    score = 1
    #from top
    temp = 0
    for i in range(tree_i-1,-1, -1):
        if forest[i][tree_j] < forest[tree_i][tree_j]:
            temp += 1
        else:
            temp += 1
            break
    score *= temp
    #from right
    temp = 0
    for j in range(tree_j + 1, width):
        if forest[tree_i][j] < forest[tree_i][tree_j]:
            temp += 1
        else:
            temp += 1
            break
    score *= temp
    #from bottom
    temp = 0
    for i in range(tree_i + 1, height):
        if forest[i][tree_j] < forest[tree_i][tree_j]:
            temp += 1
        else:
            temp += 1
            break
    score *= temp
    #from left
    temp = 0
    for j in range(tree_j-1, -1, -1):
        if forest[tree_i][j] < forest[tree_i][tree_j]:
            temp += 1
        else:
            temp += 1
            break
    score *= temp
    return score

def main():
    with open('input.txt', 'r') as file:
        lines = file.read().split('\n')
        forest = []
        for line in lines:
            row = []
            for tree in line:
                row.append(int(tree))
            forest.append(row)
        visible_tree = 2 * len(forest) + 2 * (len(forest[0]) - 2)
        scores = []
        for i in range(1, len(forest) - 1 ):
            for j in range(1, len(forest[0]) - 1):
                if is_visible_top(forest, i,j) or is_visible_right(forest, i,j) or is_visible_left(forest, i,j) or is_visible_bottom(forest, i,j):
                    visible_tree += 1
                scores.append(scenic_score(forest, i,j))
        print(visible_tree)
        print(max(scores))


if(__name__ == "__main__"):
    main()