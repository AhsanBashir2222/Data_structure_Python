my_list = [None, None, None, None, None, None, None, None, None, None]


def hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)

    return sum_of_char % 10


print("Bob has hash code : ", hash_function("Bob"))
# inserting


def add(name):
    index = hash_function(name)
    my_list[index] = name


add("Bob")
add("bob2")
add("bob3")
add("bob4")
add("bob5")
add("bob6")
print(my_list)
