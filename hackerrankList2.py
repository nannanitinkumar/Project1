def insert_list(base_list,dest_list):
    base_list.insert(int(dest_list[1]),int(dest_list[2]))
    return base_list

def append_list(base_list,dest_list):
    base_list.append(int(dest_list[1]))
    return base_list

def extend_list(base_list,dest_list):
    dest_list = dest_list[1:]
    for i in dest_list:
        base_list.extend(int(i))
    return base_list

def remove_list(base_list,dest_list):
    base_list.remove(int(dest_list[1]))
    return base_list

def pop_list(base_list):
    base_list.pop()
    return base_list

def sort_list(base_list):
    base_list.sort()
    return base_list

def reverse_list(base_list):
    base_list.reverse()
    return base_list

def print_list(base_list):
    print base_list
    return base_list

N = input()
base_list = []

for i in range(0,N):
    dest_list = raw_input()
    dest_list = dest_list.split()
    if dest_list[0] == "insert":
        base_list = insert_list(base_list,dest_list)
    elif dest_list[0] == "append":
        base_list = append_list(base_list,dest_list)
    elif dest_list[0] == "extend":
        base_list = extend_list(base_list,dest_list)
    elif dest_list[0] == "remove":
        base_list = remove_list(base_list,dest_list)
    elif dest_list[0] == "pop":
        base_list = pop_list(base_list)
    elif dest_list[0] == "sort":
        base_list = sort_list(base_list)
    elif dest_list[0] == "reverse":
        base_list = reverse_list(base_list)
    elif dest_list[0] == "print":
        base_list = print_list(base_list)
    else:
        pass
