def set_sign(field, i, j, x):
    if(j-1 <= x and x <= j+1):
        field[i][j].append('#')
    else:
        field[i][j].append('.')
