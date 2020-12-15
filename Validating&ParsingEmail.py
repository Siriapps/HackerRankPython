#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
import re
import email.utils
for _ in range(int(input())):
    mail = email.utils.parseaddr(input())
    if re.match(r'^([a-zA-Z0-9][-._]*)+@([a-zA-Z]+)\.([a-zA-Z]){1,3}$',mail[1]):
        print(email.utils.formataddr(mail))
    else:
        continue
