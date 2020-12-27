# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem

# here our task is to return each list from the sorted nested list to the function 'name_format' by using decorator
def person_lister(f):
    def inner(people):
        return [f(i) for i in sorted(people,key=lambda x:(x[2]))]  # sort by age i.e in 2nd index of each person's list
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')