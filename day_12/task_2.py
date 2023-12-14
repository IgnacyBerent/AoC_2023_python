from functools import cache

FOLDS = 5


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        all_poss = 0
        for j, line in enumerate(lines):
            record, nums = line.strip().split(' ')
            record_copy = record
            for i in range(FOLDS - 1):
                record += '?'
                record += record_copy
            nums = [int(num) for num in nums.split(',')]
            nums_copy = nums.copy()
            hashes = record.count('#')
            for i in range(FOLDS - 1):
                nums += nums_copy

            poss = calculate_poss_r(record=record, nums=tuple(nums), total_hashes=hashes)
            all_poss += poss
    print(all_poss)


@cache
def calculate_poss_r(record: str, nums: list[int], total_hashes, used_h=0) -> int:
    if not record:
        return 0

    t_hashes = total_hashes
    curr_num = nums[0]
    place_ned = sum(nums) + len(nums) - 2
    place_left = record.count('#') + record.count('?') + record.count('.?') + record.count('.#') - place_ned
    if record[0] == '.':
        place_left -= 1

    u_hashes = []
    shifts = []
    possib = 0

    if not nums[1:]:
        r_l = record
    else:
        r_l = record[:-curr_num]

    if curr_num > len(record):
        return 0

    for i, char in enumerate(r_l):
        if char != '.':
            place_left -= 1
            if not nums[1:]:
                if len(record[i:i + curr_num]) == curr_num and all(x != '.' for x in record[i:i + curr_num]):
                    if used_h + record[i:i + curr_num].count('#') == t_hashes:
                        possib += 1
            else:
                if i == 0:
                    if all(x != '.' for x in record[i:i + curr_num]) and record[i + curr_num] != '#':
                        possib += 1
                        u_hashes.append(record[i:curr_num + i].count('#'))
                        shifts.append(curr_num + i + 1)
                elif i == len(record) - curr_num:
                    if all(x != '.' for x in record[i:i + curr_num]) and record[i - 1] != '#':
                        possib += 1
                        u_hashes.append(record[i:curr_num + i].count('#'))
                        shifts.append(curr_num + i + 1)
                else:
                    if (all(x != '.' for x in record[i:i + curr_num])
                            and record[i - 1] != '#' and record[i + curr_num] != '#'):
                        possib += 1
                        u_hashes.append(record[i:curr_num + i].count('#'))
                        shifts.append(curr_num + i + 1)
            if place_left == 0:
                break
    if not nums[1:]:
        return possib
    else:
        nums = tuple(list(nums)[1:])
        return sum(
            [calculate_poss_r(record=record[shift:], nums=nums, total_hashes=t_hashes, used_h=hashes + used_h) for
             shift, hashes in
             zip(shifts, u_hashes)])


if __name__ == '__main__':
    main()
