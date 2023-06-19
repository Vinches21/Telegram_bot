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

some_list = [7, 14, 28, 32, 32, "56"]

def custom_filter(some_list):
    res = 0
    for i in some_list:
        if type(i) != "<class 'int'>":
            continue
        if i % 7 == 0:
            res += i
    if res > 83:
        return False
    else:
        return True

print(custom_filter(some_list))


