#https://www.hackerrank.com/challenges/validate-a-roman-number/problem

# 2 references-
    # https://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-13--regular-expression-matching
    # https://developers.google.com/edu/python/regular-expressions


import re
regex_pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|XI|L?X{0,3})(IX|IV|VI|V?I{0,3})$'# Do not delete 'r'.
print(str(bool(re.match(regex_pattern, input()))))