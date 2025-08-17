
def check_win_plants(array_zombies, array_plants):
    plants = 0
    zombies = 0

    min_length = min(len(array_zombies), len(array_plants))
    plants_minus_zombies = len(array_plants) - len(array_zombies)

    for i in range(min_length):

        if array_plants[i] > array_zombies[i]:
            plants += 1

        elif array_plants[i] < array_zombies[i]:
            zombies += 1

    result = plants - zombies + plants_minus_zombies

    if result > 0:
        return True

    elif result == 0:
        if sum(array_plants) >= sum(array_zombies):
            return True
        else:
            return False

    else:
        return False



print(check_win_plants([1, 3, 5, 7], [2, 4, 6, 8]))
print(check_win_plants([1, 3, 5, 7], [2, 4]))
print(check_win_plants([1, 3, 5, 7], [2, 4, 0, 8]))
print(check_win_plants([2, 1, 1, 1], [1, 2, 1, 1]))