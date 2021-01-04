# use recursion https://www.programiz.com/python-programming/recursion


def find_list_indices(value, list):

    return list_of_indices


if __name__ == '__main__':
    value1 = 1
    list1 = [0, 1, 2]
    output1 = 1
    assert output1 == find_list_indices(value1, list1)

    value2 = 1
    list2 = [[[0, 1], 1, [0, 0, 1]], 0, 1]
    output2 = [[0, 0, 1], [0, 1], [0, 2, 2], 2]
    assert output2 == find_list_indices(value2, list2)
