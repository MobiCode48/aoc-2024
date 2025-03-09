def main() -> int:
    with open("input.txt") as f:
        lines = f.readlines()
        datas = [[int(value) for value in line.strip().split(" ")] for line in lines]
        count = 0
        for data in datas:
            if is_safe(data):
                count += 1
        return count


def is_increasing_case(data: list[int]) -> bool:
    return data[0] < data[len(data) - 1]


def is_safe(data: list[int]) -> bool:
    if is_increasing_case(data):
        # increasing 44 - 45
        if all(
            data[i] < data[i + 1] and data[i + 1] - data[i] <= 3
            for i in range(len(data) - 1)
        ):
            return True
    else:
        # decreasing 58 - 56
        if all(
            data[i] > data[i + 1] and data[i] - data[i + 1] <= 3
            for i in range(len(data) - 1)
        ):
            return True
    return False


if __name__ == "__main__":
    print(main())
