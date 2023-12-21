from queue import PriorityQueue

from Broadcaster import Broadcaster
from Conjunction import Conjunction
from FlipFlop import FlipFlop

modules = {}
broadcaster = Broadcaster()


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

    send_l = 0
    send_h = 0
    for i in range(1000):
        l, h = press_button()
        send_l += l
        send_h += h

    print(send_l * send_h)


def press_button():
    global broadcaster, modules
    pq = PriorityQueue()
    send_lows = 1
    send_highs = 0
    counter = 0
    # print(f'button -low-> broadcaster')
    for output in broadcaster.outputs:
        receiver = modules[output]
        send_lows += 1
        pq.put((1, counter, receiver, 'low'))
        counter += 1
        # print(f'broadcaster -low-> {receiver}')

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
                        new_receiver = output
                    else:
                        pq.put((order + 1, counter, new_receiver, new_signal))
                        counter += 1
                    finally:
                        # print(f'{receiver} -{new_signal}-> {new_receiver}')
                        if new_signal == 'low':
                            send_lows += 1
                        else:
                            send_highs += 1
    return send_lows, send_highs


if __name__ == '__main__':
    main('input.txt')
