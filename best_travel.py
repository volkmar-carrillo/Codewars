from itertools import combinations


def choose_best_sum(t, k, ls):
    temp_list = list(filter(lambda x: (x <= t), ls))
    temp_list.sort()
    _sumatories = [sum(combination)
                   for combination in combinations(temp_list, k)]
    _sumatories = list(filter(lambda x: (x <= t), _sumatories))
    _sumatories.sort()
    _sumatories.reverse()

    return _sumatories[0] if bool(_sumatories) else None


if __name__ == "__main__":
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64,
          123, 2333, 144, 50, 132, 123, 34, 89]
    print(choose_best_sum(230, 4, xs))
    print(choose_best_sum(430, 5, xs))
    print(choose_best_sum(430, 8, xs))
