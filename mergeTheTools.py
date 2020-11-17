# https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        s = string[i:i+k] #slicing the string in k no.of parts
        l = list()
        # separting unique values
        for i in s:
            if i not in l:
                l.append(i)
        print(''.join(l))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)