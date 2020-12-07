# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
# refer - https://www.tutorialspoint.com/python3/python_reg_expressions.htm
import re

consonants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'
pattern = r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])'# '?<='is to check if the front part matches(in this case constants)
                                                                                    # '?='is to check if the last part matches(in this case constants)
output = re.findall(pattern, input(), re.I)# 're.I' considers 'AEIOU' as equal to 'aeiou' same in the case of consonants
print("\n".join(output or ['-1']))
