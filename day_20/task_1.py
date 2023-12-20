class FlipFlop:
    def __init__(self, name: str, outputs: list[str]):
        self.name = name
        self.on = False
        self.outputs = outputs

    def receive_send(self, signal: str):
        if signal == 'low':
            self.on = not self.on
            if self.on:
                return 'high'
            else:
                return 'low'
        else:
            return None

    def __repr__(self):
        return f'{self.name}'


class Conjunction:
    def __init__(self, name: str, outputs: list[str]):
        self.name = name
        self.inputs = {}
        self.outputs = outputs

    def receive_send(self, module: str, signal: str):
        if signal is not None:
            self.inputs[module] = signal
            if all([s == 'high' for s in self.inputs.values()]):
                return 'low'
            elif all([s == 'low' for s in self.inputs.values()]):
                return 'high'
            else:
                return None

    def register_input(self, module: str):
        self.inputs[module] = 'low'

    def __repr__(self):
        return f'{self.name}'


class Broadcaster:
    def __init__(self):
        self.outputs = []

    def register_outputs(self, outputs: list[str]):
        self.outputs = outputs

    def __repr__(self):
        return f'Broadcaster'


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
                conjunctor.register_input(module.name)

    send_l = 0
    send_h = 0
    seen = set()
    for i in range(1000):
        l, h = press_button()
        state = (l, h)
        if state in seen:
            break
        send_l += l
        send_h += h
        seen.add(state)

    print(send_l, send_h, i)
    result = send_l * send_h * (1000/i)**2
    print(int(result))



def press_button():
    global broadcaster, modules
    send_lows = 1
    send_highs = 0
    stash = []
    print(f'button -low-> broadcaster')
    for output in broadcaster.outputs:
        receiver = modules[output]
        send_lows += 1
        stash.append((receiver, 'low', broadcaster))
        print(f'broadcaster -low-> {receiver}')

    while stash:
        receiver, signal, prev = stash.pop(0)
        if signal is not None:
            if isinstance(receiver, FlipFlop):
                signal = receiver.receive_send(signal)
                if signal is not None:
                    for output in receiver.outputs:
                        try:
                            new_receiver = modules[output]
                        except KeyError:
                            new_receiver = output
                        else:
                            stash.append((new_receiver, signal, receiver))
                        finally:
                            print(f'{receiver} -{signal}-> {new_receiver}')
                            if signal == 'low':
                                send_lows += 1
                            else:
                                send_highs += 1

            elif isinstance(receiver, Conjunction):
                signal = receiver.receive_send(prev.name, signal)
                if signal is not None:
                    for output in receiver.outputs:
                        try:
                            new_receiver = modules[output]
                        except KeyError:
                            new_receiver = output
                        else:
                            stash.append((new_receiver, signal, receiver))
                        finally:
                            print(f'{receiver} -{signal}-> {new_receiver}')
                            if signal == 'low':
                                send_lows += 1
                            else:
                                send_highs += 1

    return send_lows, send_highs


if __name__ == '__main__':
    main('example.txt')
