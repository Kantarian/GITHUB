#7. Write a script to concatenate all elements in a list into a string and print it.


def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data(['a', 5, 'b', 2]))
