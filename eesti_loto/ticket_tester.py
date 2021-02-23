from collections import Counter

#1071(83)
losimine_1071 = [22, 62, 29, 58, 49, 26, 10, 40, 42, 6, 56, 68, 25, 63, 15, 65, 36, 71, 38, 67, 2, 21, 12, 43, 54, 60, 31, 53, 11, 28, 34, 66, 13, 18, 64,
47, 17, 48, 52, 4, 55, 45, 5, 19, 44, 3, 23, 61, 20]

losimine_342 = [5, 19, 43, 11, 12, 18]

list_games_finished = [losimine_1071, losimine_342]

ticket = [22, 62, 29, 72]


def ticker_tester(test_ticket, list_of_games):

    for opa in test_ticket:
        if opa in list_of_games:
            pass
        else:
            print('2')


for huj in list_games_finished:
    ticker_tester(ticket, huj)
