content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}


def make_percentages(a_dictionary):
    copy_dict = a_dictionary.copy()  # create a copy of the dictionary
    total = 0
    for key in a_dictionary:
        count = a_dictionary[key]
        total += count

    for key in copy_dict:  # use the copied table so original isn't changed
        copy_dict[key] = (copy_dict[key] / total) * 100

    return copy_dict


c_ratings_percentages = make_percentages(content_ratings)
print(c_ratings_percentages)
print(content_ratings)
