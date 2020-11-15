def swap_case(s):
    # return s.swapcase() - this is a built in method

    # a solution without using built in method
    output = ""
    for letter in s:
        if letter == letter.upper():
            output += letter.lower()
        else:
            output += letter.upper()
    return output


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
