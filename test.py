# users = {1: {"status_game": False,
#                       "total_game": 0,
#                       "wins_game": 0},
#          2: {"status_game": False,
#                       "total_game": 0,
#                       "wins_game": 0},
#          3: {"status_game": False,
#                       "total_game": 0,
#                       "wins_game": 0}
#         }
#
# print(users[1])
# print(len(users))




# res = lambda x: x.lower().count("я") >= 23
#
#
# print(res("Я - последняя буква в алфавите!"))



def anonymous_filter(string):
    return (lambda x: x.lower().count("я")) >= 23

    # count_russian_letters = lambda s: sum([1 for char in s if char.isalpha() and char.lower() == "я"])
    # return count_russian_letters(string) >= 23


print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))


