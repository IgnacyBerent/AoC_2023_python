import math
from collections import defaultdict
from queue import PriorityQueue

from Broadcaster import Broadcaster
from Conjunction import Conjunction
from FlipFlop import FlipFlop

modules = {}
broadcaster = Broadcaster()
dd_inputs_dict = defaultdict(int)


def main(file: str):
    global broadcaster, modules
    with open(f'{file}', 'r') as f:
        lines = f.readlines()
    for line in lines:
        module, outputs = line.strip().split(' -> ')
        if module == 'broadcaster':
            broadcaster.register_outputs(outputs.split(', '))
        elif module[0] == '%':
            modules[module[1:]] = FlipFlop(module[1:], outputs.split(', '))
        elif module[0] == '&':
            modules[module[1:]] = Conjunction(module[1:], outputs.split(', '))

    # register inputs for conjunctions
    for conjunctor in [module for module in modules.values() if isinstance(module, Conjunction)]:
        for module in modules.values():
            if conjunctor.name in module.outputs:
                conjunctor.register_input(module)

    presses = 0
    dd_inputs = [module.name for module in modules['dd'].inputs]
    while True:
        presses += 1
        found_receiver = press_button(dd_inputs)
        if found_receiver is not None:
            dd_inputs_dict[found_receiver] = presses
        if all([val != 0 for val in [dd_inputs_dict[dd_input] for dd_input in dd_inputs]]):
            break

    results = [dd_inputs_dict[dd_input] for dd_input in dd_inputs]
    print(lcm(results))


def press_button(dd_inputs: list[str]):
    global broadcaster, modules, dd_inputs_dict
    pq = PriorityQueue()
    counter = 0
    for output in broadcaster.outputs:
        receiver = modules[output]
        pq.put((1, counter, receiver, 'low'))
        counter += 1

    while not pq.empty():
        order, _, receiver, signal = pq.get()
        if signal is not None:
            if isinstance(receiver, FlipFlop):
                receiver.receive(signal)
            new_signal = receiver.send()
            if new_signal is not None:
                for output in receiver.outputs:
                    try:
                        new_receiver = modules[output]
                    except KeyError:
                        pass
                    else:
                        pq.put((order + 1, counter, new_receiver, new_signal))
                        counter += 1
                    finally:
                        if receiver.name in dd_inputs and new_signal == 'high':
                            if dd_inputs_dict[receiver.name] == 0:
                                return receiver.name
    return None


def lcm(numbers):
    lcm_value = numbers[0]
    for i in numbers[1:]:
        lcm_value = lcm_value * i // math.gcd(lcm_value, i)
    return lcm_value


if __name__ == '__main__':
    main('input.txt')
