def main():
    result = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            line = [int(i) for i in line]
            dataset = diff_seq(line)
            result += extrapolate(dataset)
    print(result)


def diff_seq(seq: list[int]) -> list[list[int]]:
    sequences = [seq]
    j = 0
    while True:
        new_seq = []
        for i in range((len(sequences[j]))):
            if i == 0:
                continue
            new_seq.append(sequences[j][i] - sequences[j][i - 1])
        sequences.append(new_seq)
        if all(x == 0 for x in new_seq):
            break
        j += 1

    return sequences


def extrapolate(sequences: list[list[int]]) -> int:
    r_sequences = list(reversed(sequences))
    for i in range(len(r_sequences)):
        if i == 0:
            continue
        if i == len(r_sequences)-1:
            return r_sequences[i - 1][-1] + r_sequences[i][-1]
        r_sequences[i].append(r_sequences[i - 1][-1] + r_sequences[i][-1])


if __name__ == '__main__':
    main()
