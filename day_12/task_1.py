from itertools import combinations


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        all_poss = 0
        for line in lines:
            record, nums = line.strip().split(' ')
            nums = [int(num) for num in nums.split(',')]
            all_poss += calculate_poss(record, nums)
    print(all_poss)


def find_groups_lengths(record: str | list[str]) -> list[int]:
    groups = []
    new_group = 0
    for char in record:
        if char != '.':
            new_group += 1
        else:
            if new_group != 0:
                groups.append(new_group)
                new_group = 0
    if new_group != 0:
        groups.append(new_group)
    return groups


def calculate_poss(record: str, grouping: list[int]) -> int:
    hashes = record.count('#')
    total_nums = sum(grouping)
    n = total_nums - hashes
    marks_pos = [i for i, char in enumerate(record) if char == '?']
    hash_comb = combinations(marks_pos, n)
    possibilities = 0
    for comb in hash_comb:
        record_copy = list(record)
        left_question_marks = [i for i in marks_pos if i not in comb]
        for i in comb:
            record_copy[i] = '#'
        for i in left_question_marks:
            record_copy[i] = '.'
        if find_groups_lengths(record_copy) == grouping:
            possibilities += 1
    return possibilities


if __name__ == '__main__':
    main()
