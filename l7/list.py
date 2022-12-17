initial_list = [1, 2, 3]


def duplicate_last(a_list):
    copy_list = a_list.copy()  # making a copy of the list
    last_element = copy_list[-1]
    copy_list.append(last_element)
    return copy_list


new_list = duplicate_last(a_list=initial_list)
print(new_list)
print(initial_list)
