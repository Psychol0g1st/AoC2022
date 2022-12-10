
class node:
    is_directory = False
    size = 0
    children = []
    parent = None
    name = ""

    def __init__(self, name = '', size = 0, is_directory = False, parent = None):
        self.size = size
        self.is_directory = is_directory
        self.name = name
        self.parent = parent
        self.children = []

    def __str__(self):
        if(self.is_directory):
            return f'{self.name} (dir, {self.size})'
        else:
            return f'{self.name} (file, {self.size})'

    def add_child(self, child):
        self.children.append(child)

def tree(root: node, tab):
    print(tab + str(root))
    tab += "  "
    if len(root.children) > 0:
        for child in root.children:
            tree(child, tab)
def calculate_dir_sizes(root: node):
    if len(root.children) > 0:
        for child in root.children:
            root.size += calculate_dir_sizes(child)
    return root.size

def sum_of_more_than(root: node, limit, sum):
    if len(root.children) > 0:
        for child in root.children:
            sum = sum_of_more_than(child, limit, sum)
    if(root.is_directory and root.size < limit):
        return sum + root.size
    else:
        return sum

def find_the_smalles(root: node, m, limit):
    if root.is_directory :
        if(root.size < m and root.size > limit):
            m = root.size
    if(len(root.children) > 0):
        for child in root.children:
            m = min(m, find_the_smalles(child, m, limit))
    return m
def proceed_line(command: str, active: node, root: node):
    values = command.split()
    if(values[0] == '$'):
        if(values[1] == 'cd'):
            if(values[2] == '/'):
                return root
            elif(values[2] == '..'):
                return active.parent
            else:
                for child in active.children:
                    if child.name == values[2]:
                        return child
        elif(values[1] == 'ls'):
            return active
    else:
        if(values[0] == 'dir'):
            active.children.append(node(values[1], 0, True, active))
        else:
            active.children.append(node(values[1], int(values[0]), False, active))
    return active

def main():
    with open("input.txt") as file:
        lines = file.read().split('\n')
        root = node('/', 0, True, None)
        active = root
        for line in lines:
            active = proceed_line(line,active,root)
        calculate_dir_sizes(root)
        tree(root, '')
        print(sum_of_more_than(root, 100000, 0))
        m = 70000000
        limit = 30000000-(70000000-root.size)
        print(limit)
        m = find_the_smalles(root, m, limit)
        print(m)
if __name__ == "__main__":
    main()
