my_list = [[], [], [], [], [], [], [], [], [], []]  # 10 empty


def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10


def add(name):
    index = hash_function(name)
    my_list[index].append(name)


def contain(name):  # add name to the bracket
    index = hash_function(name)
    return my_list[index] == name


add("b1")
add("b2")
add("b3")
add("b4")
add("b5")
print(my_list)
