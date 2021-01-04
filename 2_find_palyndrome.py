def identify_palindrome(input):
    # remove space and other non-text characters from string
    stripped_string = ''.join(ch for ch in input if ch.isalnum())

    # determine how to break the string
    if len(stripped_string) % 2 == 0:
        i = len(stripped_string)/2
        first_part = stripped_string[0:i]
        second_part = stripped_string[i:]
    else:
        i = len(stripped_string) // 2
        first_part = stripped_string[0:i]
        second_part = stripped_string[i:]

    # reverse string
    second_part_reversed = second_part[len(second_part)::-1]
    print(first_part)
    print(second_part_reversed)

    if first_part == second_part_reversed:
        return True
    else:
        return False


if __name__ == '__main__':
    input1 = 'string of words'
    output1 = False
    assert output1 == identify_palindrome(input1)

    input2 = 'meet systeem'
    output2 = True
    assert output2 == identify_palindrome(input2)