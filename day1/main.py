def gathered_list() -> tuple[list, list]:
    left_list, right_list = [], []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            l = line.split(" ")
            test_left = int(l[0])
            test_right = int(l[len(l) - 1].strip())
            left_list.append(test_left)
            right_list.append(test_right)
    return left_list, right_list


def get_distance_list(left_list: list[int], right_list: list[int]):
    dl = []
    for left, right in zip(sorted(left_list), sorted(right_list)):
        distance = abs(left - right)
        dl.append(distance)

    sum = 0
    for distance in dl:
        sum += distance

    return sum


left, right = gathered_list()
print(get_distance_list(left, right))
