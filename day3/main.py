import re


def read_file_line_by_line(file_path: str) -> list:
    lines = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            lines.append(line.strip())
    return lines


def extract_multiple() -> list[list[int]]:
    pattern = r"mul\((\d+),(\d+)\)"
    mul_pairs = []
    file_input = read_file_line_by_line("input.txt")
    for line in file_input:
        match_pattern = re.findall(pattern, line)
        mul_pairs = [[int(x), int(y)] for x, y in match_pattern]
    return mul_pairs


def calculation(list_multiples: list[list[int]]) -> int:
    multiplied_list = [x * y for x, y in list_multiples]  # index 0 + index 1
    return sum(multiplied_list)


if __name__ == "__main__":
    print(calculation(extract_multiple()))
