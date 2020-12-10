# Author: NJK (AMDG) 12/9/20

def count_odds(lst):
    num_odds = 1
    total = 0
    while num_odds < total + 1:
        if lst % 2 == 1:
            num_odds == 1
            total == 1
    return(total)


print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)
