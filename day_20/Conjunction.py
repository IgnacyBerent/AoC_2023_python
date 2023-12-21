class Conjunction:
    def __init__(self, name: str, outputs: list[str]):
        self.name = name
        self.inputs = []
        self.outputs = outputs
        self.last_signal = None

    def send(self):
        if all([module.last_signal == 'high' for module in self.inputs]):
            self.last_signal = "low"
            return 'low'
        else:
            self.last_signal = "high"
            return 'high'

    def register_input(self, module):
        self.inputs.append(module)

    def __repr__(self):
        return f'{self.name}'