def sort_a_string(input):
    # split the string based on spaces and put into list
    list = input.split()

    # sort based on first letter in every word
    sorted_list = sorted(list, key=str.casefold)

    # convert sorted list into one string with spaces between items
    sorted_string = ' '.join(sorted_list)

    return sorted_string


if __name__ == '__main__':
    input1 = 'string of words'
    output1 = 'of string words'
    assert output1 == sort_a_string(input1)

    input2 = 'banana ORANGE apple'
    output2 = 'apple banana ORANGE'_
    assert output2 == sort_a_string(input2)