# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem

# here our task is to return each list from the sorted nested list to the function 'name_format' by using decorator
def person_lister(func):
    def inner(people):
        return [func(person) for person in sorted(people,key=lambda x:int(x[2]))]  # sort by age i.e in 2nd index of each person's list
    return inner

@person_lister # --> person_lister(name_format)
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
