def main():
    workflows_objects = {}

    with open('example.txt', 'r') as file:
        lines = file.readlines()
    workflows = []
    parts = []
    second_group = False
    for line in lines:
        if line == '\n':
            second_group = True
            continue
        if second_group:
            parts.append(line.strip()[1:-1])
        else:
            workflows.append(line.strip())

    for wrk in workflows:
        workflows_objects[wrk.split('{')[0]] = Workflow(wrk.split('{')[1])

    parts_dicts = []
    for part in parts:
        part_dict = {}
        for p in part.split(','):
            key, value = p.split('=')
            part_dict[key] = value
        parts_dicts.append(part_dict)
    


class Workflow:
    def __init__(self, instructions):
        instructions = instructions[:-1]
        self.instructions = []
        for ins in instructions.split(','):
            try:
                condition, next_wf = ins.split(':')
                self.instructions.append((condition, next_wf))
            except ValueError:
                self.instructions.append((None, ins))



if __name__ == "__main__":
    main()