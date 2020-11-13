# https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    string = string.upper()
    vowels = ['A', 'E', 'I', 'O', 'U']

    kevsc = 0
    stusc = 0

    for i in range(len(string)):
        # checking whether the letter is vowel
        if string[i] in vowels:
            kevsc += (len(string) - i)  # setting the sum of all the lengths of the possible strings
                                        # i.e the length from the vowel till the end as the score

        # checking whether the letter is consonent
        else:
            stusc += (len(string) - i)  # setting the sum of all the lengths of the possible strings
                                        # i.e the length from the consonent till the end as the score

    # Checking whose score is greater so as to print their 'name and score' or declare the match as 'draw'
    if kevsc > stusc:
        print("Kevin", kevsc)
    elif stusc > kevsc:
        print("Stuart", stusc)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
