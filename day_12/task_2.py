from itertools import combinations

FOLDS = 1


def main():
    with open('example.txt', 'r') as f:
        lines = f.readlines()
        all_poss = 0
        for line in lines:
            record, nums = line.strip().split(' ')
            record_copy = record
            for i in range(FOLDS - 1):
                record += '?'
                record += record_copy
            record += '.'
            record = '.' + record
            nums = [int(num) for num in nums.split(',')]
            nums_copy = nums.copy()
            hashes = record.count('#')
            for i in range(FOLDS - 1):
                nums += nums_copy
            all_poss += calculate_poss_r(record, nums, hashes)
    print(all_poss)


def calculate_poss_r(record: str, nums: list[int], total_hashes, used_h=0) -> int:
    t_hashes = total_hashes
    curr_num = nums[0]
    place_ned = sum(nums) + len(nums) - 1
    place_left = record.count('#') + record.count('?') + record.count('.?') + record.count('.#') - place_ned
    if record[0] == '.':
        place_left -= 1
    if not nums[1:]:
        place_left += 1

    u_hashes = []
    shifts = []
    possib = 0
    for i, char in enumerate(record):
        if char != '.':
            if not nums[1:]:
                try:
                    if all(x != '.' for x in record[i:curr_num+i]) and record[i-1] != '#' and record[i+curr_num+1] != '#':
                        if used_h + record[i:curr_num+i].count('#') == t_hashes:
                            possib += 1
                            place_left -= 1
                            if place_left <= 0:
                                break
                except IndexError:
                    break
            else:
                try:
                    if all(x != '.' for x in record[i:curr_num+i]) and record[i-1] != '#' and record[i+curr_num+1] != '#':
                        possib += 1
                        place_left -= 1
                        u_hashes.append(record[i:curr_num+i].count('#'))
                        shifts.append(curr_num+i+1)
                        if place_left <= 0:
                            break
                except IndexError:
                    break
    print(record, nums, possib)
    if not nums[1:]:
        return possib
    else:
        return sum([calculate_poss_r(record[shift:], nums[1:], t_hashes, hashes) for shift, hashes in zip(shifts, u_hashes)])


if __name__ == '__main__':
    main()
